#bài 3
import math
print("nhập bán kính chiều cao")
a=eval(input("bán kính a="))
b=eval(input("chiều cao b="))
S=2*3.14*a*b
print("diện tích xung quanh=",S)
P=2*3.14*2*a
print("diện tích toàn phần",P)
V=2*a*b*3.14
print("thể tích hình trụ=",V)

#bài 7
# Hàm giải phương trình bậc 2
import math
def giaiptb2(a,b,c):
    if(a==0):
        if b==0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ",(-c/b))
        return
    delta = b*b-4*a*c
    if delta > 0:
        x1= float((-b+math.sqrt(delta))/(2*a))
        x2=float((-b-math.sqrt(delta))/(2*a))
        print("Phương trình có 2 nghiệm là: x1 = ",x1,"và x2 = ",x2)
    elif delta==0:
        x=-b/(2*a)
        print("Phương trình có nghiệm là : x1 = x2 = ",x)
    else:
        print("Phương trình vô nghiệm!")        
a=float(input("a = "))
b=float(input("b = "))               
c=float(input("c = "))
giaiptb2(a,b,c)

#bài 6
hieu_dien_the=220
cuong_do_dong_dien=2.7
gia_tien_dien=7000
thoi_gian=7
cong_suat_tieu_thu=hieu_dien_the*cuong_do_dong_dien
dien_nang_tieu_thu=cong_suat_tieu_thu*thoi_gian
so_tien_phai_tra=dien_nang_tieu_thu*gia_tien_dien
print("hiệu điện thế",hieu_dien_the)
print("cường độ dòng điện",cuong_do_dong_dien)
print("giá tiền điện",gia_tien_dien)
print("thời gian",thoi_gian)
print("công suất tiêu thụ",cong_suat_tieu_thu)
print("điẹn năng tiêu thụ",dien_nang_tieu_thu)
print("số tiền phải trả",so_tien_phai_tra)

#bài 8
x1=2
y1=3