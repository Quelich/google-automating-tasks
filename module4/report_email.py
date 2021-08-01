#!/usr/bin/env python3
import os
import datetime
import reports
import emails


fruit_names = []
fruit_weights = []


for file in os.listdir("./supplier-data/descriptions"):
    with open("./supplier-data/descriptions/" + file) as f:
        for inline in f:
            line = inline.strip()
            if len(line) <= 10 and len(line) > 0 and "lb"not in line:
                fruit_name = "name: " + line
                fruit_names.append(fruit_name)
            if "lbs" in line:
                fruit_weight = "weight: " + line
                fruit_weights.append(fruit_weight)

additional_info = ""
for name, weight in zip(fruit_names, fruit_weights):
    additional_info += name + '<br/>' + weight + '<br/>' + '<br/>'

get_today = "Processed Update on " + datetime.date.today().strftime("%B  %d, %Y")
if __name__ == "__main__":
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    my_post = emails.generate_email(
        "automation@example.com", "<username>@example.com", subject, body, "/tmp/processed.pdf")
    reports.generate_report("/tmp/processed.pdf", get_today, additional_info)
    emails.send_email(my_post)
