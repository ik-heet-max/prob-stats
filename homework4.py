import math


print("Задача 1")


A = 200
B = 800
mean_uni = (A + B) / 2
variance_uni = ((B - A) ** 2) / 12
print(f"Mean = {mean_uni}\nVariance = {variance_uni}")


print("Эадача 2")


VAR = 0.2
A = 0.5
B = math.sqrt(12 * VAR) + A
print(f"Right bound equals {round(B, 2)}")


print("Задача 3")


VAR = math.sqrt(32 / 2)
print(f"Mu equals -2, variance equals {VAR}")


print("Эадача 4")
# Mean = 174, variance = 8
P1 = 0.683
P2 = 0.955
P3 = 0.997

print(f"Probability height lies above 182 equals {0.5 - (P1 / 2)}")
print(f"Probability height lies above 190 equals {0.5 - P2 / 2}")
print(f"Probability height lies between 166 and 190 equals {(P1 + P2) / 2}")
print(f"Probability height lies between 166 and 182 equals {P1}")


print("Задача 5")
print((190 - 178) / math.sqrt(25))