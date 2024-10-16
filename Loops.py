greeting ="good morning"
if greeting== "god morning":
    print("pass")
else:
    print("fail")

#forloop
obj=[1,2,3,4]
for i in obj:
    print(i)

sum1=0
for j in range(1,6):
    sum1=sum1+j
print(sum1)

for m in range(1,10,2):
    print(m)

#while loop
print("********************")
it=10
while it>1:
    if it==7:
        continue
    if it==3:
        break
    print(it)
    it=it-1
print("done")

