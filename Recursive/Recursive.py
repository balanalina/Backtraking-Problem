
def consistent(x,m):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i] == x[j]:
                return False
    for i in range(len(x)-1):
        if abs(x[i]-x[i+1]) <m:
            return False
    return True


def solution(k,n):
    return k == n  

def solutionFound(x):
    print(x)

def backTrackRecursive(x, perm, n, k,m,nr):
    if solution(k,n):
        if consistent(perm,m):
            solutionFound(perm)
            nr =  1
    else:
        for i in x:
            perm[k] = i
            nr = backTrackRecursive(x, perm, n, k+1,m,nr)
    return nr



