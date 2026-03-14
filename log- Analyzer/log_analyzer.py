from collections import Counter

# Open the log file
with open("server_log.txt", "r") as file:
    lines = file.readlines()

ips = []

# Extract IP addresses
for line in lines:
    ip = line.split()[0]
    ips.append(ip)

# Count how many times each IP appears
count = Counter(ips)

print("Suspicious IP Activity:")

# Show IPs that appear multiple times
for ip, number in count.items():
    if number > 1:
        print(ip, "appeared", number, "times")