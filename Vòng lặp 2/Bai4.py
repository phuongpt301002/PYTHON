import math

# Sử dụng logic kiểm tra số nguyên tố từ hệ thống của bạn
def kiem_tra_so_nguyen_to(n):
    # Nếu n < 2 thì trả về false
    if n < 2:
        return False
    #Kiểm tra ước số tiềm năng của n
    #Chạy từ 2 vì 2 là số nguyên tố nhỏ nhất
    """
    Kiểm tra đến căn bậc 2 của n vì nếu n có ước số lớn hơn
    căn bậc 2 của nó, thì nó phải có 1 ước số khác nhỏ hơn căn
    bậc 2 đó
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        #Chia lấy dư, khi tìm thấy 1 số mà n%i (khác 1 và chính nó) -> Ko phải số nguyên tố
        if n % i == 0:
            return False
    return True

def in_cac_so_nguyen_to_nho_hon_n(n):
    print(f"Các số nguyên tố nhỏ hơn {n} là:")
    danh_sach_nt = [] #Khởi tạo danh sách để lưu trữ các SNT được tìm thấy
    for i in range(2, n): #Khoảng các số cần kiểm tra tính nguyên tố
        if kiem_tra_so_nguyen_to(i): #Kiểm tra i là SNT sẽ thêm vào danh sách
            danh_sach_nt.append(str(i)) #Chuyển số nguyên thành chuỗi
    
    if danh_sach_nt: #Kiểm tra danh sách có phần tử nào không
        print(", ".join(danh_sach_nt)) #Nối các số trong danh sách lại với nhau phân cách bằng dấu phẩy và khoảng cách
    else:
        print("Không có số nguyên tố nào nhỏ hơn n.")

# Chương trình chính
try:
    n = int(input("Nhập vào số nguyên n: "))
    in_cac_so_nguyen_to_nho_hon_n(n)
except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")