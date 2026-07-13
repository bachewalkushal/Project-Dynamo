import os
import pytest

def test_artifact_existence():
    """CRITERION 1: The file 'output/report.log' must exist upon task completion."""
    artifact_path = "output/report.log"
    assert os.path.exists(artifact_path), "The file 'output/report.log' was not created."

def test_error_count_accuracy():
    """CRITERION 2: The file 'output/report.log' must contain the string matching the exact error count found during parsing."""
    artifact_path = "output/report.log"
    assert os.path.exists(artifact_path), "The file 'output/report.log' must exist to check contents."
    
    with open(artifact_path, "r") as f:
        content = f.read()
        
    # Verifies that the report explicitly tracks the exact expected total of 4 critical failures
    assert "Critical Failures: 4" in content, "The report does not accurately count or state the critical failures (Expected: 4)."
