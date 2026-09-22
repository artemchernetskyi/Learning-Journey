from pathlib import Path


script_directory = Path(__file__).resolve().parent
report_path = script_directory / "deployment_report.txt"

print(f"Script directory: {script_directory}")
print(f"Report path: {report_path}")

if report_path.exists():
    report_content = report_path.read_text(encoding="utf-8")

    print("Deployment report:")
    print(report_content)
else:
    print(f"Report not found: {report_path}")