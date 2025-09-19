# grade_evaluator.py

# Ask user for name and score
name = input("Enter your name: ")
score = float(input("Enter your score (0-100): "))

# Determine grade using if-elif-else
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"

# Print the result
print(f"\nStudent: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")