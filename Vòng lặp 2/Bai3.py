def tinh_tong_chu_so(n):
    n = abs(n)  # Đảm bảo n là số dương để tính toán
    tong = 0
    while n > 0:
        tong += n % 10  # Lấy chữ số cuối cùng cộng vào tổng
        n //= 10        # Bỏ chữ số cuối cùng bằng phép chia nguyên cho 10
    return tong

# Chương trình chính với cơ chế nhập liệu an toàn

try:
    n_input = int(input("Nhập vào một số nguyên n: "))
    tinh_tong_chu_so(n_input)
    print(f"Tổng các chữ số của {n_input} là: ", tinh_tong_chu_so(n_input))
except ValueError:
    print("Đó không phải là số nguyên, hãy thử lại!")