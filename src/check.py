#!/bin/python

import requests
import time

filter = ["API Requests", "Codespaces", "GitHub Packages"]
url = "https://www.githubstatus.com/api/v2/summary.json"

while True:
  response = requests.get(url)
  data = response.json()
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  components = data["components"]
  for component in components:
    if component["name"] in filter:
      print(current_time, component["name"], component["status"])
  print("---------------------------------------------")
  time.sleep(10)
