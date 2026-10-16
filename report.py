import json
from datetime import datetime, timezone
from pathlib import Path

from config import (
REPORT_CATEGORIES,
MAX_DESCRIPTION_LENGTH,
MAX_URL_LENGTH,
DATA_DIRECTORY,
)

def collect_report():
"""Collect information for a report."""

print("\n=== CyberRUHAN-FB Report Assistant ===")

for number, category in enumerate(REPORT_CATEGORIES, start=1):
    print(f"{number}. {category}")

try:
    choice = int(input("\nSelect report category: "))
    if not 1 <= choice <= len(REPORT_CATEGORIES):
        print("Invalid category selection.")
        return None
except ValueError:
    print("Please enter a valid number.")
    return None

account_url = input("Facebook profile or post URL: ").strip()
if len(account_url) > MAX_URL_LENGTH:
    print("The URL is too long.")
    return None

description = input("Describe the issue: ").strip()
if not description:
    print("A description is required.")
    return None

if len(description) > MAX_DESCRIPTION_LENGTH:
    print("The description is too long.")
    return None

evidence = input("Evidence notes (optional): ").strip()

return {
    "category": REPORT_CATEGORIES[choice - 1],
    "url": account_url,
    "description": description,
    "evidence_notes": evidence,
    "created_at": datetime.now(timezone.utc).isoformat(),
    "status": "Draft",
}

def save_report(report):
"""Save a report draft locally as JSON."""

if not report:
    return False

data_dir = Path(DATA_DIRECTORY)
data_dir.mkdir(parents=True, exist_ok=True)

report_file = data_dir / "reports.json"

if report_file.exists():
    try:
        with report_file.open("r", encoding="utf-8") as file:
            reports = json.load(file)

        if not isinstance(reports, list):
            reports = []
    except (json.JSONDecodeError, OSError):
        reports = []
else:
    reports = []

reports.append(report)

with report_file.open("w", encoding="utf-8") as file:
    json.dump(reports, file, indent=4, ensure_ascii=False)

print(f"\nReport draft saved to: {report_file}")
print("Review the details before submitting a report.")
return True

if name == "main":
draft = collect_report()

if draft:
    save_report(draft)
  import json
from datetime import datetime, timezone
from pathlib import Path

from config import (
REPORT_CATEGORIES,
MAX_DESCRIPTION_LENGTH,
MAX_URL_LENGTH,
DATA_DIRECTORY,
)

def collect_report():
"""Collect information for a report."""

print("\n=== CyberRUHAN-FB Report Assistant ===")

for number, category in enumerate(REPORT_CATEGORIES, start=1):
    print(f"{number}. {category}")

try:
    choice = int(input("\nSelect report category: "))
    if not 1 <= choice <= len(REPORT_CATEGORIES):
        print("Invalid category selection.")
        return None
except ValueError:
    print("Please enter a valid number.")
    return None

account_url = input("Facebook profile or post URL: ").strip()
if len(account_url) > MAX_URL_LENGTH:
    print("The URL is too long.")
    return None

description = input("Describe the issue: ").strip()
if not description:
    print("A description is required.")
    return None

if len(description) > MAX_DESCRIPTION_LENGTH:
    print("The description is too long.")
    return None

evidence = input("Evidence notes (optional): ").strip()

return {
    "category": REPORT_CATEGORIES[choice - 1],
    "url": account_url,
    "description": description,
    "evidence_notes": evidence,
    "created_at": datetime.now(timezone.utc).isoformat(),
    "status": "Draft",
}

def save_report(report):
"""Save a report draft locally as JSON."""

if not report:
    return False

data_dir = Path(DATA_DIRECTORY)
data_dir.mkdir(parents=True, exist_ok=True)

report_file = data_dir / "reports.json"

if report_file.exists():
    try:
        with report_file.open("r", encoding="utf-8") as file:
            reports = json.load(file)

        if not isinstance(reports, list):
            reports = []
    except (json.JSONDecodeError, OSError):
        reports = []
else:
    reports = []

reports.append(report)

with report_file.open("w", encoding="utf-8") as file:
    json.dump(reports, file, indent=4, ensure_ascii=False)

print(f"\nReport draft saved to: {report_file}")
print("Review the details before submitting a report.")
return True

if name == "main":
draft = collect_report()

if draft:
    save_report(draft)
  import json
from datetime import datetime, timezone
from pathlib import Path

from config import (
REPORT_CATEGORIES,
MAX_DESCRIPTION_LENGTH,
MAX_URL_LENGTH,
DATA_DIRECTORY,
)

def collect_report():
"""Collect information for a report."""

print("\n=== CyberRUHAN-FB Report Assistant ===")

for number, category in enumerate(REPORT_CATEGORIES, start=1):
    print(f"{number}. {category}")

try:
    choice = int(input("\nSelect report category: "))
    if not 1 <= choice <= len(REPORT_CATEGORIES):
        print("Invalid category selection.")
        return None
except ValueError:
    print("Please enter a valid number.")
    return None

account_url = input("Facebook profile or post URL: ").strip()
if len(account_url) > MAX_URL_LENGTH:
    print("The URL is too long.")
    return None

description = input("Describe the issue: ").strip()
if not description:
    print("A description is required.")
    return None

if len(description) > MAX_DESCRIPTION_LENGTH:
    print("The description is too long.")
    return None

evidence = input("Evidence notes (optional): ").strip()

return {
    "category": REPORT_CATEGORIES[choice - 1],
    "url": account_url,
    "description": description,
    "evidence_notes": evidence,
    "created_at": datetime.now(timezone.utc).isoformat(),
    "status": "Draft",
}

def save_report(report):
"""Save a report draft locally as JSON."""

if not report:
    return False

data_dir = Path(DATA_DIRECTORY)
data_dir.mkdir(parents=True, exist_ok=True)

report_file = data_dir / "reports.json"

if report_file.exists():
    try:
        with report_file.open("r", encoding="utf-8") as file:
            reports = json.load(file)

        if not isinstance(reports, list):
            reports = []
    except (json.JSONDecodeError, OSError):
        reports = []
else:
    reports = []

reports.append(report)

with report_file.open("w", encoding="utf-8") as file:
    json.dump(reports, file, indent=4, ensure_ascii=False)

print(f"\nReport draft saved to: {report_file}")
print("Review the details before submitting a report.")
return True

if name == "main":
draft = collect_report()

if draft:
    save_report(draft)
  if name == "main":
draft = collect_report()
if draft:
    save_report(draft)
  
