from flask import Flask, request
import requests
import json

app = Flask(__name__)

DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/1458282969960681482/h2j-3eBf3QUyIe7yMs_FQ0t5ivdV0IaWgY0ci8pVpHlxGLN_kaUaXUfTPxoLnguYbTHG'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Extract alert info
    status = data.get('status', 'unknown')
    alerts = data.get('alerts', [])
    
    message = f"**{status.upper()}**\n\n"
    
    for alert in alerts:
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})
        
        message += f"**Alert:** {labels.get('alertname', 'Unknown')}\n"
        message += f"**Instance:** {labels.get('instance', 'Unknown')}\n"
        message += f"**Summary:** {annotations.get('summary', 'No summary')}\n\n"
    
    # Send to Discord
    payload = {"content": message}
    resp = requests.post(DISCORD_WEBHOOK, json=payload)
    
    return '', resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
