import random

def dao_nguoc_so(n):
    am = n < 0
    n = abs(n)
    dao_nguoc = 0
    while n > 0:
        chu_so = n % 10
        dao_nguoc = dao_nguoc * 10 + chu_so
        n //= 10
    return -dao_nguoc if am else dao_nguoc

def choi_game():
    print("--- CHÀO MỪNG BẠN ĐẾN VỚI THỬ THÁCH ĐẢO NGƯỢC ---")
    print("Máy tính sẽ đưa ra một số, nhiệm vụ của bạn là đoán số đó sau khi đảo ngược!")
    
    so_bi_mat = random.randint(10, 999)
    ket_qua_dung = dao_nguoc_so(so_bi_mat)
    
    print(f"\nSố thử thách là: {so_bi_mat}")
    
    try:
        du_doan = int(input("Số sau khi đảo ngược là bao nhiêu?: "))
        
        if du_doan == ket_qua_dung:
            print("Chúc mừng! Bạn đã đoán chính xác! 🎉")
        else:
            print(f"Tiếc quá! Đáp án đúng phải là: {ket_qua_dung}")
            
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên!")

if __name__ == "__main__":
    choi_game()