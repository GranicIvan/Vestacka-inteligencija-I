"""
Bulls and Cows

Problem Description:
    You are playing the Bulls and Cows game with your friend.
    You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
    Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls. 
    Given the secret number and your friend's guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Problem Constraints:
    1 <= secret.length, guess.length <= 100000
    secret.length == guess.length
    secret and guess consist of digits only.

Example Input:
    Input 1:
    secret = "1807", guess = "7810"
    Input 2:
    secret = "1123", guess = "0111"

Example Output:
    Output 1:
    "1A3B"
    Output 2:
    "1A1B"
"""

# @param A : string
# @param B : string
# @return a strings
def solve(a, b):
    bull = 0 #oba tacna
    cow = 0 #samo br tacan
    if len(a) != len(b):
        print("Stringovi nisu iste duzine!!!")
    else:
        i=0
        while i < len(a):            
            if a[i] == b[i]:                
                a = a[:i] + a[i+1:]               
                b = b[:i] + b[i+1:]                
                i = i - 1
                bull = bull + 1
                
            i = i + 1    

        br_a = [0]*10
        br_b = [0]*10
        i = 0

        while i < len(a):
            br_a[int(a[i])] = br_a[int(a[i])]+1
            br_b[int(b[i])] = br_b[int(b[i])]+1
            i = i + 1            
       

        i = 0
        while i < 10:
           
            while br_a[i] > 0 and br_b[i] > 0:
                cow = cow + 1        

                br_a[i] = br_a[i] - 1
                br_b[i] = br_b[i] - 1
            i = i + 1
      

    
    rez = str(bull),"A",str(cow),"B"
    rez = "".join(rez)
    return rez


if __name__ == "__main__":
    print(solve("1807", "7810"))
    #print(solve("12398712", "12378921"))
    #print(solve("6020943525972", "7157627311068"))
   