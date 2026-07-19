import json
import random
import requests

TOPIC = "mitti-reminders-2026"

# Load laws
with open("data/laws.json", "r", encoding="utf-8") as f:
    laws = json.load(f)

# Load state
with open("data/state.json", "r", encoding="utf-8") as f:
    state = json.load(f)

# Create new shuffled order if needed
if not state["order"] or state["index"] >= len(state["order"]):
    state["order"] = list(range(len(laws)))
    random.shuffle(state["order"])
    state["index"] = 0

# Pick next law
law_index = state["order"][state["index"]]
law = laws[law_index]

message = f"""{law['title']}

{law['description']}"""

# Update state
state["index"] += 1

with open("data/state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, indent=4)

# Send notification
response = requests.post(
    f"https://ntfy.sh/{TOPIC}",
    data=message.encode("utf-8")
)

print(response.status_code)
print(message)