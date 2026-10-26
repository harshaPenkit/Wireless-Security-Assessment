"""Offline unit tests - no lab targets or network required."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from wifi_audit import assess_ap, build_report  # noqa: E402


class ReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads((ROOT / "data" / "demo_observations.json").read_text())

    def test_demo_generates_report(self):
        report = build_report(self.example)
        self.assertIn("SYNTHETIC DEMONSTRATION", report)
        self.assertIn("NOT verified vulnerabilities", report)
        self.assertIn("OBS-01", report)

    def test_unprotected_guest_is_flagged_for_review(self):
        items = assess_ap(self.example["access_points"][0])
        self.assertIn("Guest segmentation", [i["control"] for i in items])

    def test_secure_demo_ap_has_no_findings(self):
        self.assertEqual(assess_ap(self.example["access_points"][1]), [])

    def test_firmware_review_absence_is_not_auto_vuln(self):
        items = assess_ap(self.example["access_points"][0])
        firmware = next(i for i in items if i["control"] == "Firmware maintenance")
        self.assertEqual(firmware["priority"], "Review")

    def test_missing_field_is_rejected(self):
        broken = dict(self.example["access_points"][1]); del broken["wps_enabled"]
        with self.assertRaises(ValueError):
            assess_ap(broken)

    def test_boolean_string_is_rejected(self):
        broken = dict(self.example["access_points"][1]); broken["wps_enabled"] = "false"
        with self.assertRaises(ValueError):
            assess_ap(broken)


if __name__ == "__main__":
    unittest.main()
