#Viết chương trình tính giai thừa của một số cho trước được nhập từ bàn phím
def tinh_giai_thua(n):
    tong_giai_thua = 0
    giai_thua =  1

    for i in range (1, n+1):
        giai_thua *= i
        tong_giai_thua += giai_thua
    return tong_giai_thua

while True:
    try:
        n = int(input("Nhập số nguyên dương n từ bàn phím: "))
        if n <= 0:
            print("Vui lòng nhập lại số nguyên dương");
        else: 
            ketqua = tinh_giai_thua(n)
            print(f"Tổng S = 1 + 1.2 + ... + 1.2...{n} là: {ketqua}")
            break 
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")