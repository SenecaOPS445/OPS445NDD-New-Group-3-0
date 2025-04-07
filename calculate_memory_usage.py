def calculate_memory_usage():
    """
    Calculate memory usage as a percentage.
                    
    The usage is determined by subtracting available memory from total memory."
    """
    memory = snapshot_memory()
    if "MemTotal" in memory and "MemAvailable" in memory:
        total = memory["MemTotal"]
        available = memory["MemAvailable"]
        used = total - available
        usage = used / total * 100
        return usage
    return 0
