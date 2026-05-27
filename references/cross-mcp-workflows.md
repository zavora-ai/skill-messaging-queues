# Messaging Cross-MCP Workflows

## Messaging + ITSM: Multi-Channel Incident Alert
```
MESSAGING: send_push(oncall, "🚨 P1") + send_sms(phone, "P1 INC-1001")
MESSAGING: fire_webhook(pagerduty_url, incident_data)
```

## Messaging + Workflow: Async Processing
```
MESSAGING: enqueue(queue: "batch_job", payload: task_data)
MESSAGING: queue_status(queue) → monitor depth
```

## Messaging + Payments: Payment Webhook
```
MESSAGING: subscribe_webhook(url: "/webhooks/stripe", events: ["payment.completed"])
→ Receives payment confirmations automatically
```
