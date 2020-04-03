"""
Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to
n, such that between any two numbers on consecutive positions, the difference in absolute value is at
least m. If there is no solution, display a message.
"""
def consistent(x,m):
    if len(x) == 1:
        return len(x) == len(set(x))
    return len(x) == len(set(x)) and abs(x[len(x)-1] - x[len(x)-2])>=m

def solution(x,n):
    return len(x) == n

def solutionFound(x):
    print(x)
    return 1
    

def backTrackIterative(n,m):
    x = [0]
    nr = 0
    while len(x) > 0:
        chosen = False
        while not chosen and x[len(x) - 1] < n:
            x[len(x) -1] += 1
            chosen = consistent(x,m)
        if chosen:
            if solution(x,n):
                nr = solutionFound(x)
            else:
                x.append(0)
        else:
            x = x[:-1]
    if nr == 0:
        print("There is no solution! ")
            
