# Winter 2025 Assignment 2
#mhamilton-edwards (report_generator.py)

# Overview:
I was responsible for creating the report generation for our script. The function, generate_reports(cpu_usage, mem_usage, output_dir), takes the CPuU memory usage metrics and puts the output into 2 files
system_reports.txt which is a report that shows the rounded CPU  and memory usage percentages and the 2nd file visual_report.txt shows cpu and memory yusage in a visual format

# A key feature
if not os.path.exists(output_dir):
 os.mkdir(output_dir)
This is a key feature because if the directory doesnt exsist for the files then the script makes the directory.
