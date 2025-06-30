# GitHub Webhook Listener

This is a simple Flask app that receives webhook payloads from GitHub and displays recent events on a UI. It filters events that are older than 30 minutes or already displayed.

## Setup

```bash
pip install -r requirements.txt
python app.py
