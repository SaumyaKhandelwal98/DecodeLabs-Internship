roles = {
    "Data Scientist": ["python", "machine learning", "sql", "statistics"],
    "AI Engineer": ["python", "machine learning", "deep learning"],
    "Web Developer": ["html", "css", "javascript"],
    "Backend Developer": ["python", "sql", "api"],
    "Data Analyst": ["excel", "sql", "python"]
}

print("=" * 50)
print("      AI CAREER RECOMMENDATION SYSTEM")
print("=" * 50)

skills = input("\nEnter your skills (comma separated): ").lower().split(",")

skills = [skill.strip() for skill in skills]

scores = {}

for role, role_skills in roles.items():
    match = len(set(skills) & set(role_skills))
    scores[role] = match

sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\nRecommended Career Paths:\n")

found = False

for role, score in sorted_roles:
    if score > 0:
        print(f"{role:<20} : {score} matching skills")
        found = True

if not found:
    print("No matching career path found.")
    print("Try skills such as: python, sql, machine learning")
