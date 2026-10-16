import json
from datetime import datetime, timezone
from pathlib import Path

from config import DATA_DIRECTORY, MAX_DESCRIPTION_LENGTH, MAX_URL_LENGTH

def collect_evidence():
"""Collect evidence details for a report."""

print("\n=== CyberRUHAN-FB Evidence Manager ===")

evidence_type = input(
    "Evidence type (URL, screenshot, message, other): "
).strip().lower()

allowed_types = {"url", "screenshot", "message", "other"}

if evidence_type not in allowed_types:
    print("Invalid evidence type.")
    return None

reference = input(
    "Evidence reference or file name (optional): "
).strip()

if len(reference) > MAX_URL_LENGTH:
    print("Reference is too long.")
    return None

description = input("Evidence description: ").strip()

if not description:
    print("Please provide an evidence description.")
    return None

if len(description) > MAX_DESCRIPTION_LENGTH:
    print("Description is too long.")
    return None

return {
    "type": evidence_type,
    "reference": reference,
    "description": description,
    "created_at": datetime.now(timezone.utc).isoformat(),
}

def save_evidence(evidence):
"""Save evidence notes locally in JSON format."""

if not evidence:
    return False

data_dir = Path(DATA_DIRECTORY)
data_dir.mkdir(parents=True, exist_ok=True)

evidence_file = data_dir / "evidence.json"

if evidence_file.exists():
    try:
        with evidence_file.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            records = []
    except (json.JSONDecodeError, OSError):
        records = []
else:
    records = []

records.append(evidence)

with evidence_file.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=4, ensure_ascii=False)

print(f"\nEvidence notes saved to: {evidence_file}")
return True

if name == "main":
evidence = collect_evidence()

if evidence:
    save_evidence(evidence)

