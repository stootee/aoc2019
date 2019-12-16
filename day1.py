from inputs.day1 import inp


def fuel_calc(mass):
    return int(int(mass) / 3) - 2


cnt = 0

for x in inp.splitlines():
    y = int(x)
    y = fuel_calc(y)
    cnt += y

print(cnt)


## part 2

cnt = 0

for x in inp.splitlines():
    y = int(x)

    while True:
        y = fuel_calc(y)
        if y > 0:
            cnt += y
        else:
            break

print(cnt)
