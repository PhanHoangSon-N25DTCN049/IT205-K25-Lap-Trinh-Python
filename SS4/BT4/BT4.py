correct_answer = 79;
check = False;
for i in range(5):
    forecast = int(input(f"Lượt đoán {i + 1}: - Nhập số của bạn(1 - 99): "));
    if forecast > correct_answer:
        print("Gợi ý: Số của bạn lớn hơn số may mắn!");
    elif forecast < correct_answer:
        print("Gợi ý: Số của bạn nhỏ hơn số may mắn!");
    else:
        print("Chúc mừng! Bạn đã đoán đúng số may mắn!")
        check = True;
        break;
    
if check == False:
    print("Bạn đã sử dụng hết 5 lượt đoán! Chúc bạn may mắn lần sau");
    print(f"Số may mắn là: {correct_answer}");
print("Kết thúc trò chơi!");

