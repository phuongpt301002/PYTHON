def tinh_tong(m, n):
    tong = 0
    print(f"Các số chia hết cho 3 hoặc 5 từ {m} đến {n} là:")
    for i in range(m, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            print(i, end=" ")
            tong += i
    print(f"\n=> Tổng là: {tong}")

# Nhập dữ liệu
try:
    m = int(input("Nhập số nguyên dương M: "))
    n = int(input("Nhập số nguyên dương N: "))

    if m >= n:
        print("Lỗi: M phải nhỏ hơn N!")
    else:
        tinh_tong(m, n)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")