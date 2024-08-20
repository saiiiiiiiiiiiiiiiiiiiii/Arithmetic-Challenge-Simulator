import random
import time
operators = ["+", "-", "*", "/"]
min_operand = 3
max_operand = 12 
total_problems = 10
correct_Ones = 0
Incorrect_ones = 0
def generate_problem():
  left = random.randint(min_operand, max_operand)
  right = random.randint(min_operand, max_operand)
  operator = random.choice(operators)
  expression = str(left) + " " +  operator + " " +  str(right)
  expression = float(expression)
  answer = eval(expression) # The eval() function in Python is used to evaluate a string-based expression as a Python expression. This means you can pass a string containing Python code to eval(), and it will execute that code and return the result.
  # Yes, that's correct! The eval() function can take a string that represents a Python expression (such as a mathematical operation, a function call, or even a variable) and evaluate it as if it were an actual piece of Python code. If the expression evaluates to a number, eval() will return that number.
  return(expression, answer)



press_enter_to_start = input("Press Enter to start")
print("------------------------------------------------------------")
start_time = time.time()

for i in range(total_problems):
  expression, answer = generate_problem()
  print(f"Question {i+1}: {expression}")
  user_answer = input("Enter your answer: ")
  if float(user_answer) == answer:
    print("Correct!")
    correct_Ones += 1
  else:
      print(f"Sorry, that's incorrect. The correct answer was {answer}.")
      Incorrect_ones += 1

end_time = time.time()  
total_time = round(end_time - start_time, 2)

print("--------------------------------------------------------------------")
print(f"Nice Work You finished in total {total_time} seconds")
print(f"You got {correct_Ones} correct and {Incorrect_ones} incorrect")

