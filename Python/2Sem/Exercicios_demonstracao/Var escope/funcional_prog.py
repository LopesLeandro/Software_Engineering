calctab2 = lambda num1,num2: num1 * num2
print(calctab2(7, 6))
othercrazyfunction = calctab2
print(othercrazyfunction(7, 6))


def gerartabuada(numero, regra):
    for i in range(11):
        print(numero, "x", i, "=", regra(numero, i))
gerartabuada(7, calctab2)

def calctab(num1:int, num2:int):
    return num1 * num2

res = calctab(7, 9)
print(res)

