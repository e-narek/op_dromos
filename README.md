# op_dromos
Outil de cartographie.

## Skeleton stack

This repository now includes a minimal map/GPS foundation for:

- **C++ routing engine** scaffold with optional **Valhalla** linkage (`/cpp`)
- **Python GIS algorithm** package for PostGIS/OpenStreetMap-derived computations (`/python/algorithms`)
- **Golang backend API** that can expose map services to mobile apps (`/go/api`)
- **Container orchestration** for **PostGIS** and **Valhalla** (`/docker-compose.yml`)

## Quick start

### 1) C++ build

```bash
cd /home/runner/work/op_dromos/op_dromos/cpp
cmake -S . -B build
cmake --build build
./build/route_engine
```

If Valhalla development libraries are installed and available via `pkg-config`, the binary reports `valhalla-linked`; otherwise it runs in scaffold mode.

### 2) Python algorithms

```bash
cd /home/runner/work/op_dromos/op_dromos/python/algorithms
python -m unittest discover -s op_dromos_gis/tests
```

### 3) Go API

```bash
cd /home/runner/work/op_dromos/op_dromos/go/api
go test ./...
go run ./cmd/api
```

### 4) Containers (PostGIS + Valhalla + API)

```bash
cd /home/runner/work/op_dromos/op_dromos
docker compose up --build
```
