import requests
import time
import os
import signal

def shutdown(signum, frame):
  # Perform any necessary cleanup tasks here

  # Stop the container
  exit()

# Register the shutdown function to be called when the SIGINT signal is received
signal.signal(signal.SIGINT, shutdown)

# URL to check
url = "https://www.nuitdelinfo.com/inscription/defis/liste"

# Webhook URL
webhook_url = os.environ.get("DISCORD_WEBHOOK")
team_name = os.environ.get("TEAM_NAME")

if webhook_url is None:
  print("No webhook URL provided, exiting...")
  exit()

if team_name is None:
  print("No team name provided, exiting...")
  exit()

# Counter for the number of times team_name appears
team_name_count = 0
previous_team_name_count = -1

while True:
  # Send a GET request to the URL
  response = requests.get(url)

  # Get the content of the response
  content = response.text

  previous_content = ""

  # Check if the content has changed
  if content != previous_content:
    # Increment the counter for each occurrence of "team_name" in the content
    team_name_count = content.count(team_name)

    if previous_team_name_count != team_name_count:
      # Create a Discord webhook message
      message_content = f"{team_name} has appeared {team_name_count} times in {url}"
      print(message_content)
      message = {
        "content": message_content
      }

      response = requests.post(webhook_url, json=message)

    previous_content = content
    previous_team_name_count = team_name_count

  # Sleep for one hour
  time.sleep(3600)
