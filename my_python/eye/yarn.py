import psutil
import time

# Define the time range in seconds
interval = 300  # 5 minutes

# Get the current network usage
start_bytes_sent, start_bytes_recv = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv

# Wait for the specified time interval
time.sleep(interval)

# Calculate the network usage during the time interval
end_bytes_sent, end_bytes_recv = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv
bytes_sent = end_bytes_sent - start_bytes_sent
bytes_recv = end_bytes_recv - start_bytes_recv

# Print the network usage in bytes and in human-readable format
print("Bytes sent: ", bytes_sent)
print("Bytes received: ", bytes_recv)
print("Data sent: ", psutil._common.bytes2human(bytes_sent))
print("Data received: ", psutil._common.bytes2human(bytes_recv))