def deployment_target(service, environment="staging"):
    return f"{service} -> {environment}"


default_target = deployment_target("web-api")
production_target = deployment_target("worker", "production")
development_target = deployment_target(
    environment="development",
    service="cache",
)

print(default_target)
print(production_target)
print(development_target)