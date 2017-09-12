import unittest
import grade as gd

class TestGrade(unittest.TestCase):

    def test_49(self):
        grade = gd.grade(49)
        self.assertEqual(grade, "Fail")

    def test_50(self):
        grade = gd.grade(50)
        self.assertEqual(grade, "Pass")

    def test_51(self):
        grade = gd.grade(51)
        self.assertEqual(grade, "Pass")

    def test_69(self):
        grade = gd.grade(69)
        self.assertEqual(grade, "Pass")

    def test_70(self):
        grade = gd.grade(70)
        self.assertEqual(grade, "Credit")

    def test_71(self):
        grade = gd.grade(71)
        self.assertEqual(grade, "Credit")

    def test_79(self):
        grade = gd.grade(79)
        self.assertEqual(grade, "Credit")

    def test_80(self):
        grade = gd.grade(80)
        self.assertEqual(grade, "Distinction")

    def test_81(self):
        grade = gd.grade(81)
        self.assertEqual(grade, "Distinction")

    def test_84(self):
        grade = gd.grade(84)
        self.assertEqual(grade, "Distinction")

    def test_85(self):
        grade = gd.grade(85)
        self.assertEqual(grade, "High Distinction")

    def test_86(self):
        grade = gd.grade(86)
        self.assertEqual(grade, "High Distinction")
