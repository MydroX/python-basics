num = 9119

squares = []

for digit in str(num):
    squares.append(str(int(digit) ** 2))

print(int(''.join(squares)))

# def square_digits(num):
#    ret = ""
#    for x in str(num):
#        ret += str(int(x)**2)
#    return int(ret)
