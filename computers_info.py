import psutil
import subprocess
import csv
import os
import sys
import importlib

try:
    importlib.import_module('psutil')
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    importlib.reload(sys.modules[__name__])
    import psutil

def get_system_info():
    hostname = os.getenv('COMPUTERNAME')
    ram = psutil.virtual_memory().total / (1024 * 1024 * 1024)
    disk = psutil.disk_usage('/').free / (1024 * 1024 * 1024)
    manufacturer = subprocess.check_output('wmic computersystem get manufacturer').decode().strip()
    model = subprocess.check_output('wmic computersystem get model').decode().strip()

    return [hostname, manufacturer, model, ram, disk]


def write_to_csv(system_info):
    with open('system_info.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Hostname', 'Manufacturer', 'Model', 'RAM (GB)', 'Free Disk Space (GB)'])
        writer.writerow(system_info)




system_info = get_system_info()
write_to_csv(system_info)
