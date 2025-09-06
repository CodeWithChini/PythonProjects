import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERANDS = 3
MAX_OPERANDS = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong_answers = 0
input("Press Enter to start the quiz...")

print("----------------------------------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer =  generate_problem()
    while True:
        guess = input("problem #" + str(i + 1)+ " : " + expr + " = ")
        if guess.lower() == str(answer):
            break
        wrong_answers += 1

end_time = time.time()
total_time = end_time - start_time

print("----------------------Results----------------------")
print("You got " + str(TOTAL_PROBLEMS - wrong_answers) + " out of " + str(TOTAL_PROBLEMS) + " correct.")
print("You took " + str(round(total_time, 2)) + " seconds to complete the quiz.")
print("You had " + str(wrong_answers) + " wrong answers.")

print("Goodbye!")
