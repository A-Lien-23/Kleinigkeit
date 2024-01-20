from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')
player = Eq(1*x + 1*y + 1*z, 110)
enemy1 = Eq(1*x - 1*y - 1*z, 0)
enemy2 = Eq(0*x + 4*y - 7*z, 0)

solution = solve((player, enemy1, enemy2), (x, y, z))

print("~ Сопротивление эффектам ~")
print("Отравление:", solution[x], "%")
print("Заморозка:", solution[y], "%")
print("Горение:", solution[z], "%")
