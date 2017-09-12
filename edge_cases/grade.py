import sys

def grade(score: int) -> str:
    """
    Determine a name grade from a score out of 100
    """

    grade = "Fail"

    if 50 < score < 70:
        grade = "Pass"

    if 70 < score < 80:
        grade = "Credit"

    if 80 < score < 85:
        grade = "Distinction"

    if 85 < score:
        grade = "High Distinction"

    return grade


if __name__ == "__main__":
    score = int(sys.argv[0])
    print(grade(score))
