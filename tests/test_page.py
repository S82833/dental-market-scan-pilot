from pathlib import Path
import unittest


PAGE = Path(__file__).resolve().parents[1] / "index.html"


class LandingPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.lower = cls.html.lower()

    def test_presents_the_multi_vertical_product(self) -> None:
        self.assertIn("Local Opportunity Finder", self.html)
        self.assertIn("Choose a category. Choose a city.", self.html)
        self.assertIn("private prototype", self.lower)
        self.assertNotIn("Dental Market Scan", self.html)

    def test_does_not_accept_payment_or_sell_a_dental_spreadsheet(self) -> None:
        self.assertNotIn("paypal.com/ncp/payment", self.lower)
        self.assertNotIn("checkout", self.lower)
        self.assertNotIn("buy the pilot", self.lower)
        self.assertNotIn("US$25", self.html)

    def test_states_data_limits_and_conservative_website_language(self) -> None:
        self.assertIn("A missing field is not proof that the information does not exist.", self.html)
        self.assertIn("coverage varies by category and location", self.lower)
        self.assertNotIn("does not have a website", self.lower)

    def test_has_an_authorized_support_contact(self) -> None:
        self.assertIn('href="mailto:simonharth61@gmail.com"', self.html)

    def test_is_responsive_and_kept_out_of_search_indexes_during_validation(self) -> None:
        self.assertIn('name="viewport"', self.html)
        self.assertIn('name="robots" content="noindex,nofollow"', self.html)
        self.assertIn("@media (max-width: 760px)", self.html)


if __name__ == "__main__":
    unittest.main()
