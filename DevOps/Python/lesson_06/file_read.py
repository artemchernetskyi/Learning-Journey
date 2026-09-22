from pathlib import Path


report_path = Path("DevOps/Python/lesson_06/deployment_report.txt")

if report_path.exists():
    report_content = report_path.read_text(encoding="utf-8")
    report_lines = report_content.splitlines()

    print(f"Services in report: {len(report_lines)}")

    for line in report_lines:
        print(f"Read line: {line}")
    print("Deployment report:")
    print(report_content)
else:
    print(f"Report not found: {report_path}")