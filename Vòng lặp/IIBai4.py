def tim_cac_uoc(n):
    print(f"Các ước của {n} là:")
    # Duyệt từ 1 đến n
    for i in range(1, n + 1):
        # Nếu n chia hết cho i thì i là ước
        if n % i == 0:
            print(i)

# Chương trình chính với cơ chế nhập liệu an toàn
while True:
    try:
        n = int(input("Nhập vào một số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập một số nguyên lớn hơn 0!")
        else:
            tim_cac_uoc(n)
            break # Thoát vòng lặp sau khi in xong
    except ValueError:
        print("Đó không phải là số nguyên, hãy thử lại!")