def Fibonacci(n):
    if(n == 0 or n == 1):
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)
num1 = input("Enter the number of Fibonacci: ")
value = Fibonacci(int(num1))
print("Fibonacci is: ", value)

def giaiThua(n):
    if(n == 1):
        return 1
    return n * giaiThua(n - 1)
num2 = input("Enter the number of giai thua: ")
mul = giaiThua(int(num2))
print("Giai thua la: ", mul)

def tinhTong(n):
    if(n == 1):
        return 1
    return n + tinhTong(n - 1)
num3 = input("Nhap so tu nhien: ")
sum = tinhTong(int(num3))
print("Tong can tinh la: ", sum)

def sum(a, b):
    return a + b
num4 = input("Nhap so dau tien: ")
num5 = input("Nhap so thu hai: ")
tong = sum(int(num4), int(num5))
print("Tong hai so tu nhien la: ", tong)