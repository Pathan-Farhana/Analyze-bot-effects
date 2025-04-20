import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the traffic log
df = pd.read_csv('traffic_log.csv')


print("📄 Columns in the file:")
print(df.columns)
print("\n🧾 First few rows:")
print(df.head())

# Clean column names: strip spaces + lowercase
df.columns = df.columns.str.strip().str.lower()

# Convert 'timestamp' column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot 1: Page visits count
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='endpoint', order=df['endpoint'].value_counts().index, palette="viridis")
plt.title('Page Visit Frequency')
plt.xlabel('Page')
plt.ylabel('Number of Visits')
plt.tight_layout()
plt.show()

# Plot 2: Top User-Agents
plt.figure(figsize=(10,6))
sns.countplot(data=df, y='user_agent', order=df['user_agent'].value_counts().head(6).index, palette="coolwarm")
plt.title('Top 6 User-Agents (Bots)')
plt.xlabel('Visits')
plt.ylabel('User-Agent')
plt.tight_layout()
plt.show()
