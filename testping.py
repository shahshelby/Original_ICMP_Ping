import os
import time
import threading

# Dictionary of floors and their IPs
servers = {
    'Floor 1': ['172.16.113.10'],
    'Floor 3': ['172.16.113.30', '172.16.113.31', '172.16.113.32', '172.16.113.33',
                '172.16.113.34', '172.16.113.35', '172.16.113.36'],
    'Floor 4': ['172.16.113.40', '172.16.113.41', '172.16.113.42'],
    'Floor 5': ['172.16.113.50', '172.16.113.51', '172.16.113.52', '172.16.113.53',
                '172.16.113.54', '172.16.113.55', '172.16.113.56', '172.16.113.57', '172.16.113.58'],
    'Floor 6': ['172.16.113.60', '172.16.113.61'],
    'Floor 7': ['172.16.113.70', '172.16.113.71', '172.16.113.72', '172.16.113.73',
                '172.16.113.74', '172.16.113.75', '172.16.113.76'],
    'Floor 8': ['172.16.113.80', '172.16.113.81', '172.16.113.82', '172.16.113.83',
                '172.16.113.84', '172.16.113.85'],
    'Floor 9': ['172.16.113.90', '172.16.113.91'],
    'Floor 10': ['192.168.137.100']
}

# Dictionary to hold results for each switch
results = {}


# Function to check the ping status of an IP and update the result in the dictionary
def check_ping(ip, sw_name):
    success = os.system(f'ping -n 1 {ip} > nul') == 0  # True if ping successful
    status = 'UP!' if success else 'DOWN!'  # Status message
    with lock:
        results[sw_name] = status  # Update the results dictionary with the switch status


# Simulate sending a message to the Line API (placeholder)
def send_line_message(message):
    print(f"[MESSAGE] {message}")


# Lock for thread synchronization
lock = threading.Lock()

# Infinite loop to keep pinging the IPs on each floor
while True:
    print('PING REQUESTS STARTING...')
    results.clear()  # Clear results for each round

    # Go through each floor and its switches
    for floor_name, sws in servers.items():
        threads = []  # List to hold threads for this round
        status_lines = []  # Store each switch's status line

        # Notify the start of pinging for this floor
        send_line_message(f"Starting ping checks for {floor_name}...")

        # Create and start a thread for each switch on the floor
        for i, ip in enumerate(sws):
            sw_name = f'SW{i + 1}'  # SW1, SW2, etc.
            thread = threading.Thread(target=check_ping, args=(ip, sw_name))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Now accumulate results in order from SW1 to SWn (based on the i order)
        for i, ip in enumerate(sws):
            sw_name = f'SW{i + 1}'
            status = results.get(sw_name, 'Unknown')  # Get the ping result from the dictionary
            status_lines.append(f"• {sw_name} ({ip}): {status}")  # Format with bullet point and IP

        # Send the results for this floor
        send_line_message(f"{floor_name} Status:\n" + "\n".join(status_lines))

    # Wait for 1 seconds after completing all floors, then start the next round
    print("END OF ROUND...")
    time.sleep(1)
