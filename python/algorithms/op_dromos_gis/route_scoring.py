from typing import Dict


def score_route(distance_km: float, elevation_gain_m: float, traffic_index: float) -> Dict[str, float]:
    """Return a simple route score payload for API consumption."""
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    if elevation_gain_m < 0:
        raise ValueError("elevation_gain_m must be non-negative")
    if not 0 <= traffic_index <= 1:
        raise ValueError("traffic_index must be between 0 and 1")

    score = max(0.0, 100.0 - (distance_km * 2.0 + elevation_gain_m * 0.02 + traffic_index * 30.0))
    return {
        "distance_km": distance_km,
        "elevation_gain_m": elevation_gain_m,
        "traffic_index": traffic_index,
        "score": round(score, 2),
    }
