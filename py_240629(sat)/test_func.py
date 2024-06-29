def sum(num):   #test1_1
    total = 0
    for i in range(1, num+1):
        total += i
    return total

def pyramid(num):   #test1_2
    print("print")
    for i in range(0, num, 1):
        for j in range(num-1-i, 0, -1):         #여기서 선생님은 range(num-(i+1)) 이런식으로 하셨다.
            print(" ", end="")
        for j in range(0, 2*i+1, 1):
            print("*", end="")
        print()

def diamond(num): #얜 피라미드하고나서 추가적으로 내가 그냥 해본거.
    print("print")
    for i in range(0, num, 1):
        for j in range(num-1-i, 0, -1):
            print(" ", end="")
        for j in range(0, 2*i+1, 1):
            print("*", end="")
        print()
    for i in range(0, num, 1):
        for j in range(0, i+1, 1):
            print(" ", end="")
        for j in range((2*num-3)-2*i, 0, -1):
            print("*", end="")    
        print()

def square_subt(x, y):  #test1_3
    return x**2 - y**2
    # return pow(x, 2) - pow(y, 2) 이렇게해도되고
    # return (num1*num1)-(num2*num2) 이렇게 해도된다. 편한대로 하면됨.




