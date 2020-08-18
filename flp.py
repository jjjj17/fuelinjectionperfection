def solution(s):
    counter = 0
    num = int(s)
    while num != 1:
        if num&1 == 1:
            if ((num+1&num) > (num-1&num-2)) or num == 3:
                num -= 1
                counter += 1
            else:
                num += 1
                counter += 1
        elif num&1 == 0:
            num = num >> 1
            counter += 1
    else:
        return(counter)

print(solution("3"))