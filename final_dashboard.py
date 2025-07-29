import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs
ph = pd.read_csv("patient_health.csv")
ss = pd.read_csv("student_scores.csv").dropna()
dl = pd.read_csv("deployment_log.csv", on_bad_lines='skip')
hl = pd.read_csv("healing_log.csv")
ul = pd.read_csv("uptime_log.csv")

# --- Page Setup ---
st.set_page_config(layout="wide", page_title="DevOps + EdTech Agent Dashboard")
st.title("DevOps + EdTech Agent Dashboard")

# --- Section 1: Patient Health Overview ---
st.header("1. Patient Health Overview")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Heart Rate Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=ph, x="timestamp", y="heart_rate", marker="o", ax=ax)
    fig.autofmt_xdate()
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Oxygen Level vs BP")
    fig, ax = plt.subplots()
    sns.scatterplot(data=ph, x="bp", y="oxygen", hue="timestamp", palette="cool", ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

# --- Section 2: Student Score Overview ---
st.header("2. Student Score Overview")
fig, ax = plt.subplots()
sns.barplot(data=ss, x="subject", y="score", hue="name", ax=ax)
plt.title("Scores by Subject")
fig.autofmt_xdate()
plt.tight_layout()
st.pyplot(fig)

# --- Section 3: Deployment Logs ---
st.header("3. Deployment Agent Logs")
st.dataframe(dl)
success_rate = dl['result'].value_counts(normalize=True).get("success", 0) * 100
st.metric("Deployment Success Rate", f"{success_rate:.2f}%")

# --- Section 4: Uptime Monitor Logs ---
st.header("4. Uptime Monitor Logs")
st.dataframe(ul)
fig, ax = plt.subplots()
ul['timestamp'] = pd.to_datetime(ul['timestamp'])
ul['status_binary'] = ul['status'].map({'UP': 1, 'DOWN': 0})
sns.lineplot(data=ul, x="timestamp", y="status_binary", drawstyle="steps-post", ax=ax)
ax.set_yticks([0, 1])
ax.set_yticklabels(['DOWN', 'UP'])
ax.set_title("Uptime Over Time")
fig.autofmt_xdate()
plt.tight_layout()
st.pyplot(fig)

# --- Section 5: Healing Agent Logs ---
st.header("5. Healing Actions Log")
st.dataframe(hl)
success_count = (hl['result'] == 'success').sum()
total_actions = len(hl)
st.metric("Healing Success Rate", f"{(success_count/total_actions)*100:.2f}%")

# --- Section 6: RL Agent Policy Simulation ---
st.header("6. RL Agent Policy (Simulated)")
st.write("(Simulated Q-Learning outcomes based on Healing Log)")
st.bar_chart(hl['fix_action'].value_counts())

st.success("Dashboard Loaded Successfully")
