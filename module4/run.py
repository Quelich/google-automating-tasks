#! /usr/bin/env python3
import os
import requests



desc_path = "./supplier-data/descriptions/"
url = "http://<external_ip_address>/fruits/"

content = ["name", "weight", "description", "image_name"]
for file in os.listdir("./supplier-data/descriptions/"):
    fruits = {}
    with open(desc_path + "/" + file) as desc_file:
        index = 0
        for line in desc_file:
            if not "lbs" in line:
                fruits[content[index]] = line
            else:
                weight_line = line.split()
                weight = int(weight_line[0])
                fruits["weight"] = weight
            index += 1
        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        for img_file in os.listdir("./supplier-data/images/"):
            if img_file == name:
                fruits["image_name"] = name
        response = requests.post(url, json=fruits)
