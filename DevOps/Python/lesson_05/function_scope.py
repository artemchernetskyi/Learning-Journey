def build_status(service):
    status = "READY"
    message = f"{service}: {status}"
    return message


result = build_status("web-api")

print(result)
# print(status)