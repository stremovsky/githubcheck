#!/bin/python

import os
import time
import requests

from slack_sdk import WebClient

def report_poblem(component, status):
  slack_token = os.environ["SLACK_API_TOKEN"]
  if slack_token is None:
    return
  client = WebClient(token=slack_token)
  try:
    response = client.chat_postMessage(
      channel="Production",
      text="Component: " + component+ " status: "+status
    )
  except Exception:
    pass

def check_status():
  filter = ["API Requests", "Codespaces", "GitHub Packages"]
  url = "https://www.githubstatus.com/api/v2/summary.json"
  response = requests.get(url)
  data = response.json()
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  components = data["components"]
  for component in components:
    if component["name"] in filter:
      print(current_time, component["name"], component["status"])
      if component["status"] != "operational":
        report_poblem(component["name"], component["status"])

if __name__ == '__main__':
  while True:
    check_status()
    print("---------------------------------------------")
    time.sleep(10)
