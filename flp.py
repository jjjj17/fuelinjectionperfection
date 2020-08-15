import math

def solution(n):
    result = n
    counter = 0
    while result != 1:
        power = int(math.log (result,2) + 0.5)
        if result%2 == 0:
            result = result/2
            counter += 1
        elif result%2 != 0:
            r1 = result-1
            r2 = result+1
            if 2 ** power == r2:
                result = r2
                counter += 1
            else:
                result = r1
                counter += 1
    else:
        return(counter)


#el 3 está malo

print(solution(4))
