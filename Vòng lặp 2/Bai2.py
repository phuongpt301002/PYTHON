def in_bang_cuu_chuong():
    print("--- BẢNG CỬU CHƯƠNG TỪ 2 ĐẾN 9 ---")
    # Duyệt qua các số từ 2 đến 9
    for i in range(2, 10):
        print(f"\nBảng cửu chương {i}:")
        # Duyệt qua các số nhân từ 1 đến 10
        for j in range(1, 11):
            print(f"{i} x {j:2} = {i * j:2}")

# Gọi hàm thực thi
if __name__ == "__main__":
    in_bang_cuu_chuong()