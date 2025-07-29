import csv
import random
from datetime import datetime

def simulate_deployment():
    # Simulate fake deploy result
    result = random.choice(["success", "failure"])
    response_time = round(random.uniform(0.5, 2.5), 2)  # fake response time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare row for log
    log_entry = [timestamp, result, response_time]

    # Log to CSV
    with open("deployment_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(log_entry)

    print(f"📦 Deployment: {result.upper()} | Time: {timestamp} | Response Time: {response_time}s")

# Run the deployment agent
simulate_deployment()
