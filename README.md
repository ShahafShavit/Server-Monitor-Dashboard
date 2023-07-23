# Server-Monitor-Dashboard
Real-time web-based system resource monitor built with Flask and JavaScript, utilizing Chart.js for data visualization. 
The application fetches and displays live server performance metrics such as CPU usage, RAM usage, Disk I/O, and Network I/O.
Additional features include per-core CPU usage and average value computation for disk and network metrics.

## Installation

### Prerequisites

Before starting the installation process, make sure to have the following programs installed:

- **Python 3.7 or newer**: Python is the programming language used for this project. Download it from the [official Python website](https://www.python.org/downloads/). During installation, make sure to add Python to your PATH.

- **pip (Python Package Installer)**: pip is a package manager for Python. It comes with Python 3.4 or later.

- **git**: Git is a version control system that lets you manage and keep track of your source code history. Download it from the [official Git website](https://git-scm.com/downloads).

### Step-by-step Guide

Follow the steps below to install and run the project:

1. **Clone the Repository**

   Open a terminal or command prompt, navigate to where you want to place the project, and run the `git clone` command:
   ```
   git clone https://github.com/ShahafShavit/Server-Monitor-Dashboard.git
   ```

2. **Navigate to the Project Directory**

Change your current working directory to the newly cloned repository:
```
cd Server-Monitor-Dashboard
```
3. **Create a Virtual Environment**

Use the `venv` module that comes with Python to create a virtual environment:
```
python -m venv venv
```

4. **Activate the Virtual Environment**

To use the virtual environment, you need to activate it:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

5. **Install Required Python Packages**

With your virtual environment activated, install the Python packages that the project needs:
```
pip install -r requirements.txt
```

## Running the Project

1. **Set FLASK_APP Environment Variable**

Before starting the server, set the FLASK_APP environment variable to point to the app file:

- On Windows:
  ```
  set FLASK_APP=main.py
  ```
- On Unix or MacOS:
  ```
  export FLASK_APP=main.py
  ```

2. **Start the Server**

Start the Flask server with the following command:
```
flask run
```

You should now be able to access the application at `http://localhost:5000`.


## Accessing the Application from Another Computer in the Same LAN

1. **Find Your Host Machine's Internal IP Address**

    You will need to know the internal IP address (IPv4) of the host machine (the one running the Flask server). Here's how you can find it:

   - On Windows:
     - Open the Command Prompt and type `ipconfig`. Look for "IPv4 Address".
   
   - On Unix or MacOS:
     - Open Terminal and type `ifconfig`. Look for "inet" under your network adapter.

2. **Run Flask with Host Parameter**

   By default, the Flask server only responds to requests from the host machine. To allow connections from any device on the same network, you need to run Flask with the `--host` parameter set to `0.0.0.0`:
```
flask run --host=0.0.0.0
```

3. **Access the Application**

From the other computer, open a web browser and enter the host machine's internal IP address followed by `:5000` (the port number). For example, if the host's internal IP address is `192.168.1.123`, you would enter `http://192.168.1.123:5000`.

Remember to replace `"192.168.1.123"` with the actual internal IP address of your host machine.


