import os
from junitparser import JUnitXml

# Directory where test reports are stored
test_report_dir = "./downloaded-test-results/"
merged_report = JUnitXml()

# Loop through all XML files and merge them
for root, dirs, files in os.walk(test_report_dir):
    for file in files:
        if file.endswith(".xml"):
            report_path = os.path.join(root, file)
            print(f"Found XML file: {report_path}")  # Debug output
            xml = JUnitXml.fromfile(report_path)

            # Add each suite from the xml to the merged_report
            for suite in xml:
                # Check for custom file attribute in each testcase
                for case in suite:
                    # Optionally add the 'file' attribute as a property
                    case.properties['file'] = case.properties.get('file', '')  # Preserve the file attribute if it exists

                # Append the suite to the merged report
                merged_report.add(suite)

# Save the merged report
os.makedirs("unified-test-results", exist_ok=True)
merged_report.write("unified-test-results/unified-report.xml")
print("Merged report saved to unified-test-results/unified-report.xml")