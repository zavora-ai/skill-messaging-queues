---
name: messaging-queues
description: Orchestrate messaging operations — send push notifications, SMS, webhooks, manage channels, queue messages, and broadcast to groups. Use when sending push notifications, SMS messages, firing webhooks, managing message channels, queuing async tasks, or broadcasting to user groups.
license: Apache-2.0
compatibility: Requires mcp-messaging server connected.
allowed-tools: [send_push, broadcast, send_sms, fire_webhook, create_channel, send_message, get_messages, enqueue, dequeue, queue_status, subscribe_webhook]
metadata:
  category: communication
  author: Zavora AI
  mcp-server: mcp-messaging
  success-criteria:
    trigger-rate: "90% on messaging queries"
    delivery: "Confirm delivery on every send"
    queue-health: "Monitor queue depth to prevent backlogs"
---

# Messaging & Queues

You manage multi-channel messaging — push, SMS, webhooks, in-app messages, and async queues. Always confirm delivery. Monitor queue depth to prevent backlogs.

## Decision Tree

```
├── "push", "notification", "alert"? → send_push
├── "SMS", "text message"? → send_sms
├── "webhook", "HTTP callback"? → fire_webhook / subscribe_webhook
├── "broadcast", "all users", "announce"? → broadcast
├── "channel", "create channel"? → create_channel
├── "message", "send to channel"? → send_message / get_messages
├── "queue", "enqueue", "async task"? → enqueue / dequeue / queue_status
```

## Key Workflows

### Send Push Notification (1 call)
`send_push(recipient, title, body, priority)` → delivered

### Send SMS (1 call)
`send_sms(phone, message)` → delivered

### Fire Webhook (1 call)
`fire_webhook(url, payload, headers)` → response status

### Async Queue (2-3 calls)
1. `enqueue(queue, payload)` → message queued
2. `queue_status(queue)` → depth, processing rate
3. `dequeue(queue)` → process next message

### Broadcast (1 call)
`broadcast(channel, message)` → sent to all subscribers

## MUST DO
- Confirm delivery status on every send
- Monitor queue depth (alert if growing)
- Use appropriate channel (push for urgent, SMS for critical, webhook for systems)
- Rate limit broadcasts (don't spam)

## MUST NOT DO
- Don't send SMS for non-critical messages (cost)
- Don't let queues grow unbounded (monitor and alert)
- Don't fire webhooks without verifying endpoint is reachable

## Cross-MCP Orchestration

### Messaging + ITSM: Incident Alert Pipeline
```
ITSM: create_ticket(priority: "critical") → INC-1001
MESSAGING: send_push(recipient: oncall, title: "🚨 P1 Incident", body: "INC-1001: DB outage")
MESSAGING: send_sms(phone: oncall_phone, message: "P1: INC-1001 DB outage. Acknowledge now.")
MESSAGING: fire_webhook(url: pagerduty_url, payload: {incident: "INC-1001"})
```

### Messaging + Workflow: Async Task Processing
```
WORKFLOW: start_workflow(name: "batch_invoicing")
MESSAGING: enqueue(queue: "invoice_generation", payload: {customers: [...]})
MESSAGING: queue_status(queue: "invoice_generation") → {depth: 50, rate: "10/min"}
→ Monitor until queue drains
```

## Troubleshooting

**Push not delivered:** Check device token validity. Verify app has notification permissions.

**SMS failed:** Verify phone number format (E.164). Check provider balance.

**Queue growing:** Processing rate < enqueue rate. Scale consumers or pause producers.
