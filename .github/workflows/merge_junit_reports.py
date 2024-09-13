import os
from junitparser import JUnitXml

# Directory where test reports are stored
test_report_dir = "parallel-backend-tests/core/build/test-results/test"
merged_report = JUnitXml()

# Loop through all XML files and merge them
for root, dirs, files in os.walk(test_report_dir):
    for file in files:
        if file.endswith(".xml"):
            report_path = os.path.join(root, file)
            xml = JUnitXml.fromfile(report_path)
            merged_report += xml

# Save the merged report
merged_report.write("unified-test-results/unified-report.xml")
