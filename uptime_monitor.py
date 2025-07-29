import random
import time
import csv
from datetime import datetime
import os

LOG_FILE = "data/uptime_log.csv"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Create CSV with header if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "status", "response_time"])

def check_uptime():
    status = random.choice(["UP", "DOWN"])
    response_time = round(random.uniform(0.1, 1.5), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"🌐 STATUS: {status} | Response Time: {response_time}s")

    if status == "DOWN":
        print("🔴 ALERT: System is currently DOWN!")
    else:
        print("🟢 All systems operational.")

    # Append result to CSV
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status, response_time])

# Run multiple checks
for _ in range(10):
    check_uptime()
    time.sleep(1)
