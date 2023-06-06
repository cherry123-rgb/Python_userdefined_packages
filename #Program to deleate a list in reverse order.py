#Program to deleate a list in reverse order

l = [int(input()) for i in range(int(input("Enter the length of list")))]
print(l)

for i in range(len(l)-1,-1,-1):
    print(l.pop(i))
print(l)