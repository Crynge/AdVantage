from advantage import AdOptimizer


class TestAdOptimizer:
    def test_optimize_returns_plan(self):
        optimizer = AdOptimizer()
        plan = optimizer.optimize(
            campaign_name="Test Campaign",
            target_cpa=25.0,
            creative_assets=["ad_v1.jpg", "ad_v2.mp4"],
            audience_segments=["retargeting", "prospecting"],
        )
        assert plan.total_budget == 50000
        assert "meta" in plan.allocations
        assert plan.predicted_roi > 0

    def test_custom_platforms(self):
        optimizer = AdOptimizer(platforms=["tiktok"], total_budget=10000)
        plan = optimizer.optimize(campaign_name="X", target_cpa=10.0)
        assert list(plan.allocations.keys()) == ["tiktok"]

    def test_creative_scoring(self):
        optimizer = AdOptimizer()
        scores = optimizer._score_creatives(["a.jpg", "b.mp4"])
        assert len(scores) == 2
        assert scores[0].effectiveness > 0
