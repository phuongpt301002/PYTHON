def ve_hinh_chu_nhat_rong(n, m):
    print(f"Hình chữ nhật rỗng kích thước {m}x{n}:")
    for i in range(m):
        # i chạy từ 0 đến m-1 (tổng cộng m hàng)
        for j in range(n):
            # j chạy từ 0 đến n-1 (tổng cộng n cột)
            
            # Kiểm tra xem có phải là biên không:
            # Biên trên (i == 0) hoặc biên dưới (i == m-1)
            # Biên trái (j == 0) hoặc biên phải (j == n-1)
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print('*', end=" ")
            else:
                # In khoảng trắng cho phần rỗng bên trong
                print(' ', end=" ")
        # Xuống dòng sau khi in xong một hàng
        print()

# Chương trình chính
try:
    n = int(input("Nhập chiều dài (n): "))
    m = int(input("Nhập chiều rộng (m): "))
    
    if n <= 0 or m <= 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        ve_hinh_chu_nhat_rong(n, m)
except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")