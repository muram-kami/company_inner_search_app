import requests

def check_package_version(pkg_line):
    if "==" not in pkg_line:
        return None  # バージョン指定なしは無視
    pkg, ver = pkg_line.strip().split("==")
    url = f"https://pypi.org/pypi/{pkg}/json"
    resp = requests.get(url)
    if resp.status_code != 200:
        return f"⚠️ {pkg} is not found on PyPI"
    data = resp.json()
    versions = data["releases"].keys()
    if ver not in versions:
        latest = sorted(versions, reverse=True)[0]
        return f"❌ {pkg}=={ver} not found (latest: {latest})"
    return None  # OK

with open("requirements_windows.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    result = check_package_version(line)
    if result:
        print(result)
