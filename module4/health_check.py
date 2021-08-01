
#!/usr/bin/env python3
import os
import socket
import shutil
import psutil
import emails


# Report an error if CPU usage is over 80%
if psutil.cpu_percent(1) > 80:
    warning = emails.generate_error_report(
        "automation@example.com", "<username>@example.com", "Error - CPU usage is over 80%", "Unable to complete the task :(")
    emails.send_email(warning)

# Report an error if 
disk_usage = shutil.disk_usage("/")
usage_percentage = disk_usage.free/disk_usage.total * 100
if usage_percentage < 20:
    warning = emails.generate_error_report(
        "automation@example.com", "<username>@example.com", "Error - Available disk space is lower than 20%", "Unable to complete the task :(")
    emails.send_email(warning)
    
# Report an error if available memory is less than 500MB
if psutil.virtual_memory().available < 1 * 500 * 1024 * 1024:
    warning = emails.generate_error_report(
        "automation@example.com", "<username>@example.com", "Error - Available memory is less than 500MB", "Unable to complete the task :(")
    emails.send_email(warning)

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
if socket.gethostbyname('localhost') != '127.0.0.1':
    warning = emails.generate_error_report(
        "automation@example.com", "<username>@example.com", "Error - The hostname 'localhost' cannot be resolved to '127.0.0.1'", "Unable to complete the task :(")
    emails.send_email(warning)
