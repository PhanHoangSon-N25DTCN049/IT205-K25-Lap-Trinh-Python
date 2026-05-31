# các phương thức trên không thay đổi chuỗi gốc mà trả về 1 chuỗi mới nên nếu chỉ gọi mà không gán lại dữ liệu ban đầu sẽ dữ nguyên

student_name = "  ngUYen vAn a "
student_code = "  rk-001-python   "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title();
student_code = student_code.strip().upper();
email = email.strip().lower();

print("Họ tên: ",student_name);
print("Mã học viên: ",student_code);
print("Email: ", email);