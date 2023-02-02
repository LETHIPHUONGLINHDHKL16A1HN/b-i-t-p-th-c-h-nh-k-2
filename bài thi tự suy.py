#tìm số nhỏ nhất lớn nhất               
a=int(input("so a"))                 a=int(input("so a"))
b=int(input("so b"))
c=int(input("so c"))
d=int(input("so d"))
g=0                                       g=0 h=0 while(g<a)or (g<b)or  g+=1 g=h  
h=0
while(g<a) or (g<b)or(g<c)or (g<d):
    g+=1
    h=g
while(h>a)or (h>b)or (h>c)or (h>d):
    h-=1
print("max=",g)
print("min=",h)

#tinh tong so n nguyen
a=int(input("nhap n"))
k=0
while a>0:
    print("nhap so thu",a)
    h=int(input())
    k=k+h
    a-=1
    if a==0:
        print("tong cac so hang",k)
        break
    
#tinh tong cac so nguyen
h=1
k=0
while h!=0:
    h=eval(input("nhap h"))
    k=k+h 
    if (h==0):
        print("tong cac so hang",k)
        
#tim ucln
a=int(input("nhap a"))
b=int(input("nhap b"))
c=2
while(a%c!=0)or (b%c==0):
    c+=1
    if (a%c==0)and(b%c==0):
        print(c,"la uoc chung nho nhat")
        break
    if c>b and c>a :
        print ("khong co uoc chung nho nhat")
        break
    
#kiem tra so nguyen to
b=int(input("nhap so"))
c=1
h=0
while c<b:
    if (b%c==0):
        h=h+c
        print(h)
    c+=1
if h==b:
    print(b,"la so hoan hao")
else:
    print(b,"la so khong hoan hao")
        
#in tong S
sum=0
numbers=[1,2,3,4,5]
for number in numbers:
    sum+=number
print("sum=",sum)

    