patient_name = input('Nhập tên bệnh nhân: ').strip();
year_of_birth = int(input('Nhập năm sinh bệnh nhân: '));
number_of_sick_days = int(input('Nhập số ngày bệnh: '));
body_temperature = float(input('Nhập nhiệt độ cơ thể: '));
examination_costs = int(input('Nhập chi phí khám: '));

if patient_name == '':
    print('Tên bệnh nhân không được để trống');
elif year_of_birth < 1900 or year_of_birth > 2026:
    print('Năm sinh không hợp lệ');
elif number_of_sick_days <= 0:
    print('Số ngày bệnh không hợp lệ');
elif body_temperature < 30 or body_temperature > 45:
    print('Nhiệt độ cơ thể không hợp lệ');
elif examination_costs < 0:
    print('Chi phí khám > 0');
else:
    print('-- Kết quả -- ');
    print("Tên: ", patient_name);
    print("Tuổi: ", 2026 - year_of_birth);
    print('Nhiệt độ cơ thể: ', body_temperature);
    print("Số ngày bệnh: ", number_of_sick_days);
    status = '';
    if body_temperature > 38 and number_of_sick_days > 3:
        status = 'Nguy hiểm';
    elif body_temperature > 38:
        status = 'Sốt cao';
    elif body_temperature > 37.5:
        status = 'Sốt nhẹ';
    else: 
        status = 'bình thường';
    print('\n\nTình trạng: ', status);
    
    priority_level = '';
    if status == 'Nguy hiểm':
        if 2026 - year_of_birth > 60:
            priority_level = 'Cấp cứu';
        else:
            priority_level = 'Ưu tiên cao';
    else:
        priority_level = 'Bình thường';
    print('Cấp độ ưu tiên: ', priority_level);
    
    print('\nTổng chi phí: ', examination_costs * 1.1);
    print(f'Mức chi phí:', "Cao" if examination_costs * 1.1 else 'thấp');
    