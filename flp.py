import math

def solution(n):
    result = int(n)
    counter = 0
    while result != 1:
        if result%2 == 0:
            result = result/2
            counter += 1
        elif result%2 != 0:
            r1 = result-1
            r2 = result+1
            if (math.log(r2, 2).is_integer() and math.log(r1, 2).is_integer() == False):
                result = r2
                counter += 1
            else:
                result = r1
                counter += 1
    else:
        return(counter)


#el 3 está malo

print(solution("1213254654561325851545454545454545122165465465445645641513213213213213246545415646547871213254654561325851545454545454545122165465465445645641513213213213213246545415646547871213254654561325851545454545454545122165465465445645641513213213213213246545415646547871213254654561325851545454545454545122165"))