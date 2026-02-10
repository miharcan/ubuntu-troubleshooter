from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ubuntu Troubleshooting Helper")

class Input(BaseModel):
    text: str

def diagnose(text: str):
    t = text.lower()

    if "no space left on device" in t or "disk full" in t:
        return {
            "issue": "Disk space exhausted",
            "steps": [
                "Check disk usage",
                "Identify large directories",
                "Clean package cache"
            ],
            "commands": [
                "df -h",
                "du -sh /* 2>/dev/null | sort -h",
                "sudo apt clean"
            ]
        }

    if "apt" in t and ("failed" in t or "error" in t):
        return {
            "issue": "APT / package manager issue",
            "steps": [
                "Fix broken packages",
                "Refresh package lists"
            ],
            "commands": [
                "sudo dpkg --configure -a",
                "sudo apt update"
            ]
        }

    if "permission denied" in t:
        return {
            "issue": "Permission error",
            "steps": [
                "Check file ownership",
                "Verify file permissions"
            ],
            "commands": [
                "ls -l <file>",
                "sudo chown USER:USER <file>"
            ]
        }

    if any(k in t for k in [
        "network",
        "internet",
        "no connection",
        "cannot connect",
        "connection failed",
        "temporary failure in name resolution",
        "dns",
    ]):
        return {
            "issue": "Network connectivity issue",
            "steps": [
                "Check if the network interface is up",
                "Verify IP address and default gateway",
                "Test DNS resolution",
                "Check firewall rules"
            ],
            "commands": [
                "ip a",
                "ip route",
                "ping -c 3 8.8.8.8",
                "ping -c 3 google.com",
                "resolvectl status"
            ]
        }

    return {
        "issue": "Unknown issue",
        "steps": [
            "Check system logs",
            "Search the exact error message online"
        ],
        "commands": [
            "journalctl -xe"
        ]
    }


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/diagnose")
def diagnose_issue(payload: Input):
    return diagnose(payload.text)
