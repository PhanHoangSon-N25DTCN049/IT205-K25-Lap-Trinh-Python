"""
trong đoạn code trên hệ thống sử dụng or để kiểm tra điều kiện
nên khi chỉ cần 1 điều kiện đúng thì sẽ trả về true và cho kết quả đủ điều kiện

or trả về true khi có 1 điều kiện đúng 
and trả về true khi tất cả điều kiện đều đúng    
"""

print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
elif donor_age < 18:
    print("Result: not old enough")
elif donor_weight < 50:
    print("Result: not enough weight");
    
