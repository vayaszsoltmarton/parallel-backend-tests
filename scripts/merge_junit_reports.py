import os
from junitparser import JUnitXml

# Directory where test reports are stored
test_report_dir = "/home/runner/work/parallel-backend-tests/parallel-backend-tests/downloaded-test-results"
merged_report = JUnitXml()

# Loop through all XML files and merge them
for root, dirs, files in os.walk(test_report_dir):
    for file in files:
        if file.endswith(".xml"):
            report_path = os.path.join(root, file)
            print(f"Found XML file: {report_path}")  # Debug output
            xml = JUnitXml.fromfile(report_path)
            merged_report += xml

# Save the merged report
os.makedirs("unified-test-results", exist_ok=True)
merged_report.write("unified-test-results/unified-report.xml")
print("Merged report saved to unified-test-results/unified-report.xml") 
