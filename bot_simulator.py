import requests
import random
import time

# Base URL of your Flask server
BASE_URL = "http://127.0.0.1:5000"

# Fake user-agents to simulate browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
    "curl/7.68.0",
    "Python-urllib/3.9"
]

# Pages the bot will hit
pages = ["/", "/products", "/cart", "/signup"]

# Simulate multiple bot visits
for i in range(20):  # You can increase to 100+ later
    page = random.choice(pages)
    agent = random.choice(user_agents)

    headers = {
        "User-Agent": agent
    }

    try:
        response = requests.get(BASE_URL + page, headers=headers)
        print(f"[{i+1}] Bot visited {page} with User-Agent: {agent} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error visiting {page}: {e}")

    time.sleep(random.uniform(0.5, 2))  # Sleep to mimic human-ish delays


# # import requests
# # import random
# # import time
# # import threading

# # # Base URL of your Flask server
# # BASE_URL = "http://127.0.0.1:5000"

# # # Fake user-agents to simulate browsers
# # user_agents = [
# #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
# #     "Mozilla/5.0 (Linux; Android 11)",
# #     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
# #     "curl/7.68.0",
# #     "Python-urllib/3.9"
# # ]

# # # Pages the bot will hit
# # pages = ["/", "/products", "/cart", "/signup"]

# # # Function to simulate a bot
# # def simulate_bot(bot_id):
# #     for i in range(20):  # You can increase this for more visits
# #         page = random.choice(pages)
# #         agent = random.choice(user_agents)

# #         headers = {
# #             "User-Agent": agent
# #         }

# #         try:
# #             response = requests.get(BASE_URL + page, headers=headers)
# #             print(f"Bot {bot_id} [{i+1}] visited {page} with User-Agent: {agent} - Status: {response.status_code}")
# #         except Exception as e:
# #             print(f"Error visiting {page} with Bot {bot_id}: {e}")

# #         time.sleep(random.uniform(0.5, 2))  # Sleep to mimic human-ish delays

# # # Simulate multiple bots
# # def simulate_multiple_bots(num_bots):
# #     threads = []
# #     for bot_id in range(1, num_bots + 1):
# #         thread = threading.Thread(target=simulate_bot, args=(bot_id,))
# #         threads.append(thread)
# #         thread.start()

# #     for thread in threads:
# #         thread.join()

# # # Simulate 5 bots (you can increase the number)
# # simulate_multiple_bots(5)


# import requests
# import random
# import time

# # Base URL of your Flask server
# BASE_URL = "http://127.0.0.1:5000"

# # Fake user-agents to simulate browsers
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#     "Mozilla/5.0 (Linux; Android 11)",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
#     "curl/7.68.0",
#     "Python-urllib/3.9"
# ]

# # Pages the bot will hit
# pages = ["/", "/products", "/cart", "/signup", "/login", "/comment", "/price", "/check_user"]

# # Simulate multiple bot visits
# for bot_id in range(5):  # Create 5 bots for more traffic
#     for i in range(20):  # Each bot visits 20 pages
#         page = random.choice(pages)
#         agent = random.choice(user_agents)

#         headers = {
#             "User-Agent": agent
#         }

#         try:
#             response = requests.get(BASE_URL + page, headers=headers)
#             print(f"[Bot {bot_id+1}][{i+1}] Bot visited {page} with User-Agent: {agent} - Status: {response.status_code}")
#         except Exception as e:
#             print(f"Error visiting {page}: {e}")

#         time.sleep(random.uniform(0.5, 2))  # Sleep to mimic human-ish delays
