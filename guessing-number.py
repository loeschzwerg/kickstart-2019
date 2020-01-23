def IO_operation(x: int):
    print(x)
    return input()


def guess(a, b):
    '''selects the ceiling average of (a,b]'''
    return int(a + (b-a)/2)


def guessing_round():
    '''
    Adjusts boundaries a and b for a simple O(log(n)) binary search.
    WRONG_ANSWER can only be received, when choosing between (a, a+1]
    '''
    a, b = [int(x) for x in input().split()]
    n = int(input())
    x = guess(a,b)
    answer = IO_operation(x)
    for tries in range(n):
        if 'TOO_SMALL' in answer: 
            a = x + 1
        elif 'TOO_BIG' in answer:
            b = x - 1
        elif 'WRONG_ANSWER' in answer:
            b += 1
        else: # also 'CORRECT'
            break
        x = guess(a, b)
        answer = IO_operation(x)


if __name__ == "__main__":
    testcases = int(input())
    for tc in range(testcases):
        guessing_round()
