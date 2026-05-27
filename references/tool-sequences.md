# Messaging Tool Sequences (11 tools)

| Tool | Purpose | Channel |
|------|---------|---------|
| `send_push` | Push notification | Mobile/desktop |
| `broadcast` | Send to all in channel | Multi-device |
| `send_sms` | Text message | Phone |
| `fire_webhook` | HTTP callback | System-to-system |
| `create_channel` | Create messaging channel | — |
| `send_message` | Send to channel | In-app |
| `get_messages` | Read channel messages | In-app |
| `enqueue` | Add to async queue | Queue |
| `dequeue` | Process from queue | Queue |
| `queue_status` | Queue depth + rate | Queue |
| `subscribe_webhook` | Register webhook endpoint | System |

## Channel Selection Guide
| Urgency | Channel | Tool |
|---------|---------|------|
| Critical (wake up) | SMS + Push | send_sms + send_push |
| Urgent (act now) | Push | send_push |
| Normal (FYI) | In-app | send_message |
| System event | Webhook | fire_webhook |
| Async task | Queue | enqueue |
