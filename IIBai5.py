def tinh_tong_giai_thua(n):
    tong = 0
    giai_thua = 1
    
    # Duyệt từ 1 đến N
    for i in range(1, n + 1):
        giai_thua *= i  # Cập nhật giá trị giai thừa hiện tại: 1*2*...*i
        tong += giai_thua # Cộng dồn vào tổng
        
    return tong

# Chương trình chính với cơ chế nhập liệu an toàn
while True:
    try:
        n = int(input("Nhập vào một số nguyên dương N: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên lớn hơn 0!")
        else:
            ket_qua = tinh_tong_giai_thua(n)
            print(f"Tổng S = 1 + 1.2 + ... + 1.2...{n} là: {ket_qua}")
            break 
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")