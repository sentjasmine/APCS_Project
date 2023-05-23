# create two random numbers and add them together

import random
import time

class Main:
    first = 0
    second = 0
    add = 0
    answer = 0
    starttme = time.time()
    timeduration = 5
    
    def addition(self):
        attempts = 0
        counter = 0
        while counter<=10:
            first = random.randint(1,10)
            second = random.randint(1,10)
            answer = first + second
            answer_input = input(str(first) + " + " + str(second) +": ")
            if str(answer) == answer_input:
                counter += 1
            else:
                print("That is not the right answer. Try again")
                attempts += 1
                break
    
    def timer5(self):
        
            
            
