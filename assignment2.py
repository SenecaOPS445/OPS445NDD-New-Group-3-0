#!/usr/bin/env python3

import argparse
import os
import time

def parse_arguments():
    """
        Parse command-line arguments.

        Options:
        --interval: Number of seconds to wait between two CPU snapshots.
        --output: Directory where the report files will be saved."
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=int, default=2)  # Seconds to wait between CPU snapshots
    parser.add_argument("--output", default="Reports")      # Directory to save the report files
    return parser.parse_args()

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

def create_visualization(percentage):
    """
    Create a simple text-based visualization.                

    One '#' character represents 2% of usage.

    """

    num_hashes = int(percentage / 2)
    return '#' * num_hashes

def save_text_report(content, filepath):
    """
    Save the provided text content into a file.
    """

    file = open(filepath, "w")
    file.write(content)
    file.close()

def generate_reports(cpu_usage, mem_usage, output_dir):
    """
    Generate system performance reports and visualizations.

    Two files are created:
        - system_report.txt: Contains numerical data.
        - visual_report.txt: Contains text-based visualizations.
    """

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Create the detailed report
    report = "System Performance Report:\n\n"
    report += "CPU Usage: " + str(round(cpu_usage, 2)) + "%\n"
    report += "Memory Usage: " + str(round(mem_usage, 2)) + "%"

    # Create visualizations
    cpu_visual = create_visualization(cpu_usage)
    mem_visual = create_visualization(mem_usage)
    visualization = "CPU Usage Visualization:\n" + cpu_visual + "\n\n"
    visualization += "Memory Usage Visualization:\n" + mem_visual

    # Save the report and visualization to text files
    save_text_report(report, output_dir + "/system_report.txt")
    save_text_report(visualization, output_dir + "/visual_report.txt")

if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()

    # Calculate CPU and memory usage
    cpu_usage = calculate_cpu_usage(args.interval)
    mem_usage = calculate_memory_usage()

    # Generate the reports and save them in the specified directory
    generate_reports(cpu_usage, mem_usage, args.output)

    # Notify the user where the reports are saved
    print("Reports generated in directory:", args.output)
