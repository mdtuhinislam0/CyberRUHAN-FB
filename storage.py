import json
from pathlib import Path

from config import DATA_DIRECTORY

class Storage:
"""Store and retrieve report and evidence records locally."""

def __init__(self):
    self.data_dir = Path(DATA_DIRECTORY)
    self.data_dir.mkdir(parents=True, exist_ok=True)

    self.reports_file = self.data_dir / "reports.json"
    self.evidence_file = self.data_dir / "evidence.json"

def _read_records(self, file_path):
    """Read records from a JSON file."""

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if isinstance(records, list):
            return records

        raise ValueError(
            f"Expected a list in {file_path.name}"
        )

    except json.JSONDecodeError as error:
        raise ValueError(
            f"{file_path.name} contains invalid JSON."
        ) from error

def _write_records(self, file_path, records):
    """Write records to a JSON file."""

    temporary_file = file_path.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(
            records,
            file,
            indent=4,
            ensure_ascii=False,
        )

    temporary_file.replace(file_path)

def save_report(self, report):
    """Save one report record."""

    if not isinstance(report, dict):
        raise TypeError("Report must be a dictionary.")

    records = self._read_records(self.reports_file)
    records.append(report)
    self._write_records(self.reports_file, records)

    return True

def get_reports(self):
    """Return all saved report records."""

    return self._read_records(self.reports_file)

def save_evidence(self, evidence):
    """Save one evidence record."""

    if not isinstance(evidence, dict):
        raise TypeError("Evidence must be a dictionary.")

    records = self._read_records(self.evidence_file)
    records.append(evidence)
    self._write_records(self.evidence_file, records)

    return True

def get_evidence(self):
    """Return all saved evidence records."""

    return self._read_records(self.evidence_file)

if name == "main":
storage = Storage()

print("=== CyberRUHAN-FB Storage ===")
print(f"Reports saved: {len(storage.get_reports())}")
print(f"Evidence records saved: {len(storage.get_evidence())}")
print(f"Data directory: {storage.data_dir.resolve()}")
