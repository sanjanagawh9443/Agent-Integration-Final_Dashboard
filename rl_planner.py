import pandas as pd

df = pd.read_csv("healing_log.csv")

# Group by error type and fix action to count success
summary = df[df['result'] == 'success'].groupby(['error_type', 'fix_action']).size().reset_index(name='success_count')

# Best fix for each error type
best_fixes = summary.sort_values('success_count', ascending=False).drop_duplicates('error_type')

print(" RL Suggested Best Fixes:")
print(best_fixes)