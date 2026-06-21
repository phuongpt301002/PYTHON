# Danh sách ban đầu
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# a) Tính tổng các phần tử dương
def tong_duong(arr):
    return sum(x for x in arr if x > 0)

# b) Đếm số phần tử chia hết cho 3
def dem_chia_het_cho_3(arr):
    return len([x for x in arr if x % 3 == 0])

# c) Thêm phần tử vào vị trí k
def them_vao_vi_tri_k(arr, k, value):
    arr.insert(k, value)
    return arr

# d) Tìm vị trí phần tử âm đầu tiên
def vi_tri_am_dau(arr):
    for i, x in enumerate(arr):
        if x < 0: return i
    return -1

# e) Tìm max và vị trí max cuối cùng
def thong_tin_max(arr):
    val_max = max(arr)
    # Tìm index bằng cách duyệt ngược hoặc lấy index của lần cuối xuất hiện
    idx_max = len(arr) - 1 - arr[::-1].index(val_max)
    return val_max, idx_max

# f) Vị trí phần tử chẵn cuối cùng
def vi_tri_chan_cuoi(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0: return i
    return -1

# g) Kiểm tra tăng dần và sắp xếp
def kiem_tra_va_sap_xep(arr):
    if arr == sorted(arr):
        return True, arr
    else:
        return False, sorted(arr)

# h) Xóa phần tử lớn nhất
def xoa_max(arr):
    val_max = max(arr)
    arr.remove(val_max) # Lưu ý: remove chỉ xóa phần tử đầu tiên nó gặp
    return arr

# THỰC THI KIỂM TRA
print(f"Danh sách gốc: {a}")
print(f"a) Tổng dương: {tong_duong(a)}")
print(f"b) Đếm chia hết cho 3: {dem_chia_het_cho_3(a)}")

# Ví dụ cho câu c (Giả sử k=2, giá trị 100)
print(f"c) Sau khi thêm: {them_vao_vi_tri_k(a.copy(), 2, 100)}")

print(f"d) Vị trí âm đầu: {vi_tri_am_dau(a)}")
print(f"e) Max và vị trí max cuối: {thong_tin_max(a)}")
print(f"f) Vị trí chẵn cuối: {vi_tri_chan_cuoi(a)}")

is_sorted, sorted_a = kiem_tra_va_sap_xep(a)
print(f"g) Có tăng dần không? {is_sorted}. Danh sách sau sắp xếp: {sorted_a}")
print(f"h) Danh sách sau khi xóa 1 giá trị max: {xoa_max(a)}")