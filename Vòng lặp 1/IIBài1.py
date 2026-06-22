def in_so_le(n):
    print(f"Các số lẻ nhỏ hơn hoặc bằng {n} là:")
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print() # Xuống dòng sau khi in xong

# Nhập dữ liệu từ người dùng
try:
    n_input = int(input("Nhập vào số nguyên n: "))
    in_so_le(n_input)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")