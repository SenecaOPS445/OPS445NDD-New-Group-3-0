def snapshot_memory():
    """

    Read memory usage information from /proc/meminfo.

    This function creates a dictionary containing memory info values,
    such as total and available memory.
    """

    meminfo = {}
    file = open("/proc/meminfo", "r")
    for line in file:
        parts = line.split(":")
        if len(parts) >= 2:
            key = parts[0].strip()               # e.g., "MemTotal", "MemAvailable"
            value = parts[1].strip().split()[0]  # Get the first number
            meminfo[key] = int(value)
    file.close()
    return meminfo