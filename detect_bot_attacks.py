# import pandas as pd

# # Load logs
# df = pd.read_csv("traffic_log.csv")
# df.columns = df.columns.str.lower().str.replace(" ", "_")
# df['endpoint'] = df['endpoint'].str.lower().str.strip()

# # 🛒 Cart Hoarding: same IP hits /cart a lot
# cart_ips = df[df['endpoint'].str.contains("cart", na=False)]
# cart_counts = cart_ips['ip_address'].value_counts()
# cart_bot_ips = cart_counts[cart_counts > 5].index.tolist()

# # 🧾 Signup Flood: same IP hitting /signup repeatedly
# signup_ips = df[df['endpoint'].str.contains("signup", na=False)]
# signup_counts = signup_ips['ip_address'].value_counts()
# signup_bot_ips = signup_counts[signup_counts > 3].index.tolist()

# # 🕷️ Scraping: IP visited many different endpoints
# endpoint_diversity = df.groupby('ip_address')['endpoint'].nunique()
# scraper_ips = endpoint_diversity[endpoint_diversity > 4].index.tolist()

# # 🧠 Combine all bot IPs
# all_bot_ips = set(cart_bot_ips + signup_bot_ips + scraper_ips)

# # ✅ Print
# print("📍 Cart Hoarding IPs:", cart_bot_ips)
# print("📍 Signup Flood IPs:", signup_bot_ips)
# print("📍 Scraping IPs:", scraper_ips)
# print("🔐 Total Unique Bot IPs:", len(all_bot_ips))
# print("🧾 All Detected Bot IPs:\n", list(all_bot_ips))

# # 💾 Optional: Save to file
# with open("detected_bot_ips.txt", "w") as f:
#     for ip in all_bot_ips:
#         f.write(f"{ip}\n")


import pandas as pd

# Load logs
df = pd.read_csv("traffic_log.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")
df['endpoint'] = df['endpoint'].str.lower().str.strip()

# 🛒 Cart Hoarding: same IP hits /cart a lot
cart_ips = df[df['endpoint'].str.contains("cart", na=False)]
cart_counts = cart_ips['ip_address'].value_counts()
cart_bot_ips = cart_counts[cart_counts > 5].index.tolist()

# 🧾 Signup Flood: same IP hitting /signup repeatedly
signup_ips = df[df['endpoint'].str.contains("signup", na=False)]
signup_counts = signup_ips['ip_address'].value_counts()
signup_bot_ips = signup_counts[signup_counts > 3].index.tolist()

# # 🕷️ Scraping: IP visited many different endpoints
# endpoint_diversity = df.groupby('ip_address')['endpoint'].nunique()
# scraper_ips = endpoint_diversity[endpoint_diversity > 4].index.tolist()

# # 🔐 Brute Force Attack: multiple login attempts from the same IP (without status)
# login_ips = df[df['endpoint'].str.contains("login", na=False)]
# login_counts = login_ips['ip_address'].value_counts()
# brute_force_ips = login_counts[login_counts > 10].index.tolist()

# # 🗨️ Comment Spam: same IP submitting many comments
# comment_ips = df[df['endpoint'].str.contains("comment", na=False)]
# comment_counts = comment_ips['ip_address'].value_counts()
# comment_spam_ips = comment_counts[comment_counts > 20].index.tolist()

# # 💵 Price Scraping: same IP accessing price-related endpoints frequently
# price_scrape_ips = df[df['endpoint'].str.contains("price", na=False)]
# price_scrape_counts = price_scrape_ips['ip_address'].value_counts()
# price_scraping_ips = price_scrape_counts[price_scrape_counts > 10].index.tolist()

# # 🔍 Account Enumeration: checking multiple usernames or email addresses
# account_enum_ips = df[df['endpoint'].str.contains("check_user", na=False)]
# account_enum_counts = account_enum_ips['ip_address'].value_counts()
# account_enum_bot_ips = account_enum_counts[account_enum_counts > 5].index.tolist()

# 🧠 Combine all bot IPs
all_bot_ips = set(cart_bot_ips + signup_bot_ips)

# ✅ Print
print("📍 Cart Hoarding IPs:", cart_bot_ips)
print("📍 Signup Flood IPs:", signup_bot_ips)
# print("📍 Scraping IPs:", scraper_ips)
# print("📍 Brute Force IPs:", brute_force_ips)
# print("📍 Comment Spam IPs:", comment_spam_ips)
# print("📍 Price Scraping IPs:", price_scraping_ips)
# print("📍 Account Enumeration IPs:", account_enum_bot_ips)
print("🔐 Total Unique Bot IPs:", len(all_bot_ips))
print("🧾 All Detected Bot IPs:\n", list(all_bot_ips))

# 💯 Total Number of Bots
total_bots = len(cart_bot_ips) + len(signup_bot_ips)
print("💥 Total Number of Bots Detected:", total_bots)

# 💾 Optional: Save to file
with open("detected_bot_ips.txt", "w") as f:
    for ip in all_bot_ips:
        f.write(f"{ip}\n")
