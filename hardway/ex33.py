


####################################

def do_while(n, a):
    i = 0
    numbers = []
    while i < n:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += a
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")
    for num in numbers:
        print(num)

do_while(8,2)