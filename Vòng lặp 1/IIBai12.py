def tinh_tong_chu_so(n):
    n = abs(n)  # Đảm bảo n là số dương để tính toán
    tong = 0
    while n > 0:
        tong += n % 10  # Lấy chữ số cuối cùng cộng vào tổng
        n //= 10        # Bỏ chữ số cuối cùng bằng phép chia nguyên cho 10
    return tong

# Chương trình chính với cơ chế nhập liệu an toàn
while True:
    try:
        n_input = input("Nhập vào một số nguyên dương n: ")
        n = int(n_input)
        
        if n < 0:
            print("Vui lòng nhập một số nguyên dương!")
        else:
            ket_qua = tinh_tong_chu_so(n)
            print(f"Tổng các chữ số của {n} là: {ket_qua}")
            break
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")