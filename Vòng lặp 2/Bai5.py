def dao_nguoc_so(n):
    # Lưu dấu của số nếu là số âm
    am = n < 0
    n = abs(n)
    
    dao_nguoc = 0 #Khởi tạo biến để lưu kết quả
    while n > 0: #Chạy đến khi nào n vẫn còn giá trị lớn hơn 0
        chu_so = n % 10 #cách để lấy chữ số cuối của n
        """
        Dịch giá trị hiện tại của dao_nguoc sang trái 1 hàng
        (nhân 10) rồi cộng thêm chữ số vừa lấy vào hàng đơn vị
        """
        dao_nguoc = dao_nguoc * 10 + chu_so
        #Chia lấy phần nguyên -> loại bỏ chữ số n=cuối cùng của n sau khi đã xử lý xong
        n //= 10
        
    # Trả lại dấu âm nếu ban đầu là số âm
    return -dao_nguoc if am else dao_nguoc

# Chương trình chính
try:
    n = int(input("Nhập vào một số nguyên n: "))
    ket_qua = dao_nguoc_so(n)
    print(f"Số sau khi đảo ngược là: {ket_qua}")
except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")