[![CI](https://github.com/Crynge/AdVantage/actions/workflows/ci.yml/badge.svg)](https://github.com/Crynge/AdVantage/actions/workflows/ci.yml)
[![Go](https://img.shields.io/badge/Go-1.22-00ADD8)](https://go.dev)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB)](https://python.org)

# AdVantage

**AI-powered advertising intelligence and budget optimization.**

Maximize ROAS (Return on Ad Spend) across campaigns with ML-driven budget allocation, creative performance prediction, and automated bidding.

---

## ROI Dashboard

```
  CAMPAIGN        SPEND      REVENUE    ROAS      STATUS
  ─────────────────────────────────────────────────────────
  Q3 Brand       $45,200    $187,300   4.14x     ● Optimal
  Q3 Performance $32,800    $98,400    3.00x     ● Optimal
  Q3 Retarget    $18,500    $24,050    1.30x     ⚡ Optimize
  Q3 Awareness   $12,000    $9,600     0.80x     ⚠️ Review
  ─────────────────────────────────────────────────────────
  TOTAL          $108,500   $319,350   2.94x
```

## Features

| Feature | Description |
|---|---|
| **Budget Optimizer** | Portfolio allocation using convex optimization and bandit algorithms |
| **Creative Scoring** | Predicts ad creative CTR and conversion rates before launch |
| **Automated Bidding** | Real-time bid adjustments based on conversion probability |
| **Agent Framework** | Autonomous agents monitor campaigns and suggest reallocations |
| **Forecasting** | Time-series spend and revenue predictions with uncertainty bounds |
| **Multi-channel** | Google Ads, Meta, TikTok, DV360, and The Trade Desk |

## Quick Start

```bash
go install github.com/Crynge/AdVantage/src/api/server

# Start the optimization API
advantage-server --port 8080 --config config.yaml
```

```python
from advantage.optimizer import BudgetOptimizer

optimizer = BudgetOptimizer(
    budget=100000,
    channels=[
        {"name": "google", "roas": 3.8, "volatility": 0.2},
        {"name": "meta", "roas": 2.9, "volatility": 0.3},
        {"name": "tiktok", "roas": 4.2, "volatility": 0.5},
    ],
)

allocation = optimizer.optimize()
# {'google': 42000, 'meta': 31000, 'tiktok': 27000}
```

## Agents

```python
from advantage.agents import CampaignMonitor

monitor = CampaignMonitor(
    channels=["google", "meta"],
    budget=50000,
    alert_threshold=0.15,  # Alert if ROAS drops 15%+
)

while True:
    alerts = monitor.check()
    for alert in alerts:
        print(f"[{alert.severity}] {alert.channel}: {alert.message}")
    await asyncio.sleep(3600)  # Check hourly
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/optimize` | Run budget optimization |
| `GET` | `/api/campaigns` | List active campaigns |
| `POST` | `/api/forecast` | Predict campaign performance |
| `GET` | `/api/report` | Generate ROI report |

## Modules

```
src/
├── api/
│   └── server.go              # Go REST API
├── advantage/
│   └── optimizer.py           # Budget optimization engine
└── agents/
    └── agent.py               # Autonomous campaign agents
```
