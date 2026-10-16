import re
import json
from datetime import datetime, timezone
from pathlib import Path

def current_timestamp():
"""Return the current UTC date and time."""

return datetime.now(timezone.utc).isoformat()

def clean_text(value):
"""Remove unnecessary whitespace from text."""

if not isinstance(value, str):
    return ""

return value.strip()

def safe_filename(value, max_length=80):
"""Convert text into a safe filename."""

if not isinstance(value, str):
    return "untitled"

value = value.strip()
value = re.sub(r"[^a-zA-Z0-9._-]+", "_", value)
value = value.strip("._-")

if not value:
    return "untitled"

return value[:max_length]

def load_json(file_path, default=None):
"""Load JSON data safely."""

path = Path(file_path)

if not path.exists():
    return default if default is not None else []

try:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
except (json.JSONDecodeError, OSError):
    return default if default is not None else []

def save_json(file_path, data):
"""Save data as formatted JSON."""

path = Path(file_path)
path.parent.mkdir(parents=True, exist_ok=True)

temporary_path = path.with_suffix(".tmp")

with temporary_path.open("w", encoding="utf-8") as file:
    json.dump(
        data,
        file,
        indent=4,
        ensure_ascii=False,
    )

temporary_path.replace(path)

def report_summary(report):
"""Create a short summary of a report."""

if not isinstance(report, dict):
    return "Invalid report data."

category = clean_text(report.get("category", "Unknown"))
status = clean_text(report.get("status", "Draft"))
created_at = clean_text(report.get("created_at", "Unknown"))

return (
    f"Category: {category}\n"
    f"Status: {status}\n"
    f"Created: {created_at}"
)

if name == "main":
print("=== CyberRUHAN-FB Utilities ===")
print("Current UTC time:", current_timestamp())
print("Filename example:", safe_filename("Facebook Report #1"))
print("\nUtilities loaded successfully.")
