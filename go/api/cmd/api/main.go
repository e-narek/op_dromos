package main

import (
	"log"
	"net/http"

	"op_dromos/go/api/internal/httpserver"
)

func main() {
	mux := httpserver.NewMux()
	const addr = ":8080"
	log.Printf("op_dromos API listening on %s", addr)
	if err := http.ListenAndServe(addr, mux); err != nil {
		log.Fatal(err)
	}
}
