import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

APP_NAME = "CyberRUHAN-FB"
DATA_DIR = Path("evidence")
DATA_FILE = DATA_DIR / "reports.json"


def setup():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def banner():
    print("\033[96m")
    print("=" * 46)
    print("       CyberRUHAN-FB")
    print("  Facebook Security Assistant")
    print("=" * 46)
    print("\033[0m")


def valid_facebook_url(url):
    try:
        parsed = urlparse(url.strip())
        host = (parsed.hostname or "").lower()

        allowed = {
            "facebook.com",
            "www.facebook.com",
            "m.facebook.com",
            "web.facebook.com",
            "fb.watch",
            "www.fb.watch",
        }

        return (
            parsed.scheme == "https"
            and host in allowed
            and bool(parsed.path.strip("/"))
        )
    except (ValueError, AttributeError):
        return False


def load_reports():
    setup()

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_report(report):
    reports = load_reports()
    reports.append(report)

    DATA_FILE.write_text(
        json.dumps(reports, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def analyze_profile():
    print("\n--- Profile Link Checker ---")
    url = input("Facebook profile/post URL: ").strip()

    if not valid_facebook_url(url):
        print("\n[!] Invalid or unsupported Facebook URL.")
        print("Use a valid HTTPS Facebook profile or post link.")
        return

    print("\n[+] URL format looks valid.")
    print("[i] This does NOT establish whether the account is fake.")
    print("[i] No Facebook account has been contacted or modified.")

    details = input(
        "Describe the suspected impersonation or concern: "
    ).strip()

    report = {
        "type": "profile_review",
        "url": url,
        "details": details,
        "created_at": datetime.now().astimezone().isoformat(),
    }

    save_report(report)
    print("\n[+] Review notes saved locally.")


def create_report():
    print("\n--- Evidence & Report Assistant ---")

    url = input("Facebook profile/post URL: ").strip()

    if not valid_facebook_url(url):
        print("[!] Please enter a valid HTTPS Facebook URL.")
        return

    category = input(
        "Category (impersonation/scam/harassment/content): "
    ).strip().lower()

    details = input(
        "Describe what happened and what evidence exists: "
    ).strip()

    evidence = input(
        "Evidence reference (optional screenshot filename/link): "
    ).strip()

    report = {
        "type": "report_draft",
        "url": url,
        "category": category,
        "details": details,
        "evidence": evidence,
        "created_at": datetime.now().astimezone().isoformat(),
        "status": "draft",
    }

    save_report(report)

    print("\n========== REPORT DRAFT ==========")
    print("Category:", category)
    print("Profile/Post:", url)
    print("Description:", details)
    print("Evidence:", evidence or "Not supplied")
    print("=================================")
    print("Saved locally. Review before submitting.")


def view_reports():
    reports = load_reports()

    print("\n--- Saved Reports ---")

    if not reports:
        print("No reports saved yet.")
        return

    for number, report in enumerate(reports, start=1):
        print(f"\n[{number}] {report.get('type', 'unknown')}")
        print("URL:", report.get("url", ""))
        print("Category:", report.get("category", "-"))
        print("Details:", report.get("details", ""))
        print("Created:", report.get("created_at", ""))


def show_help():
    print("""
CyberRUHAN-FB Help
------------------
1. Profile Link Checker
   Checks URL format and records your observations.

2. Report Assistant
   Creates a local draft based on your evidence.

3. View Saved Reports
   Displays previously saved local notes.

Important:
- This tool does not determine account authenticity.
- It does not access Facebook's internal systems.
- It does not automatically submit reports.
- Never upload private evidence to a public repository.
""")


def main():
    setup()

    while True:
        banner()
        print("1. Check Profile Link")
        print("2. Create Report Draft")
        print("3. View Saved Reports")
        print("4. Help")
        print("0. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            analyze_profile()
        elif choice == "2":
            create_report()
        elif choice == "3":
            view_reports()
        elif choice == "4":
            show_help()
        elif choice == "0":
            print("CyberRUHAN-FB closed.")
            break
        else:
            print("Invalid option. Please choose 0-4.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
