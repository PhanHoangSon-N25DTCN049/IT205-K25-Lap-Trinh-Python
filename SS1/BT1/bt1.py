#   kết quả in ra sai là do biến được truyền vào print không đúng 
#  tên bệnh nhân được truyền vào dòng print của tuổi còn tuổi thì được truyền vào triệu chứng ... 


print('-- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input('Nhập triệu chứng: ');

print('-- Phiếu khám bệnh --');
print('Tên bệnh nhân: ', name_patient);
print('Tuổi: ', age);
print('Triệu chứng: ', symptom);