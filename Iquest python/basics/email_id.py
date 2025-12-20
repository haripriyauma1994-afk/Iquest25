'''
Created on 12-Dec-2025

@author: ABC
'''
import requests
import random
import string
import time

BASE_URL = "https://api.mail.tm"

def random_string(n=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

emails_created = []

for i in range(200):
    try:
        # Step 1: Get domain list
        domains = requests.get(f"{BASE_URL}/domains").json()
        domain = domains["hydra:member"][0]["domain"]

        # Generate email + password
        email = f"{random_string(8)}@{domain}"
        password = random_string(12)

        # Step 2: Create account
        data = {"address": email, "password": password}
        create_res = requests.post(f"{BASE_URL}/accounts", json=data)

        if create_res.status_code == 201:
            print(f"[{i+1}] Created: {email} | {password}")
            emails_created.append(f"{email},{password}")
        else:
            print(f"[{i+1}] Failed: {create_res.text}")

        # Small delay to avoid rate limit
        time.sleep(1)

    except Exception as e:
        print(f"Error at {i+1}: {e}")
        time.sleep(2)

# Save to file
with open("mailtm_accounts.csv", "w") as f:
    f.write("email,password\n")
    for item in emails_created:
        f.write(item + "\n")

print("\nFinished creating accounts!")
print("Saved to mailtm_accounts.csv")
