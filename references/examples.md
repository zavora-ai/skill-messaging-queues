# Messaging Examples

## Example 1: "Alert the on-call engineer"
```
send_push(recipient: "oncall_user", title: "🚨 P1 Incident", body: "DB outage. Acknowledge within 5 min.", priority: "critical")
send_sms(phone: "+254700000000", message: "P1: DB outage INC-1001. Acknowledge: https://...")
```
Response: "✅ Push + SMS sent to on-call. Awaiting acknowledgment."

## Example 2: "Check the invoice queue"
```
queue_status(queue: "invoice_generation") → {depth: 12, processing_rate: "5/min", eta_drain: "2.4 min"}
```
Response: "Invoice queue: 12 messages, processing at 5/min. Will drain in ~2.5 minutes."

## Example 3: "Fire a webhook to our payment processor"
```
fire_webhook(url: "https://payments.example.com/webhook", payload: {event: "invoice.paid", id: "inv_123"}, headers: {"X-Signature": "..."})
→ {status: 200, response_time: "120ms"}
```
Response: "✅ Webhook delivered (200 OK, 120ms)."
