score1 = float(input("Enter your score: "))
score2 = float(input("Enter your second score: "))
score3 = float(input("Enter your third score: "))
average = (score1 + score2 + score3) / 3

print(f"The average score is", average )

if average > 95:
    print("congratulations!")
    print("That is a great average!")