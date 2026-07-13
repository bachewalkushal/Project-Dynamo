# Task: Dynamo Log Reporting

Your goal is to parse the system log files located in the root directory and compile a summary report.

## Requirements
1. Analyze all raw logs to extract system errors.
2. Generate a final summary text file and save it exactly to the path: `output/report.log`.
3. The generated file must include a summary string that displays the exact calculation of critical system events in the specific format: `Critical Failures: X` (where X is the integer total).

## Success Criteria
* The file `output/report.log` must exist upon task completion.
* The file `output/report.log` must contain the string matching the exact error count found during parsing.
