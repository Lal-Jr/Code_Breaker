import random

def get_guess():
    user_code = input("What is the code?")
    return list(user_code)

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED"

    clues =[]
    for index,num in enumerate(user_guess):
        if num == code[index]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome To CODE BREAKER")
secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("Here is the report of your guess:")
    for clue in clue_report:
        print(clue)
        


