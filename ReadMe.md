# Winter 2025 Assignment 2

1. How will your program gather required input?

The program gathers input by reading system files on a Linux machine. It reads from /proc/stat to obtain CPU metrics and from /proc/meminfo to obtain memory statistics. Additionally, the program uses command-line arguments (via the argparse module) so that a user can specify parameters such as the time interval between snapshots and the output directory for the reports.
 
2. How will your program accomplish its requirements?

The program accomplishes its requirements by performing the following steps:
It captures two snapshots of CPU metrics at a defined time interval, calculates the differences, and computes the percentage of CPU usage.
It reads the memory information, calculates the percentage of used memory, and then generates two types of outputs.
It creates a detailed textual report showing numerical data for CPU and memory usage.
It also generates a simple text-based visualization where each '#' symbol represents 2% usage.
Finally, the output files are saved in a specified directory, making the data accessible for review.
 
3. How will output be presented?

The output will be presented in two text files:
system_report.txt: This file contains a detailed report with the exact percentage of CPU and memory usage.
visual_report.txt: This file provides a simple visual representation of the usage data, using hash marks (#) to represent the usage levels. Both files are stored in a directory specified by the user, and a message is printed to the console to indicate where the reports are saved.
 
4. What arguments or options will be included?

The program includes two command-line options:
--interval: This argument allows the user to define the number of seconds the program should wait between taking the first and second snapshots of CPU metrics.
--output: This argument specifies the directory where the generated reports (both the numerical report and the visualization) will be saved. These options provide flexibility for the user to adjust the monitoring period and choose a preferred location for the output.
 
5. What aspects of development do you think will present the most challenge?

The most challenging aspects of development might include:
Accurate Calculation of Metrics: Ensuring the CPU usage calculation is accurate, given that system load can vary rapidly.
Handling File Operations: Properly reading from system files like /proc/stat and /proc/meminfo without errors and ensuring that these operations work reliably across different Linux environments.
Error Handling: Managing potential errors, such as file read errors or invalid command-line inputs, in a simple but robust manner.
Synchronization of Snapshots: Timing the snapshots precisely using time.sleep so that the calculations reflect real-time usage accurately.
 
6. When do you estimate you will complete each part of the task? Provide a rough timeline for planning, coding, testing, and documenting your assignment.

A possible timeline for the project could be:
Planning (1–2 days):
Meet with group members to define the project scope, assign roles, and review the requirements.
Coding (3–4 days):
Each member works on their assigned section.
Testing (2 days):
Test the script on a Linux machine to ensure the CPU and memory usage calculations are correct, and that reports are generated in the correct format.
Documentation (1 day):
Prepare the README file, document the code, and provide clear instructions on how to run the program.