from flask import Flask, jsonify, render_template
import psutil
import time

app = Flask(__name__)
# app.config['DEBUG'] = True

disk_io_start = psutil.disk_io_counters()
net_io_start = psutil.net_io_counters()
time_start = time.time()
prev_sent_speed = 0
prev_recv_speed = 0

def get_cpu_utilization():
    return [round(cpu, 2) for cpu in psutil.cpu_percent(percpu=True)]

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_io_usage():
    global disk_io_start, time_start
    current_disk_io = psutil.disk_io_counters()
    current_time = time.time()
    time_diff = current_time - time_start

    read_speed = (current_disk_io.read_bytes - disk_io_start.read_bytes) / time_diff / (1024 * 1024)  # in MB/s
    write_speed = (current_disk_io.write_bytes - disk_io_start.write_bytes) / time_diff / (1024 * 1024)  # in MB/s

    disk_io_start = current_disk_io
    time_start = current_time

    return {
        'read_speed': read_speed,
        'write_speed': write_speed
    }

def get_network_usage():
    global net_io_start, time_start, prev_sent_speed, prev_recv_speed
    current_net_io = psutil.net_io_counters()
    current_time = time.time()
    time_diff = current_time - time_start
    if time_diff > 0:
        sent_speed = (current_net_io.bytes_sent - net_io_start.bytes_sent) / time_diff  # in Bytes per second
        recv_speed = (current_net_io.bytes_recv - net_io_start.bytes_recv) / time_diff  # in Bytes per second
        prev_sent_speed = sent_speed
        prev_recv_speed = recv_speed
    else:
        sent_speed = prev_sent_speed
        recv_speed = prev_recv_speed
    
    net_io_start = current_net_io
    time_start = current_time
    return {
        'sent_speed': sent_speed,
        'recv_speed': recv_speed
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({
        'cpu': get_cpu_utilization(),
        'ram': get_ram_usage(),
        'disk': get_disk_io_usage(),
        'network': get_network_usage(),
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
