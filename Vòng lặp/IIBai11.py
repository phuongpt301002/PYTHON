import math

def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    # Tính căn bậc hai
    can_bac_hai = math.sqrt(n)
    # Kiểm tra xem căn bậc hai có phải là số nguyên hay không
    return can_bac_hai.is_integer()

# Chương trình chính với cơ chế nhập liệu an toàn
while True:
    try:
        n = int(input("Nhập vào một số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên dương!")
        else:
            if kiem_tra_so_chinh_phuong(n):
                print(f"{n} là số chính phương.")
            else:
                print(f"{n} không phải là số chính phương.")
            break
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")