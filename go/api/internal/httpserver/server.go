package httpserver

import (
	"encoding/json"
	"net/http"
)

type HealthResponse struct {
	Service string `json:"service"`
	Status  string `json:"status"`
}

func NewMux() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, http.StatusText(http.StatusMethodNotAllowed), http.StatusMethodNotAllowed)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(HealthResponse{Service: "op_dromos_api", Status: "ok"})
	})
	return mux
}
