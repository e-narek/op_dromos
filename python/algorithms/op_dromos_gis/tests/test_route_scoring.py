import unittest

from op_dromos_gis.route_scoring import score_route


class ScoreRouteTests(unittest.TestCase):
    def test_score_route_basic(self):
        payload = score_route(distance_km=8.0, elevation_gain_m=100.0, traffic_index=0.2)
        self.assertEqual(payload["score"], 76.0)

    def test_score_route_rejects_invalid_traffic(self):
        with self.assertRaises(ValueError):
            score_route(distance_km=1.0, elevation_gain_m=2.0, traffic_index=1.5)


if __name__ == "__main__":
    unittest.main()
