x = int(input())
a = 0
i = 0
b = 0
c = 0
menor_num = 0

while i < x:
    num = int(input())
    if num >= a:
        maior_num = num
    else:
        c = num
    if num < c:
        menor_num = num
    elif num <= b:
        menor_num = num
    a = maior_num 
    b = menor_num
    i += 1
print(f"{maior_num} e {menor_num}")
    