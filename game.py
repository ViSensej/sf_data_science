#game to guess the number
import numpy as np
number = np.random.randint(1,101) #choose the number
count = 0

while True:
    count +=1
    predict_number = int(input("Guess number from 1 to 100:"))                          
    
    if predict_number > number:
        print("The number should be less!")
    elif predict_number < number:
        print("The number should be more!")
    else:
        print(f"You have guessed this number! This is 60{number}, for {count} counts!")
        break #end of the gams and cycle
    