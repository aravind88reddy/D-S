billAmount = list(input())
int(billAmount)
count = 0
for i in billAmount:
    if i/2 == 1:
        count= count + 1
    else:
        continue
print(billAmount)
