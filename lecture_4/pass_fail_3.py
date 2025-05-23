# Data
scores = [88, 38, 45, 55, 65, 78, 92, 12, 37, 80, 82, 45, 89, 32]

# Categorize scores into Pass (>=50) and Fail (<50)
pass_scores = []
for student_score_single in scores:
    if student_score_single >= 50:
        pass_scores.append(student_score_single)

# Print passing scores
for score in pass_scores:
    print(score)