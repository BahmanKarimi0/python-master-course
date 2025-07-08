"""
Mini‑Project – Student Score Analyzer & Scholarship Checker
Chapter 04 (Conditionals)
"""
try:
    while (name := input("Enter your name: ").strip()) == '':
        print("⚠️  Name cannot be empty.")
    while (average_score := float(input("Enter your average score (0-20): ").strip())) > 20 or average_score < 0:
        print("⚠️  average score is invalid [average score : 0-20]")
    while (discipline_score := float(
            input("Enter your discipline score (0–100): ").strip())) > 100 or discipline_score < 0:
        print("⚠️  discipline score is invalid [discipline score : 0-100]")
    while (extra_activity := input("Are you have extra activity [yes / no]: ").casefold()) not in ["yes", "y", "no",
                                                                                                   "n"]:
        print("⚠️  extra activity is invalid [extra activity : (yes/no)]")
    scholarship = average_score >= 17 and discipline_score >= 90 and extra_activity in ['yes', 'y']
    accept = average_score >= 10
    if accept and scholarship:
        print(f'{name} – Passed (avg: {average_score}) – 🏅 Scholarship awarded')
    elif accept and not scholarship:
        print(f'{name} – Passed (avg: {average_score}) – No scholarship')
    else:
        print(f'{name} – Failed (avg: {average_score})')
except ValueError:
    print("Please enter valid input.")
