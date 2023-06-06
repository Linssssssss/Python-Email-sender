quiz = {
    "question1": {
        "question": "What is the capital of Kenya?",
        "answer": "Nairobi"
    },
    "question2": {
        "question": "What is the capital of South Korea?",
        "answer": "Seoul"
    },
    "question3": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question4": {
        "question": "What is the capital of South Africa?",
        "answer": "Pretoria"
    },
    "question5": {
        "question": "What is the capital of Monaco?",
        "answer": "Monaco-Ville"
    },
    "question6": {
        "question": "What is the capital of Tanzania?",
        "answer": "Dodoma"
    },
    "question6": {
        "question": "What is the capital of Rwanda?",
        "answer": "Kigali"
    },
    "question7": {
        "question": "What is the capital of Seychells?",
        "answer": "Victoria"
    },
    "question8": {
        "question": "What is the capital of Greece?",
        "answer": "Athens"
    },
}


score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 8 questions correctly")
print("Your percentage is " + str(int(score/8 * 100)) + "%")
