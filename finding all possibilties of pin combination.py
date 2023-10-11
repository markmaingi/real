from typing import List  # our variables

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

# finding the combinations
possible_list: list[int] = [a, b, c, d]

for i in range(0 ):
    for j in range(0 ):
        for k in range(0 ):
            for l in range(0):
                if (i != j, i != k, i != l, j != k, j != l, k != l):
                    print("{} {} {} {}".format(possible_list[i], possible_list[j], possible_list[k], possible_list[l]))
