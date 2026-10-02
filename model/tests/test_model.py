import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import feasibility_model as fm  # noqa: E402


class FinanceHelpersTest(unittest.TestCase):
    def test_npv_known_value(self):
        self.assertAlmostEqual(fm.npv(0.10, [-100, 110]), 0.0, places=6)

    def test_irr_recovers_rate(self):
        self.assertAlmostEqual(fm.irr([-100, 60, 60]), 0.1307, places=3)

    def test_irr_none_without_sign_change(self):
        self.assertIsNone(fm.irr([100, 100, 100]))

    def test_payback(self):
        self.assertAlmostEqual(fm.payback_years([-100, 50, 50, 50]), 2.0)
        self.assertIsNone(fm.payback_years([-100, 10, 10]))


class ModelTest(unittest.TestCase):
    def setUp(self):
        self.scenarios = {s: fm.load_assumptions(fm.ASSUMPTIONS_DIR / f"{s}.json") for s in fm.SCENARIOS}

    def test_projection_length(self):
        a = self.scenarios["base"]
        self.assertEqual(len(fm.project(a)), a["years"])

    def test_scenarios_are_ordered(self):
        npvs = [fm.evaluate(self.scenarios[s])["npv"] for s in fm.SCENARIOS]
        self.assertLess(npvs[0], npvs[1])
        self.assertLess(npvs[1], npvs[2])

    def test_higher_price_raises_npv(self):
        a = dict(self.scenarios["base"])
        base = fm.evaluate(a)["npv"]
        a["price_per_unit"] *= 1.1
        self.assertGreater(fm.evaluate(a)["npv"], base)

    def test_no_tax_on_losses(self):
        for r in fm.project(self.scenarios["downside"]):
            if r["ebitda"] <= 0:
                self.assertEqual(r["tax"], 0.0)


if __name__ == "__main__":
    unittest.main()
