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
        self.assertIn('"openclaw"', contents)
        self.assertIn('"primaryEnv":"MDTERO_API_KEY"', contents)
        self.assertIn('"env":["MDTERO_API_KEY"]', contents)
        self.assertIn('"envVars"', contents)
        self.assertIn('"name":"MDTERO_API_KEY"', contents)
        self.assertIn('"description":"Required for Mdtero API authentication."', contents)
        self.assertIn('"required":true', contents)
        self.assertIn('"name":"ELSEVIER_API_KEY"', contents)
        self.assertIn('"description":"Optional. Helps local Elsevier or ScienceDirect acquisition on the user\'s machine."', contents)
        self.assertIn('"required":false', contents)
        self.assertIn("MDTERO_API_KEY", contents)
        self.assertIn("POST /tasks/parse", contents)
        self.assertIn("POST /tasks/translate", contents)
        self.assertIn("paper_md", contents)
        self.assertIn("paper_pdf", contents)
        self.assertIn("translated_md", contents)
        self.assertIn("PDF is an optional artifact", contents)
        self.assertIn("Elsevier", contents)
        self.assertIn("browser extension", contents)
        self.assertIn("download the helper installer, review it locally, then run it", contents)
        self.assertIn("https://mdtero.com/guide", contents)
        self.assertIn("https://mdtero.com/account", contents)
        self.assertIn("keyword discovery and API-key management stay in Mdtero Account", contents)
        self.assertIn("ClawHub install only sets up the agent skill", contents)
        self.assertIn("does not install the local helper", contents)
        self.assertIn("Parse and translate requests send paper content", contents)
        self.assertIn("sensitive or proprietary manuscripts", contents)
        self.assertIn("ELSEVIER_API_KEY", contents)
        self.assertIn("does not enable direct server-side `POST /tasks/parse`", contents)
        self.assertIn("POST /tasks/parse-helper-bundle-v2", contents)
        self.assertIn("POST /tasks/parse-fulltext-v2", contents)
        self.assertIn("helper_bundle", contents)
        self.assertIn("install_mdtero_helper.sh", contents)
        self.assertIn("result.artifacts.paper_md.path", contents)
        self.assertNotIn("| sh", contents)
        self.assertNotIn('"/absolute/path/from/paper_md"', contents)

    def test_readme_explains_clawhub_publish_flow(self):
        contents = README.read_text(encoding="utf-8")

        self.assertIn("ClawHub", contents)
        self.assertIn("skills/mdtero/SKILL.md", contents)
        self.assertIn("Chrome Web Store", contents)
        self.assertIn("chromewebstore.google.com/detail/mdtero/knpihhcooldgedbklgjghebijcpejibp", contents)
        self.assertIn("Microsoft Edge", contents)
        self.assertIn("python3 -m unittest discover -s tests -v", contents)
        self.assertIn("clawhub login", contents)
        self.assertIn("clawhub --workdir . publish skills/mdtero", contents)
        self.assertIn("OpenClaw", contents)
        self.assertIn("Account", contents)
        self.assertIn("POST /tasks/parse-helper-bundle-v2", contents)
        self.assertIn("install_mdtero_helper.sh", contents)


if __name__ == "__main__":
    unittest.main()
