<div align="center">
  <img src="docs/assets/logo.svg" alt="AdVantage" width="360">
  <p><strong>AI-Powered Advertising Intelligence & Budget Optimization</strong></p>
  <p>Multi-agent ad creative testing · budget allocation · audience insights · performance tracking</p>

  [![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://python.org)
  [![Go](https://img.shields.io/badge/Go-1.22%2B-00ADD8?logo=go&logoColor=white)](https://go.dev/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![CI](https://github.com/Crynge/AdVantage/actions/workflows/ci.yml/badge.svg)](https://github.com/Crynge/AdVantage/actions/workflows/ci.yml)
  [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
  [![GitHub Stars](https://img.shields.io/github/stars/Crynge/AdVantage?style=social)](https://github.com/Crynge/AdVantage)

</div>

---

## Overview

AdVantage deploys specialized AI agents to optimize every layer of digital advertising. From creative analysis and audience research to budget allocation and performance tracking, it works like an autonomous ad buying desk — but runs on your infrastructure.

## Key Features

- **Creative performance scoring** — Predicts ad creative effectiveness before launch
- **Budget optimization** — Dynamic allocation across channels and campaigns
- **Audience intelligence** — Lookalike discovery, segmentation, and targeting suggestions
- **Performance analytics** — Real-time attribution with causal impact models
- **Platform-agnostic** — Works with Meta Ads, Google Ads, LinkedIn, TikTok, and more

## Architecture

```
Campaign Config → BudgetOptimizer → CreativeAnalyst
                  → AudienceResearcher → PerformanceTracker
                    → Unified Budget & Creative Recommendations
```

## Quick Start

```bash
pip install -e .
python -m advantage optimize --budget 50000 --platforms meta,google,linkedin
```

## Installation

```bash
git clone https://github.com/Crynge/AdVantage.git
cd AdVantage
pip install -e ".[dev]"
```

## Usage

```python
from advantage import AdOptimizer

optimizer = AdOptimizer(
    platforms=["meta", "google", "linkedin"],
    total_budget=100000,
    currency="USD"
)

plan = optimizer.optimize(
    campaign_name="Summer Sale 2026",
    target_cpa=25.00,
    creative_assets=["./assets/creative_v1.jpg", "./assets/creative_v2.mp4"],
    audience_segments=["retargeting", "lookalike", "prospecting"]
)

print(plan.budget_allocation)
print(plan.predicted_roi)
```

## Agent Roles

| Agent | Role | Tools |
|-------|------|-------|
| CreativeAnalyst | Scores ad creatives, suggests variations, predicts CTR | Vision AI, copy scoring |
| BudgetOptimizer | Allocates budget across channels, optimizes bids | Portfolio optimizer, bid simulator |
| AudienceResearcher | Finds high-value segments, lookalike modeling | Demographic API, interest graph |
| PerformanceTracker | Real-time attribution, anomaly detection | Analytics pipeline, alert engine |
