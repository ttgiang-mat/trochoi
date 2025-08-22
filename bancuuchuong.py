import random
import os

def clear_screen():
    """Xóa màn hình console để giao diện gọn gàng hơn."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Hiển thị menu chính của trò chơi."""
    print("*************************************")
    print("* *")
    print("* CHÀO MỪNG ĐẾN VỚI GAME CỬU CHƯƠNG  *")
    print("* *")
    print("*************************************")
    print("\nVui lòng chọn một bảng cửu chương để học (từ 1 đến 9):")

def get_choice():
    """Nhận và kiểm tra lựa chọn của người dùng."""
    while True:
        try:
            choice = int(input(">> Nhập lựa chọn của bạn: "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("⚠️ Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 9.")
        except ValueError:
            print("⚠️ Đây không phải là một số! Vui lòng nhập lại.")

def run_game(table_number):
    """Bắt đầu trò chơi với bảng cửu chương đã chọn."""
    score = 0
    questions_total = 10  # Số lượng câu hỏi cho mỗi lượt chơi

    print(f"\n--- Bắt đầu với Bảng Cửu Chương {table_number}! ---")
    print(f"Bạn sẽ có {questions_total} câu hỏi. Cố gắng lên nhé! 💪\n")

    for i in range(questions_total):
        # Tạo câu hỏi ngẫu nhiên
        num1 = table_number
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2

        # Tạo các phương án sai
        wrong_answers = set()
        while len(wrong_answers) < 3:
            wrong = random.randint(correct_answer - 10, correct_answer + 10)
            if wrong != correct_answer and wrong >= 0:
                wrong_answers.add(wrong)

        # Trộn các phương án trả lời
        options = list(wrong_answers) + [correct_answer]
        random.shuffle(options)

        # Hiển thị câu hỏi và các phương án
        print(f"Câu {i + 1}: {num1} x {num2} = ?")
        for idx, option in enumerate(options):
            print(f"  {chr(65 + idx)}. {option}") # A, B, C, D

        # Nhận câu trả lời của người dùng
        while True:
            user_input = input(">> Đáp án của bạn (A, B, C, D): ").upper()
            if user_input in ['A', 'B', 'C', 'D']:
                user_answer_index = ord(user_input) - 65
                user_answer = options[user_answer_index]
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn A, B, C hoặc D.")

        # Kiểm tra và phản hồi
        if user_answer == correct_answer:
            score += 1
            print("🎉 Chính xác! Tuyệt vời!\n")
        else:
            print(f"😥 Rất tiếc, bạn đã sai. Đáp án đúng là {correct_answer}.\n")

    # Hiển thị kết quả cuối cùng
    clear_screen()
    print("--- 🏁 KẾT THÚC 🏁 ---")
    print(f"Bảng cửu chương: {table_number}")
    print(f"Tổng số câu hỏi: {questions_total}")
    print(f"Điểm của bạn: {score}/{questions_total}")

    if score == questions_total:
        print("\n🏆 Xuất sắc! Bạn đã trả lời đúng tất cả các câu hỏi!")
    elif score >= questions_total / 2:
        print("\n👍 Tốt lắm! Hãy tiếp tục luyện tập nhé.")
    else:
        print("\n💪 Đừng nản lòng, luyện tập thêm sẽ giúp bạn giỏi hơn!")

def main():
    """Hàm chính điều khiển luồng của trò chơi."""
    while True:
        clear_screen()
        show_menu()
        choice = get_choice()
        run_game(choice)

        play_again = input("\nBạn có muốn chơi lại không? (c/k): ").lower()
        if play_again != 'c':
            print("\nTạm biệt! Hẹn gặp lại nhé. 👋")
            break

if __name__ == "__main__":
    main()