from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')
r = 80
ur_1 = Eq(2*x + 3*y - 1*z, r)
ur_2 = Eq(4*x - 1*y - 2*z, r)
ur_3 = Eq(1*x + 2*y + 3*z, r)

solution = solve((ur_1, ur_2, ur_3), (x, y, z))

print("~ Бонусы уровня репутации", r, "~")
print("Скидка у бродячих торговцев:", round(solution[x]), "%")
print("Бонус к вероятности удачных переговоров:", "+", round(solution[y]), "%")
print("Множитель награды за задания:", "х", round(solution[z]))
