import os
from junitparser import JUnitXml, TestSuite, TestCase

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

            # Append each suite from the xml to the merged_report
            for suite in xml:
                # Create a new TestSuite object to preserve the file attribute
                new_suite = TestSuite(name=suite.name,
                                      tests=suite.tests,
                                      skipped=suite.skipped,
                                      failures=suite.failures,
                                      errors=suite.errors,
                                      timestamp=suite.timestamp,
                                      hostname=suite.hostname,
                                      time=suite.time)

                # Preserve the file attribute
                if hasattr(suite, 'file'):
                    new_suite.file = suite.file

                # Loop through each testcase to preserve the file attribute
                for case in suite:
                    new_case = TestCase(name=case.name,
                                        classname=case.classname,
                                        time=case.time)

                    # Preserve the file attribute in the testcase
                    if hasattr(case, 'file'):
                        new_case.file = case.file

                    # Add the testcase to the new suite
                    new_suite.append(new_case)

                # Add the new suite to the merged report
                merged_report.suites.append(new_suite)

# Save the merged report
os.makedirs("unified-test-results", exist_ok=True)
merged_report.write("unified-test-results/unified-report.xml")
print("Merged report saved to unified-test-results/unified-report.xml")