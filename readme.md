# Server Status Monitor

A Python script for pinging IP addresses across multiple floors and sending status updates.

## Features

ICMP Ping: Pings IP addresses and reports if a server is UP! or DOWN!.
Multi-threading: Concurrent pings for faster performance.

The script pings servers on each floor using threads.
Results are formatted and sent via send_line_message()

## Base Implementation

```python
# Function to check the ping status of an IP and update the result in the dictionary
def check_ping(ip, sw_name):
    success = os.system(f'ping -n 1 {ip} > nul') == 0  # True if ping successful
    status = 'UP!' if success else 'DOWN!'  # Status message
    with lock:
        results[sw_name] = status  # Update the results dictionary with the switch status
```

