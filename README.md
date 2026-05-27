# Messaging & Queues Skill

> Multi-channel messaging for AI agents — push notifications, SMS, webhooks, in-app messages, async queues, and broadcasts.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--messaging-green)](https://github.com/zavora-ai/mcp-messaging)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Push Notification | 1 | Alert user on device |
| SMS | 1 | Critical text message |
| Webhook | 1 | System-to-system callback |
| Broadcast | 1 | Message all channel subscribers |
| Queue | 1-2 | Async task processing |

### Channel Selection

| Urgency | Use |
|---------|-----|
| Critical (wake up) | SMS + Push |
| Urgent (act now) | Push |
| Normal (FYI) | In-app message |
| System event | Webhook |
| Async task | Queue |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-messaging-queues.git \
  ~/.skills/skills/messaging-queues
```

## Requirements

**Required:** `mcp-messaging` (11 tools)
**Cross-MCP:** `mcp-itsm` (incident alerts), `mcp-workflow` (async tasks), `mcp-payments` (webhooks)

## Success Criteria

| Metric | Target |
|--------|--------|
| Delivery | Confirmed on every send |
| Queue health | Alert if depth growing |
| Channel selection | Appropriate urgency matching |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
