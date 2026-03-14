import socket

# Target machine to scan
target = "127.0.0.1"

# List of ports to test
ports = [20,21,22,23,25,53,80,110,443,3306]

print("Checking ports on", target)
print()

# Loop through each port
for port in ports:

    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout after 1 second
    s.settimeout(1)

    # Attempt connection
    result = s.connect_ex((target, port))

    # If connection succeeds
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

    # Close connection
    s.close()