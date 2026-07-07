print("     GENERAL KNOWLEDGE QUIZ")
questions = [
    "1. Which country is known as the Land of the Rising Sun?",
    "2. How many days are there in a leap year?",
    "3. Which is the smallest planet in the Solar System?",
    "4. Who wrote the Indian National Anthem?",
    "5. Which device is used to measure temperature?"
]

options = [
    ["A. China", "B. Japan", "C. India", "D. Korea"],
    ["A. 365", "B. 364", "C. 366", "D. 367"],
    ["A. Mars", "B. Mercury", "C. Venus", "D. Earth"],
    ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Jawaharlal Nehru", "D. Bankim Chandra Chatterjee"],
    ["A. Barometer", "B. Thermometer", "C. Hygrometer", "D. Ammeter"]
]

answers = ["B", "C", "B", "A", "B"]

score = 0

for i in range(5):
    print("\n" + questions[i])

    for option in options[i]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == answers[i]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", answers[i])
print("           QUIZ COMPLETED")

print("Your Score:", score, "/5")

percentage = (score / 5) * 100
print("Percentage:", percentage, "%")

if score == 5:
    print("Outstanding!")
elif score == 4:
    print("Very Good!")
elif score == 3:
    print("Good Job! ")
elif score == 2:
    print("Keep Learning! ")
else:
    print("Better Luck Next Time! ")

print("\nThank you for playing the quiz!")