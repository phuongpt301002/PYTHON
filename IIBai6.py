def ve_hinh_chu_nhat(n, m):
    print(f"Hình chữ nhật kích thước {m}x{n}:")
    for i in range(m):
        # In n dấu sao trên cùng một hàng
        print(' * ' * n)

# Chương trình chính
while True:
    try:
        n = int(input("Nhập chiều dài (n): "))
        m = int(input("Nhập chiều rộng (m): "))
        
        if n <= 0 or m <= 0:
            print("Vui lòng nhập số nguyên dương!")
        else:
            ve_hinh_chu_nhat(n, m)
            break
    except ValueError:
        print("Đầu vào không hợp lệ, hãy nhập số nguyên!")