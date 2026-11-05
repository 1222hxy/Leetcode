def t(l1,l2):
    num1 = 0
    num2 = 0
    for x in range(len(l1)):
        bs = 10 ** x
        num1 += bs * l1[x]

    for y in range(len(l2)):
        bs = 10 ** y
        num2 += bs * l2[y]
    print(num1,num2)
    return [int(num) for num in str(num1+num2)][::-1]

print(t([9,9,9,9,9,9,9],[9,9,9,9]))