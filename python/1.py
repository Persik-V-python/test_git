 n = int(input())
b = []
b2 = []
count = len(b)
while(n!=0 and count < 999 and n <= 30000):
    b.append(n)
    n = int(input())
    count = len(b)
for i in range(-1,len(b)-1):
    if b[i]%5 == 0:
        b2.append(b[i])
print(len(b2))
