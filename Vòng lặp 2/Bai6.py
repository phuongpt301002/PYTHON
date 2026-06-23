def in_tam_giac_so(n):
    so_hien_tai = 1 #Khởi tạo biến bằng 1 để tam giác luôn bắt đầu là 1 và tăng dần 1,2,3,....
    for i in range(1, n + 1): #Vòng lặp ngoài, kiểm soát số hàng của tam giác
        # In i số trên mỗi hàng
        for j in range(i): #Vòng lặp trong, kiểm soát số lượng con số trên mỗi hàng, hàng 1 in 1 số, hàng 2 in 2 số,...
            print(f"{so_hien_tai:<3}", end="") #làm số thẳng hàng, end ngăn tự động xuống dòng, các số in trên cùng 1 hàng
            so_hien_tai += 1 #Sau khi in 1 số, tăng giá trị lên 1 để in số tiếp theo
        # Xuống dòng sau khi in xong một hàng
        print()

# Chương trình chính
try:
    n = int(input("Nhập số hàng bạn muốn in: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        in_tam_giac_so(n)
except ValueError:
    print("Dữ liệu nhập vào phải là số nguyên!")