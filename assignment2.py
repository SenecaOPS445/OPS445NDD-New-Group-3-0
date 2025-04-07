def snapshot_cpu():
    """

    Take a snapshot of CPU metrics by reading /proc/stat.

    The file /proc/stat contains overall CPU statistics.
    We read the first line and convert the values to integers.
    """
    file = open("/proc/stat", "r")
    line = file.readline().strip()    # Read the first line (starts with "cpu")
    parts = line.split()              # Split the line into parts
    file.close()

    # Convert each value (ignoring the 'cpu' label)
    cpu_times = []
    for value in parts[1:]:
        cpu_times.append(int(value))
    return cpu_times

def calculate_cpu_usage(interval):
    """
    Calculate CPU usage by comparing two snapshots taken with a delay.        

    Steps:
        1. Take the first CPU snapshot.
        2. Wait for a specified interval.
        3. Take the second snapshot.
        4. Calculate the change in idle time and total time.
        5. Compute the CPU usage percentage.
    """

    # Take the first snapshot
    cpu_start = snapshot_cpu()
    total_start = sum(cpu_start)
    idle_start = cpu_start[3]  # Idle time is usually the 4th value

    # Wait for the given interval
    time.sleep(interval)

    # Take the second snapshot
    cpu_end = snapshot_cpu()
    total_end = sum(cpu_end)
    idle_end = cpu_end[3]

    # Compute the differences
    total_diff = total_end - total_start
    idle_diff = idle_end - idle_start

    # Calculate CPU usage: percentage of time not idle
    if total_diff == 0:
        return 0
    usage = (total_diff - idle_diff) / total_diff * 100
    return usage
