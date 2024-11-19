t = 1
sumtotal = 0
n = 1

while t > 0.000000000001:
    t = 1/n**2
    n += 1
    sumtotal += t

print(sumtotal)

quit()