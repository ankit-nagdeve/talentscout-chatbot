
def get_tech_questions(tech_stack):
    techs = [t.strip().lower() for t in tech_stack.split(",")]
    questions = []
    for tech in techs:
        if tech == "python":
            questions.append("Q1: What are Python's key features?")
            questions.append("Q2: Explain list comprehension with an example.")
        elif tech == "django":
            questions.append("Q3: What is Django ORM?")
            questions.append("Q4: How does Django handle forms?")
        elif tech == "javascript":
            questions.append("Q5: Difference between == and === in JS?")
        else:
            questions.append(f"Q: What are your experiences with {tech}?")
    return questions
