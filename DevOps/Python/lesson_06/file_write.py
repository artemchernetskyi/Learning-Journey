from pathlib import Path


report_path = Path("DevOps/Python/lesson_06/deployment_report.txt")

report_content = """web-api: READY
worker: WARNING
database: CRITICAL
"""

report_path.write_text(report_content, encoding="utf-8")

print(f"Report written to: {report_path}")
print(f"File exists: {report_path.exists()}")