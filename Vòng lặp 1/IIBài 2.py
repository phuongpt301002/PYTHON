# Nhập dữ liệu
n = int(input("Nhập vào số N: "))

# Khởi tạo biến tổng
tong = 0

# Vòng lặp từ 1 đến N (range(1, n+1) tạo ra dãy số từ 1 đến n)
for i in range(1, n + 1):
    if i % 2 == 0:  # Kiểm tra số chẵn
        tong = tong + i

# In kết quả
print(f"Tổng các số chẵn từ 1 đến {n} là: {tong}")