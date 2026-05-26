""" 
Phân tích Input / Output
Dữ liệu đầu vào (Input):

age: Số nguyên, đại diện cho tuổi bệnh nhân.

blood_pressure: Số nguyên, đại diện cho huyết áp tâm thu (mmHg).

blood_sugar: Số nguyên, đại diện cho chỉ số đường huyết (mg/dL).

Dữ liệu đầu ra (Output):

Thông báo kết quả xét duyệt: "ĐỦ ĐIỀU KIỆN PHẪU THUẬT" hoặc "TỪ CHỐI PHẪU THUẬT".

Thông báo lỗi dữ liệu: "Dữ liệu nhập vào không hợp lệ" (khi có chỉ số âm).

Giải pháp 1: Gộp điều kiện (Flat Logic)Sử dụng toán tử logic and để kiểm tra tất cả các điều kiện y khoa cùng một lúc trên một dòng if.
Nếu tất cả đều đúng thì đủ điều kiện, ngược lại là từ chối.

Giải pháp 2: Điều kiện lồng nhau (Nested If)Kiểm tra từng chỉ số một theo từng cấp bậc.


Tiêu chí	                    Giải pháp 1: Gộp điều kiện (Flat Logic)	                                                Giải pháp 2: Điều kiện lồng nhau (Nested If)
Độ ngắn gọn của code	        Rất ngắn gọn, ít dòng code, cấu trúc phẳng.	                                            Dài hơn do phải chia thành nhiều cấp bậc điều kiện.

Độ phức tạp khi đọc code	    Dễ đọc, nhìn tổng quan luật nghiệp vụ rất nhanh vì không bị thụt lề nhiều.	            Phức tạp hơn, thụt lề (indentation) nhiều tầng dễ gây rối mắt nếu có nhiều tiêu chí.

Trải nghiệm & Giá trị y khoa	Trải nghiệm ở mức cơ bản. Chỉ thông báo chung chung là bị từ chối chứ không             Cho phép ghi nhận và thông báo cụ thể lý do từ chối (Ví dụ: Từ chối do huyết áp cao)
                                chỉ rõ bệnh nhân bị trượt ở chỉ số nào.	Trải nghiệm cao và có giá trị y khoa lớn.       
"""

# Bước 1: Nhập dữ liệu đầu vào từ điều dưỡng
age = int(input("Nhập tuổi bệnh nhân: "))
blood_pressure = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

print("\n-- KẾT QUẢ SÀNG LỌC TIỀN PHẪU THUẬT --")

# Bước 2: Xử lý Edge Cases (Bẫy dữ liệu âm hoặc không hợp lý)
if age < 0 or blood_pressure < 0 or blood_sugar < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ")

# Bước 3: Xét duyệt y khoa theo giải pháp Điều kiện lồng nhau (Nested If)
else:
    # Kiểm tra tiêu chí 1: Tuổi
    if age < 75:
        
        # Kiểm tra tiêu chí 2: Huyết áp tâm thu (90 - 140 mmHg)
        if 90 <= blood_pressure <= 140:
            
            # Kiểm tra tiêu chí 3: Đường huyết
            if blood_sugar < 150:
                print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
                
            else:
                print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
                print("Lý do: Chỉ số đường huyết vượt ngưỡng an toàn (>= 150 mg/dL).")
                
        else:
            print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
            print("Lý do: Huyết áp tâm thu nằm ngoài khoảng an toàn (90 - 140 mmHg).")
            
    else:
        print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Bệnh nhân vượt quá độ tuổi phẫu thuật an toàn (>= 75 tuổi).")