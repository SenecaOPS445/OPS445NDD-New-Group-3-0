def create_visualization(percentage):
    """
    Create a simple text-based visualization.

    One '#' character represents 2% of usage.

    """

    num_hashes = int(percentage / 2) # this calculates how many # symbols to use based on the %
    return '#' * num_hashes # this will return a string with that many # characters

def save_text_report(content, filepath):
    """
    Save the provided text content into a file.
    """

    file = open(filepath, "w") # This opens the file in write mode , it also creates it if it doesnt alrady exist
    file.write(content) # writes the content string into the file
    file.close() # this will close the file and save all changes

def generate_reports(cpu_usage, mem_usage, output_dir):
    """
    Generate system performance reports and visualizations.

    Two files are created:
        - system_report.txt: Contains numerical data.
        - visual_report.txt: Contains text-based visualizations.
    """

    # Ensure the output directory exists, if it doesnt then the directory is created.
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Create the detailed report with  CPU and memory usage information.
    report = "System Performance Report:\n\n"
    report += "CPU Usage: " + str(round(cpu_usage, 2)) + "%\n"  # This adds the rounded CPU usage data.
    report += "Memory Usage: " + str(round(mem_usage, 2)) + "%"  # This adds the  rounded memory usage data.

    # Create visualizations(Generate text-based visualizations of CPU and memory usage).
    cpu_visual = create_visualization(cpu_usage)
    mem_visual = create_visualization(mem_usage)

    # Combine the visualizations into a single string with appropriate formatting.
    visualization = "CPU Usage Visualization:\n" + cpu_visual + "\n\n"
    visualization += "Memory Usage Visualization:\n" + mem_visual

    # Save the report and visualization to text files.
    save_text_report(report, output_dir + "/system_report.txt") #the report is made in the output directory with the name system_report.txt
    save_text_report(visualization, output_dir + "/visual_report.txt") #the visualzation is make in the output directory with the name  visual_report.txt

if __name__ == "__main__":

# Generate the reports and save them in the specified directory
    generate_reports(cpu_usage, mem_usage, args.output)
