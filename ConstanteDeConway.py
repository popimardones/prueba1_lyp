import re
x = "1"
print(x)
for n in range(10):
    x="".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])
    print(x)



