import csv
import random
import time
from datetime import datetime

file_path = "/Users/j.ruchithareddy/.n8n-files/sensor_data.csv";
# Create CSV file with headers if it doesn't exist
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "temperature", "pressure", "vibration"])

print("Sensor generator started...")

while True:
    time_now = datetime.now().strftime("%H:%M:%S")

    temperature = round(random.uniform(60, 110), 2)
    pressure = round(random.uniform(90, 150), 2)
    vibration = round(random.uniform(2, 10), 2)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time_now, temperature, pressure, vibration])

    print("Generated:", time_now, temperature, pressure, vibration)

    time.sleep(2)
