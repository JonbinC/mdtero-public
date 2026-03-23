import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "mdtero" / "SKILL.md"
README = ROOT / "README.md"


class ClawHubPackageTests(unittest.TestCase):
    def test_skill_bundle_exists(self):
        self.assertTrue(SKILL.exists(), "expected skills/mdtero/SKILL.md to exist")

    def test_skill_bundle_contains_public_openclaw_guidance(self):
        contents = SKILL.read_text(encoding="utf-8")

        self.assertIn("name: mdtero", contents)
        self.assertIn("description:", contents)
        self.assertIn("MDTERO_API_KEY", contents)
        self.assertIn("POST /tasks/parse", contents)
        self.assertIn("POST /tasks/translate", contents)
        self.assertIn("paper_md", contents)
        self.assertIn("translated_md", contents)
        self.assertIn("PDF is optional input", contents)
        self.assertIn("Elsevier", contents)
        self.assertIn("browser extension", contents)
        self.assertIn("download it, review it, then run it", contents)
        self.assertIn("result.artifacts.paper_md.path", contents)
        self.assertNotIn("| sh", contents)
        self.assertNotIn('"/absolute/path/from/paper_md"', contents)

    def test_readme_explains_clawhub_publish_flow(self):
        contents = README.read_text(encoding="utf-8")

        self.assertIn("ClawHub", contents)
        self.assertIn("skills/mdtero/SKILL.md", contents)
        self.assertIn("python3 -m unittest discover -s tests -v", contents)
        self.assertIn("clawhub login", contents)
        self.assertIn("clawhub publish ./skills/mdtero", contents)


if __name__ == "__main__":
    unittest.main()
