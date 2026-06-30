package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type OptimizeRequest struct {
	CampaignName    string   `json:"campaignName"`
	TotalBudget     float64  `json:"totalBudget"`
	TargetCPA       float64  `json:"targetCPA"`
	Platforms       []string `json:"platforms"`
	CreativeAssets  []string `json:"creativeAssets"`
	AudienceSegment string   `json:"audienceSegment"`
}

type Allocation struct {
	Platform string  `json:"platform"`
	Amount   float64 `json:"amount"`
	ROI      float64 `json:"predictedROI"`
}

type OptimizeResponse struct {
	Allocations      []Allocation `json:"allocations"`
	PredictedROI     float64      `json:"predictedROI"`
	PredictedClicks  int          `json:"predictedClicks"`
	PredictedImpress int          `json:"predictedImpressions"`
	Currency         string       `json:"currency"`
}

func handleOptimize(w http.ResponseWriter, r *http.Request) {
	var req OptimizeRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}
	platforms := req.Platforms
	if len(platforms) == 0 {
		platforms = []string{"meta", "google", "linkedin"}
	}
	var allocations []Allocation
	for _, p := range platforms {
		alloc := req.TotalBudget / float64(len(platforms))
		allocations = append(allocations, Allocation{Platform: p, Amount: alloc, ROI: 2.8})
	}
	resp := OptimizeResponse{
		Allocations:      allocations,
		PredictedROI:     2.8,
		PredictedClicks:  int(req.TotalBudget / req.TargetCPA),
		PredictedImpress: int(req.TotalBudget/req.TargetCPA) * 100,
		Currency:         "USD",
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

func handleHealth(w http.ResponseWriter, _ *http.Request) {
	json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}

func main() {
	http.HandleFunc("/api/v1/optimize", handleOptimize)
	http.HandleFunc("/health", handleHealth)
	fmt.Println("AdVantage API on :9090")
	http.ListenAndServe(":9090", nil)
}
