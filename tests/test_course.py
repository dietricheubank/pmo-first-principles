import json
import unittest
from pathlib import Path
from assess import evaluate, DOMAINS

ROOT=Path(__file__).resolve().parents[1]

class CurriculumTests(unittest.TestCase):
    def test_course_complete(self):
        lessons=json.loads((ROOT/"lessons.json").read_text())
        self.assertEqual(len(lessons),10)
        self.assertEqual([x["id"] for x in lessons],list(range(1,11)))
        for item in lessons:
            self.assertTrue(all(item.get(k) for k in ("title","principle","scenario","exercise","question")))
            self.assertEqual(len(item["choices"]),3)
            self.assertIn(item["answer"],range(3))

    def test_assessment(self):
        scores={d:3 for d in DOMAINS}
        result=evaluate(scores)
        self.assertEqual(result["stage"],"Developing")
        self.assertEqual(len(result["focus"]),3)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            evaluate({"Outcomes":5})
        with self.assertRaises(ValueError):
            evaluate({d:0 for d in DOMAINS})

if __name__=="__main__":
    unittest.main()
