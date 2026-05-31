# 📨 Queue Status Report

**Generated:** {timestamp}
**Broker:** {broker_name}
**Environment:** {environment}

## Queue Health

| Queue | Depth | Consumers | Status |
|-------|-------|-----------|--------|
| {queue_1} | {depth_1} | {consumers_1} | {status_1} |
| {queue_2} | {depth_2} | {consumers_2} | {status_2} |
| {queue_3} | {depth_3} | {consumers_3} | {status_3} |

## Throughput

| Metric | Value |
|--------|-------|
| Messages/sec (in) | {msg_in_rate} |
| Messages/sec (out) | {msg_out_rate} |
| Dead Letter Count | {dlq_count} |
| Avg Latency | {avg_latency} |

## Status Legend

- ✅ Healthy — Processing normally
- ⚠️ Backlog — Depth exceeds threshold
- ❌ Stalled — No consumers active

---
*Monitored by {agent_name} • {uptime} uptime*
