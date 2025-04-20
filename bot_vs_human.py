import pandas as pd
import matplotlib.pyplot as plt

# Load the log file
df = pd.read_csv('traffic_log.csv')

# Convert column to datetime (fix casing issue if needed)
df.rename(columns=lambda x: x.strip().lower(), inplace=True)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Define bot indicators (common patterns in User-Agent strings)
bot_keywords = ['curl', 'python-urllib', 'bot', 'scrapy', 'spider']

# Function to check if user agent is a bot
def is_bot(user_agent):
    return any(bot in user_agent.lower() for bot in bot_keywords)

# Add a new column to label requests
df['Traffic Type'] = df['user agent'].apply(lambda ua: 'Bot' if is_bot(ua) else 'Human')

# Count bot vs human
traffic_counts = df['Traffic Type'].value_counts()

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(traffic_counts, labels=traffic_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'skyblue'])
plt.title('Bot vs Human Traffic')
plt.axis('equal')
plt.tight_layout()
plt.show()
