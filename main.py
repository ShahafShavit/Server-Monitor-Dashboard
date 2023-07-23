from flask import Flask, jsonify, render_template
import psutil
import time
import threading
from socket import gethostname

INTERVAL = 2000
CACHE = 60

app = Flask(__name__)
app.config['DEBUG'] = True

# Initialize a global state dictionary for all metrics
state = {
    'machine': {
        'name': gethostname()
    },
    'cpu': [],
    'ram': 0,
    'disk': {
        'read_speed': 0,
        'write_speed': 0
    },
    'network': {
        'sent_speed': 0,
        'recv_speed': 0
    },
    'total_cpu': 0,
    'settings': {
        'interval': INTERVAL,
        'cache': CACHE,
    },
}

disk_io_start = psutil.disk_io_counters()
disk_io = psutil.disk_io_counters(perdisk=True)
print(disk_io['PhysicalDrive1'])
net_io_start = psutil.net_io_counters()
time_start = time.time()

# This is the function that will be running in a separate thread, updating the state every second
def update_state():
    global state, disk_io_start, net_io_start, time_start
    while True:
        time.sleep(INTERVAL/1000)
        current_time = time.time()
        time_diff = current_time - time_start

        # Update CPU and RAM metrics
        state['cpu'] = [round(cpu, 2) for cpu in psutil.cpu_percent(percpu=True)]
        cpu_array = state['cpu']
        new_cpu_array = []
        for cpu in cpu_array:
            new_cpu_array.append(str(cpu) + '%')
        state['cpu'] = new_cpu_array
        state['ram'] = psutil.virtual_memory().percent
        state['total_cpu'] = psutil.cpu_percent()

        # Update disk IO metrics
        current_disk_io = psutil.disk_io_counters()
        state['disk']['read_speed'] = (current_disk_io.read_bytes - disk_io_start.read_bytes)*8 / time_diff   # in Bits per second
        state['disk']['write_speed'] = (current_disk_io.write_bytes - disk_io_start.write_bytes)*8 / time_diff   # in Bits per second
        disk_io_start = current_disk_io

        # Update network usage metrics
        current_net_io = psutil.net_io_counters()
        state['network']['sent_speed'] = (current_net_io.bytes_sent - net_io_start.bytes_sent)*8 / time_diff  # in Bits per second
        state['network']['recv_speed'] = (current_net_io.bytes_recv - net_io_start.bytes_recv)*8 / time_diff  # in Bits per second
        net_io_start = current_net_io

        time_start = current_time

        # Sleep for 1 second before the next update


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(state)

if __name__ == "__main__":
    # Start the update_state function in a separate thread
    threading.Thread(target=update_state).start()

    # Run the Flask app
    app.run(host='0.0.0.0', debug=True)
