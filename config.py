==========================================

CyberRUHAN-FB

Configuration Settings

==========================================

APP_NAME = "CyberRUHAN-FB"
VERSION = "1.0.0"
AUTHOR = "RUHAN"

Application Settings

DEBUG = False
LANGUAGE = "en"

Report Categories

REPORT_CATEGORIES = [
"Fake Account",
"Impersonation",
"Harassment",
"Scam or Fraud",
"Inappropriate Content",
"Other Policy Violations"
]

Evidence Settings

REQUIRE_EVIDENCE = True
ALLOW_TEXT_EVIDENCE = True
ALLOW_URL_EVIDENCE = True

Storage Settings

DATA_DIRECTORY = "data"
REPORTS_FILE = "reports.json"
EVIDENCE_FILE = "evidence.json"

Input Validation

MAX_DESCRIPTION_LENGTH = 5000
MAX_URL_LENGTH = 2048

Safety Settings

CONFIRM_BEFORE_SAVE = True
AUTOMATIC_SUBMISSION = False

Important Notice

DISCLAIMER = (
"CyberRUHAN-FB helps organize evidence and prepare reports. "
"It does not attack, hack, lock, or suspend accounts. "
"Account enforcement decisions belong to the platform."
)
