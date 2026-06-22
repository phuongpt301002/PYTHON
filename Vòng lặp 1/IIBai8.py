def ve_tam_giac_vuong_can(n):
    print(f"Tam giác vuông cân với cạnh góc vuông bằng {n}:")
    # Vẽ n hàng
    for i in range(1, n + 1):
        # Mỗi hàng i sẽ in ra i dấu sao
        print(' * ' * i)

# Chương trình chính
try:
    n = int(input("Nhập độ dài cạnh góc vuông (n): "))
    
    if n <= 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        ve_tam_giac_vuong_can(n)
except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")