def snapshot_cpu():

    file = open("/proc/stat", "r")
    line = file.readline().strip()    
    parts = line.split()              
    file.close()

    cpu_times = []
    for value in parts[1:]:
        cpu_times.append(int(value))
    return cpu_times