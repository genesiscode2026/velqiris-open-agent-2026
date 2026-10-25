"""Unit tests for ZetarisClient."""

import unittest
from agent.config import AgentConfig
from agent.zetaris_client import ZetarisClient

class TestZetarisClient(unittest.TestCase):

    def setUp(self):
        self.config = AgentConfig({
            "ZETARIS_REST_URL": "http://localhost:3000",
            "ZETARIS_ORG_ID": "test-org",
            "ZETARIS_API_KEY": "", # Offline mode
        })
        self.client = ZetarisClient(self.config)

    def test_live_mode_fails_closed_without_credentials(self):
        """Missing live credentials must never return fixture data as success."""
        res = self.client.run_sql("SELECT 1 AS one")
        self.assertFalse(res["success"])
        self.assertEqual(res["mode"], "LIVE_UNCONFIGURED")
        self.assertEqual(res["rows"], [])
        self.assertFalse(self.client.verify_connection())

    def test_explicit_dry_run_returns_fixture(self):
        """Fixture data is available only through an explicit dry run."""
        res = self.client.run_sql("SELECT 1 AS one", dry_run=True)
        self.assertTrue(res["success"])
        self.assertEqual(res["row_count"], 1)
        self.assertEqual(res["rows"][0]["one"], 1)
        self.assertEqual(res["mode"], "OFFLINE_SIMULATION")
        self.assertEqual(res["source"], "BUILT_IN_FIXTURE")
        self.assertTrue(bool(res["request_id"]))

    def test_market_feed_query_simulation(self):
        """Verifies querying market feeds returns multi-venue rows including the anomaly."""
        res = self.client.run_sql("SELECT * FROM market_feeds", dry_run=True)
        self.assertTrue(res["success"])
        self.assertGreaterEqual(res["row_count"], 4)
        venues = [r["venue"] for r in res["rows"]]
        self.assertIn("BINANCE", venues)
        self.assertIn("COINBASE", venues)
        self.assertIn("OKX", venues)
        self.assertIn("ANOMALY_DEX", venues)

    def test_unique_uuid_per_request(self):
        """Verifies each query gets a unique UUID X-Request-ID as required by Zetaris."""
        r1 = self.client.run_sql("SELECT 1", dry_run=True)
        r2 = self.client.run_sql("SELECT 1", dry_run=True)
        self.assertNotEqual(r1["request_id"], r2["request_id"])

if __name__ == "__main__":
    unittest.main()
