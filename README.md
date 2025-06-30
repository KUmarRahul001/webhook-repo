# GitHub Webhook Listener

This is a simple Flask app that receives webhook payloads from GitHub and displays recent events on a UI. It filters events that are older than 30 minutes or already displayed.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Webhook Endpoint
POST to ```/webhook``` from GitHub.

---
## Supported Events
- Push
- Pull Request
- (Optional) Merge

---

## 🔗 Next Steps for You:

1. **Push this code** to your two GitHub repos:
   - Push the **GitHub Actions YAML** to `action-repo`
   - Push the **Flask code + UI** to `webhook-repo`

2. **Deploy the Flask app** (you can use **Render, Railway, or local tunneling with ngrok**).

3. **Set the GitHub webhook**:
   - Go to your **`action-repo`** → Settings → Webhooks → Add Webhook
   - Use your `/webhook` endpoint as the URL
   - Content type: `application/json`
   - Events: Send everything or just `push`, `pull_request`, optionally `merge`

4. **Test by pushing to `action-repo`** and see events appear on the UI.




