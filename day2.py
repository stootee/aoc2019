from inputs.day2 import inp

# inp = "1,9,10,3,2,3,11,0,99,30,40,50"

inp = list(map(int, inp.split(",")))
print(inp)


def operate(operators):
    a = inp[operators[1]]
    b = inp[operators[2]]
    c = operators[3]

    if operators[0] == 1:
        d = a + b
    elif operators[0] == 2:
        d = a * b
    else:
        print("oh oh spaghetti-os")
        raise

    inp[c] = d

inp[1] = 12
inp[2] = 2

posn = 0

while inp[posn] != 99:
    ops = inp[posn:posn + 4]
    print(ops)
    operate(ops)
    posn += 4

print(inp)