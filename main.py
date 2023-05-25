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
    attempts = 0
    counter = 0    
   
    
    while counter<=40:
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
            if counter == 10:
                while counter <=19:
                    first = random.randint(1,10)
                    second = random.randint(1,10)
                    answer = first - second
                    answer_input = input(str(first) + " - " + str(second) +": ")
                    if str(answer) == answer_input:
                        counter += 1
                    else:
                        print("That is not the right answer. Try again")
                        attempts += 1
                        break
                    if counter == 19:
                        while counter <=28:
                            first = random.randint(1,10)
                            second = random.randint(1,10)
                            answer = first * second
                            answer_input = input(str(first) + " x " + str(second) +": ")
                            if str(answer) == answer_input:
                                counter += 1
                            else:
                                print("That is not the right answer. Try again")
                                attempts += 1
                                break
                            if counter == 28:
                                while counter <=37:
                                    first = random.randint(1,10)
                                second = random.randint(1,10)
                                answer = first % second
                                answer_input = input(str(first) + " % " + str(second) +": ")
                                if str(answer) == answer_input:
                                    counter += 1
                                else:
                                    print("That is not the right answer. Try again")
                                    attempts += 1
                                    break
                                if counter == 37:
                                    print("You've won, congrats!")
            
  
    
  
