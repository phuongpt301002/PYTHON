def loc_so_le(danh_sach, a, b):
    ket_qua = [x for x in danh_sach if a <= x <= b and x % 2 != 0]
    return ket_qua

# Chương trình chính
try:
    n = int(input("Nhập số lượng phần tử N: "))
    day_so = []
    
    # Nhập từng phần tử vào danh sách
    for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        day_so.append(so)
        
    a = int(input("Nhập giá trị a: "))
    b = int(input("Nhập giá trị b: "))
    
    if a >= b:
        print("Lỗi: a phải nhỏ hơn b!")
    else:
        ds_le = loc_so_le(day_so, a, b)
        print(f"Các phần tử lẻ trong khoảng [{a}, {b}] là: {ds_le}")

except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")