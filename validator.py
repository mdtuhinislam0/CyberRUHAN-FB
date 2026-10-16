from urllib.parse import urlparse

from config import (
REPORT_CATEGORIES,
MAX_DESCRIPTION_LENGTH,
MAX_URL_LENGTH,
)

def validate_category(category):
"""Check whether the report category is supported."""

if not isinstance(category, str):
    return False, "Category must be text."

if category not in REPORT_CATEGORIES:
    return False, "Invalid report category."

return True, "Category is valid."

def validate_url(url):
"""Validate a public HTTP or HTTPS URL."""

if not isinstance(url, str):
    return False, "URL must be text."

url = url.strip()

if not url:
    return False, "URL is required."

if len(url) > MAX_URL_LENGTH:
    return False, "URL exceeds the maximum allowed length."

try:
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False, "URL must use HTTP or HTTPS."

    if not parsed.hostname:
        return False, "URL must contain a valid hostname."

    if parsed.username or parsed.password:
        return False, "URLs containing credentials are not allowed."

except ValueError:
    return False, "Malformed URL."

return True, "URL format is valid."

def validate_description(description):
"""Validate a report description."""

if not isinstance(description, str):
    return False, "Description must be text."

description = description.strip()

if not description:
    return False, "Description cannot be empty."

if len(description) > MAX_DESCRIPTION_LENGTH:
    return False, "Description exceeds the maximum allowed length."

return True, "Description is valid."

def validate_report(report):
"""Validate the main fields of a report."""

if not isinstance(report, dict):
    return False, ["Report must be a dictionary."]

errors = []

category_ok, category_message = validate_category(
    report.get("category")
)
if not category_ok:
    errors.append(category_message)

description_ok, description_message = validate_description(
    report.get("description")
)
if not description_ok:
    errors.append(description_message)

url = report.get("url", "").strip() if isinstance(
    report.get("url", ""), str
) else ""

# URL is optional, but if provided it must be valid.
if url:
    url_ok, url_message = validate_url(url)
    if not url_ok:
        errors.append(url_message)

if errors:
    return False, errors

return True, ["Report data is valid."]

if name == "main":
print("=== CyberRUHAN-FB Validator ===")

category = input("Enter report category: ").strip()
description = input("Enter report description: ").strip()
url = input("Enter URL (optional): ").strip()

test_report = {
    "category": category,
    "description": description,
    "url": url,
}

valid, messages = validate_report(test_report)

for message in messages:
    print(("[OK] " if valid else "[ERROR] ") + message)

if valid:
    print("\nValidation completed successfully.")
else:
    print("\nPlease correct the invalid fields.")
