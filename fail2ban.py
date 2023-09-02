import re
import time
from datetime import datetime, timedelta

def print_table_header():
    print("===============================================")
    print("| Port |       IP       |      Date & Time    |")
    print("===============================================")

# Clear terminal
print("\033c", end="")

# Extract Fail2ban Version, banTime, and logfile location
with open('/var/log/fail2ban.log', 'r') as f:
    lines = f.readlines()
    for line in lines[:20]:
        version_match = re.search(r'Starting Fail2ban v([\d.]+)', line)
        ban_time_match = re.search(r'banTime: (\d+)', line)
        log_file_match = re.search(r'Added logfile: \'(.*?)\'', line)

        if version_match:
            print(f"Fail2ban Version: {version_match.group(1)}")
        if ban_time_match:
            print(f"banTime: {ban_time_match.group(1)}s")
        if log_file_match:
            print(f"logfile location: {log_file_match.group(1)}")
            #print_table_header()
            print("\nYesterday")
            print_table_header()

# Pause for 2 seconds
time.sleep(2)

# Calculate yesterday's and today's date
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
today_str = datetime.now().strftime('%Y-%m-%d')

# Define regular expression pattern for log entries
pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).*\[(\w+)\] (Ban|Unban) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# Read log file for log entries and print for 'Yesterday' and 'Today'
with open('/var/log/fail2ban.log', 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            log_time_str = match.group(1)
            log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M:%S,%f')
            log_date_str = log_time.strftime('%Y-%m-%d')

            # Check if the log entry is from yesterday
            if log_date_str == yesterday_str:
                jail = match.group(2)
                ip = match.group(4)
                print(f"| {jail:<4} | {ip:<15} | {log_time.strftime('%Y-%m-%d %H:%M:%S')} |")

print("\nToday")
print_table_header()

with open('/var/log/fail2ban.log', 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            log_time_str = match.group(1)
            log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M:%S,%f')
            log_date_str = log_time.strftime('%Y-%m-%d')

            # Check if the log entry is from today
            if log_date_str == today_str:
                jail = match.group(2)
                ip = match.group(4)
                print(f"| {jail:<4} | {ip:<15} | {log_time.strftime('%Y-%m-%d %H:%M:%S')} |")

print("\nNow")
print_table_header()

try:
    while True:
        with open('/var/log/fail2ban.log', 'r') as f:
            f.seek(0, 2)  # go to the end of file
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)  # Sleep for a second and check again
                    continue
                match = pattern.search(line)
                if match:
                    log_time_str = match.group(1)
                    log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M:%S,%f')
                    jail = match.group(2)
                    ip = match.group(4)
                    print(f"| {jail:<4} | {ip:<15} | {log_time.strftime('%Y-%m-%d %H:%M:%S')} |")
except KeyboardInterrupt:
    print("\nExiting...")
