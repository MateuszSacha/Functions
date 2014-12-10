# Mateusz Sacha
# functions improvement exercise
# times-table tester
#import random

# main program
#print("Times-table tester")
#print()
#testTable = int(input("Which times-table do you want to be tested on? "))
#for questions in range(1,6):
    #Num1 = testTable
    #Num2 = random.randrange(2,13)
    #Ans = Num1 * Num2
   # UserAnswer = int(input(str(Num1) + ' x ' + str(Num2) + ' = ? '))
    #if UserAnswer == Ans:
      #  print('Well done, you got the correct answer!')
     #   print()
   # else:
     #   print('Sorry, you got the answer wrong. The correct answer is',Ans)
     #   print()
              
def test_table_check():
    test_table = get_times_table()
    random_number, ans = generate_question(test_table)
    random_number = generate_random_number()
    ans = generate_the_answer(test_table, random_number)
    
def get_times_table():
    test_table = int(input("Which times-table do you want to be tested on?"))
    return test_table

def generate_question(test_table):
    random_number = generate_random_number()
    ans = generate_the_answer(test_table, random_number)
    return random_number, ans

def generate_random_number():
    import random
    random_number = random.randrange(1,13)
    return random_number

def generate_the_answer(test_table, random_number):
    ans = test_table * random_number
    return ans

def ask_question(test_table, random_number, ans):
    user_answer = int(input(str(test_table) + ' x ' + str(random_number) + ' = ? '))
    check_the_answer(ans, user_answer)

def check_the_answer(ans, user_answer):
    if user_answer == ans:
        print('Well done, you got the correct answer!')
    else:
        print('Sorry, you got the answer wrong. The correct answer is',ans)

test_table_check()
    


