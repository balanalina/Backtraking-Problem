from Iterative.Iterative import backTrackIterative
from Recursive.Recursive import backTrackRecursive

def UI():
    n = int(input("Enter the integer n: "))
    m = int(input("Enter the integer m: "))
    k = False
    while not k:
        command = input("Choose the method: iterative or recursive:  ")
        if command == "iterative":
            backTrackIterative(n, m)
            k = True
        elif command == "recursive":
            k = True
            l = []
            for i in range(n):
                l.append(i+1)
            perm = [0]* len(l)
            nr = 0
            nr = backTrackRecursive(l, perm, n, 0,m,nr)
            if nr != 1:
                print("There is no solution! ")
        else:
            print("Invalid input!")