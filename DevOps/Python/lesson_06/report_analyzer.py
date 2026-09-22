from pathlib import Path


script_directory = Path(__file__).resolve().parent
report_path = script_directory / "deployment_report.txt"

report_lines = report_path.read_text(encoding="utf-8").splitlines()
ready_services = []
problem_services = []

for line in report_lines:
    service, status = line.split(": ", maxsplit=1)
    print(f"Service: {service} | Status: {status}")

    if status == "READY":
        ready_services.append(service)
    else:
        problem_services.append(service)
ready_names = ", ".join(ready_services)
problem_names = ", ".join(problem_services)

print(f"Ready services ({len(ready_services)}): {ready_names}")
print(f"Problem services ({len(problem_services)}): {problem_names}")

reports_directory = script_directory / "reports"
summary_path = reports_directory / "service_summary.txt"

reports_directory.mkdir(parents=True, exist_ok=True)

summary_lines = [
    f"Ready services ({len(ready_services)}): {ready_names}",
    f"Problem services ({len(problem_services)}): {problem_names}",
]

summary_content = "\n".join(summary_lines) + "\n"
summary_path.write_text(summary_content, encoding="utf-8")

print(f"Summary written to: {summary_path}")