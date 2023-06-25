if __name__ == '__main__':
    #GETTING THE INPUT
    n = int(input())
    #I ADD N + 1 IN RANGE() BECAUSE THE NUMBER WE WOULD GET FROM THE INPUT IS ALWAYS 1 NUMBER BELOW, SO TO GET THE EXACT NUMBER, I PUT +1
    for numbers in range(1, n + 1):
    #(end="") IS WHEN I WANT TO PRINT IN 1 LINE. IT'S POSSIBLE TO USE (end=" ") TO PUT SPACES IN BETWEEN EACH NUMBER IN 1 LINE
        print(numbers, end="")
