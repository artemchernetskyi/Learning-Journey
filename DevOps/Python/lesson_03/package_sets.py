installed_packages = {"nginx", "docker", "curl", "nginx"}

print(installed_packages)
print(type(installed_packages))
print(f"Package count: {len(installed_packages)}")

docker_installed = "docker" in installed_packages
print(f"Docker installed: {docker_installed}")

required_packages = {"docker", "curl", "git", "python3"}

missing_packages = required_packages - installed_packages
extra_packages = installed_packages - required_packages
common_packages = installed_packages & required_packages
all_packages = installed_packages | required_packages

print(f"Required packages: {required_packages}")
print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")
print(f"All unique packages: {all_packages}")

installed_packages.add("git")
installed_packages.discard("nginx")

updated_missing_packages = required_packages - installed_packages

print(f"Updated installed packages: {installed_packages}")
print(f"Original missing packages: {missing_packages}")
print(f"Updated missing packages: {updated_missing_packages}")