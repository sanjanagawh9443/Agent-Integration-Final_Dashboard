import pandas as pd

def detect_issues(file='deployment_log.csv'):
    try:
        df = pd.read_csv(file)
        recent = df.tail(5) # check last 5 entries
        failures = recent[recent['result'] == 'failure']
        count = failures.shape[0]

        print(f"❌ Failures in last 5 deploys: {count}")
        if count > 1:
            print("⚠️ WARNING: Frequent Deployment Failures Detected!")
        else:
            print("✅ System looks stable.")
    except FileNotFoundError:
        print("File not found. Please check your deployment_log.csv.")

# Run the function
detect_issues()