# Do not forget to make necesary changes
#! /usr/bin/env python3
import os
import requests
import json
# List all .txt files under /data/feedback
dir = "/data/feedback/"
url = "http://<ip address>/feedback/"

# print(os.listdir(dir))

for file in os.listdir(dir):
    content = ["title", "name", "date", "feedback"]
    param = {}
    with open(dir + "/" + file, "r") as txt:
        x = 0
        for line in txt:
            param[content[x]] = line.rstrip('\n')
            x += 1
    response = requests.post(url, json=param)
    response.raise_for_status()
