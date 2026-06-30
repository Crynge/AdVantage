from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CreativeScore:
    asset_name: str
    predicted_ctr: float
    predicted_conv_rate: float
    quality_score: float

    @property
    def effectiveness(self) -> float:
        return round(self.predicted_ctr * self.predicted_conv_rate * 100, 2)


@dataclass
class AudienceInsight:
    segment_name: str
    estimated_size: int
    expected_cpa: float
    relevance_score: float


@dataclass
class BudgetPlan:
    total_budget: float
    allocations: dict
    predicted_impressions: int
    predicted_clicks: int
    predicted_roi: float

    @property
    def summary(self) -> str:
        lines = [
            f"Budget Plan: ${self.total_budget:,.0f}",
            f"Allocations: {self.allocations}",
            f"Predicted ROI: {self.predicted_roi:.1f}x",
            f"Expected clicks: {self.predicted_clicks:,}",
        ]
        return "\n".join(lines)


class AdOptimizer:
    def __init__(
        self,
        platforms: Optional[list] = None,
        total_budget: float = 50000,
        currency: str = "USD",
    ):
        self.platforms = platforms or ["meta", "google"]
        self.total_budget = total_budget
        self.currency = currency

    def optimize(
        self,
        campaign_name: str,
        target_cpa: float,
        creative_assets: Optional[list] = None,
        audience_segments: Optional[list] = None,
    ) -> BudgetPlan:
        scores = self._score_creatives(creative_assets or [])
        audiences = self._research_audiences(audience_segments or [])
        allocation = self._allocate_budget(scores, audiences)
        roi = self._predict_roi(allocation, target_cpa)

        return BudgetPlan(
            total_budget=self.total_budget,
            allocations=allocation,
            predicted_impressions=int(roi["impressions"]),
            predicted_clicks=int(roi["clicks"]),
            predicted_roi=roi["roi"],
        )

    def _score_creatives(self, assets: list) -> list:
        return [
            CreativeScore(asset_name=a, predicted_ctr=0.042, predicted_conv_rate=0.08, quality_score=7.5)
            for a in assets
        ]

    def _research_audiences(self, segments: list) -> list:
        return [
            AudienceInsight(segment_name=s, estimated_size=500000, expected_cpa=15.0, relevance_score=8.0)
            for s in (segments or ["prospecting", "retargeting"])
        ]

    def _allocate_budget(self, scores: list, audiences: list) -> dict:
        per_platform = self.total_budget / len(self.platforms)
        return {p: per_platform for p in self.platforms}

    def _predict_roi(self, allocation: dict, target_cpa: float) -> dict:
        total_spend = sum(allocation.values())
        clicks = total_spend / max(target_cpa, 1)
        return {"impressions": clicks * 100, "clicks": clicks, "roi": 2.8}
