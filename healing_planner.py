import pandas as pd
import random

error_list = ["high_latency", "crash_error", "memory_spike"]
fix_actions = ["retry_deploy", "restore_version", "adjust_threshold"]

log = []

# Simulate fixing each error
for error in error_list:
    action = random.choice(fix_actions)
    result = random.choice(["success", "fail"])
    log.append({"error_type": error, "fix_action": action, "result": result})

# Save to CSV
df = pd.DataFrame(log)
df.to_csv("healing_log.csv", index=False)
print("✅ Healing log updated.")
print(df)