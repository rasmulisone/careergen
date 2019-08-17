import random
careerend = random.randint(2012, 2015)
retirementage = random.randint(36, 39)
birthyear = careerend - retirementage
careerstart = birthyear + random.randint(17, 19)
careerlength = careerend - careerstart
clubs = int(input("Number of club spells: "))
length = 0
while length != careerlength:
    year = careerstart
    for i in range(clubs):
        exec("start" + str(i) + " = year")
        exec("length" + str(i) + " = random.randint(1, 6)")
        exec("end" + str(i) + " = start" + str(i) + " + length" + str(i))
        exec("year = end" + str(i))
    exec("length = end" + str(clubs - 1) + " - careerstart")
print("Birth year: " + str(birthyear))
print("Career start: " + str(careerstart))
print("Career end: " + str(careerend) + " (age " + str(retirementage) + ")")
print("Career length: " + str(careerlength))
for i in range(clubs):
    exec("print('" + str(i) + ": ' + str(start" + str(i) + ") + '-' + str(end" + str(i) + "))")
