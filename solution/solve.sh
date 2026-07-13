#!/bin/bash
# A simple script to parse the logs and output the required report

# Create the output directory
mkdir -p output

# Count how many times "Critical Failures" appears in the system.log
ERROR_COUNT=$(grep -c "Critical Failures" system.log)

# Write exactly what the instruction.md asked for into the report.log
echo "Critical Failures: $ERROR_COUNT" > output/report.log
