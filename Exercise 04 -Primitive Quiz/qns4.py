# making a dictionary with new questions and correct answers
country_quiz = {
    "What is the capital of Japan?": "tokyo",
    "What is the capital of Canada?": "ottawa",
    "What is the capital of Australia?": "canberra",
    "What is the capital of India?": "new delhi",
    "What is the capital of Brazil?": "brasilia",
    "What is the capital of South Korea?": "seoul",
    "What is the capital of Egypt?": "cairo",
    "What is the capital of Argentina?": "buenos aires",
    "What is the capital of Kenya?": "nairobi",
    "What is the capital of Turkey?": "ankara"
}

# greeting message
print("Hey! Let's try a new capital cities quiz 😄")

# going through each question in the dictionary
for qn, right_ans in country_quiz.items():
    # asking the user the question
    user_reply = input(qn + " ")

    # checking the user's answer (ignoring uppercase/lowercase)
    if user_reply.strip().lower() == right_ans:
        print("✅ Correct!\n")
    else:
        print(f"❌ Wrong! The correct answer is {right_ans.title()}.\n")

# ending message
print("Quiz finished! Good job 🎉")
