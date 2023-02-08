import numpy as np
""" Game to guess the number.
    Computer chooses and guess the number by itself"""

def random_predict(number:int=1) -> int:
    """Guess the number randomly
    args:
        number(int, optinol): guessed number
     returns:
        int: number of tries""" 
    
    count = 0
    
    while True:
        count +=1
        predict_number = np.random.randint(1, 101) #guessed number
        if number == predict_number:
            break #end of cycle if guessed
    return(count)
print(f"Number of tries:{random_predict()}")

def score_game(random_predict) -> int:
    """How many tries from 1000 in average our algorithm guesses
    args: 
       random_predict([type]): guess functon
    returns:
       int: average number of tries"""
       
    count_ls = [] #list for saving numbers of tries
    np.random.seed(1) #fix seed for play
    random_array = np.random.randint(1,101, size=(1000))
       
    for number in random_array:
        count_ls.append(random_predict(number))
           
        score = int(np.mean(count_ls)) #find avarage number of tries
           
        print(f"Your algorithm guesses the number at average for: {score} tries")
        return(score)
    #RUN
    if __name__ == "_main_":
       score_game(random_predict) 

    