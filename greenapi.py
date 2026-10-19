"""Send countdown messages to the WhatsApp group through Green API.

Usage:
  python greenapi.py status              # check WhatsApp is linked
  python greenapi.py groups              # list your groups and their IDs
  python greenapi.py test "Hello 🌴"     # send a sample message to the group
  python greenapi.py today               # send today's scheduled message (if any)
  python greenapi.py shortcut            # print the URL/body for the iPhone shortcut
"""

import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
SECRETS = HERE / "greenapi_secrets.json"


def load_secrets():
    if not SECRETS.exists():
        SECRETS.write_text(json.dumps({
            "api_url": "https://api.green-api.com",
            "id_instance": "",
            "api_token": "",
            "group_id": "",
        }, indent=2), encoding="utf-8")
        sys.exit(f"Fill in {SECRETS} with your Green API details, then run again.")
    return json.loads(SECRETS.read_text(encoding="utf-8"))


def call(s, method, body=None):
    url = f"{s['api_url'].rstrip('/')}/waInstance{s['id_instance']}/{method}/{s['api_token']}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def send(s, text):
    if not s.get("group_id"):
        sys.exit("group_id is empty. Run `python greenapi.py groups` and copy the ID into the secrets file.")
    result = call(s, "sendMessage", {"chatId": s["group_id"], "message": text})
    print(f"Sent ✅ (id {result.get('idMessage')}): {text}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    s = load_secrets()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"

    if cmd == "status":
        print(call(s, "getStateInstance"))  # want {'stateInstance': 'authorized'}
    elif cmd == "groups":
        for c in call(s, "getContacts"):
            if c.get("type") == "group" or c["id"].endswith("@g.us"):
                print(f"{c['id']:<35} {c.get('name') or c.get('contactName', '')}")
    elif cmd == "test":
        send(s, sys.argv[2] if len(sys.argv) > 2 else "Test message from the trip countdown bot 🌴")
    elif cmd == "today":
        schedule = json.loads((HERE / "countdown_schedule.json").read_text(encoding="utf-8"))
        msg = schedule.get(date.today().isoformat())
        send(s, msg) if msg else print("No post scheduled today.")
    elif cmd == "shortcut":
        print("URL:  ", f"{s['api_url'].rstrip('/')}/waInstance{s['id_instance']}/sendMessage/{s['api_token']}")
        print("Body:  JSON  chatId =", s["group_id"], "  message = Dictionary Value")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
