import math

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    # Kiểm tra từ 2 đến căn bậc hai của n
    # Dùng int(math.sqrt(n)) + 1 để giới hạn vòng lặp
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Chương trình chính với cơ chế nhập liệu kiểm tra số âm
while True:
    try:
        n = int(input("Nhập vào một số nguyên n: "))
        
        if n < 0:
            print("Hãy nhập lại số khác (số bạn vừa nhập là số âm)!")
            continue # Quay lại vòng lặp để nhập lại
        
        if kiem_tra_so_nguyen_to(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
        break # Thoát vòng lặp khi đã nhập và kiểm tra xong
        
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên!")