def in_bang_cuu_chuong(n):
    print(f"---BẢNG CỬU CHƯƠNG {n}---")
    for i in range (1, 11):
        print(f"{n} x {i:2} = {n * i:2}")

if __name__ == "__main__":
    try:
        n = int(input("Nhập bảng cửu chương bạn muốn in (từ 2 đến 9): "))
        if 2 <= n <= 9:
            in_bang_cuu_chuong(n);
        else: 
            print("Vui lòng nhập số khoảng từ 2 đến 9!!")
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên!")