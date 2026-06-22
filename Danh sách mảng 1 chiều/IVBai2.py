def tim_max_thu_cong(danh_sach):
    # Giả định phần tử đầu tiên là lớn nhất
    max_val = danh_sach[0]
    # Duyệt qua các phần tử còn lại để so sánh
    for x in danh_sach:
        if x > max_val:
            max_val = x
    return max_val

# Chương trình chính
try:
    n = int(input("Nhập số lượng phần tử N: "))
    if n <= 0:
        print("Số lượng phần tử phải lớn hơn 0!")
    else:
        day_so = []
        # Nhập dãy số
        for i in range(n):
            so = int(input(f"Nhập phần tử thứ {i+1}: "))
            day_so.append(so)
        
        # Tìm max
        max_cua_day = tim_max_thu_cong(day_so)
        print(f"Phần tử lớn nhất trong dãy là: {max_cua_day}")

except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")
except IndexError:
    print("Danh sách không được để trống!")