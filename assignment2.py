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