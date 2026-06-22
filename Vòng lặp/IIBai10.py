def kiem_tra_so_hoan_hao(n):
    if n <= 1:
        return False
    
    tong_uoc = 0
    # Duyệt các số từ 1 đến n-1 để tìm ước
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
            
    # Kiểm tra xem tổng các ước có bằng n không
    return tong_uoc == n

# Chương trình chính với cơ chế nhập liệu an toàn
while True:
    try:
        n = int(input("Nhập vào một số nguyên dương N: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0!")
        else:
            if kiem_tra_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo.")
            else:
                print(f"{n} không phải là số hoàn hảo.")
            break 
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")