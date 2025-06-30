from flask import Flask, request, render_template, jsonify
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)

DATA_FILE = 'events.json'
TIME_WINDOW_MINUTES = 30  # Only show events from the last 30 minutes

def load_events():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_events(events):
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=4)

def is_duplicate(new_event, events):
    return any(event['id'] == new_event['id'] for event in events)

@app.route('/')
def index():
    events = load_events()
    now = datetime.utcnow()
    valid_events = [
        e for e in events
        if datetime.fromisoformat(e['timestamp']) >= now - timedelta(minutes=TIME_WINDOW_MINUTES)
    ]
    return render_template('index.html', events=valid_events)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    events = load_events()

    event_type = request.headers.get('X-GitHub-Event', 'unknown')
    new_event = {
        "id": str(payload.get("after") or payload.get("pull_request", {}).get("id")),
        "event": event_type,
        "repo": payload.get("repository", {}).get("full_name"),
        "sender": payload.get("sender", {}).get("login"),
        "timestamp": datetime.utcnow().isoformat()
    }

    if not is_duplicate(new_event, events):
        events.append(new_event)
        save_events(events)

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # For Render deployment
    app.run(host='0.0.0.0', port=port)
