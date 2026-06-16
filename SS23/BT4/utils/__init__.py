def calculate_average(scores):
    """
    Tính điểm trung bình của sinh viên.
    Bẫy lỗi dữ liệu điểm không hợp lệ (Bẫy 3) và danh sách điểm rỗng (Bẫy 2).
    """
    if not scores or not isinstance(scores, list):
        return 0.0
        
    valid_scores = []
    for score in scores:
        # Kiểm tra xem điểm có phải là số (int hoặc float) và không phải kiểu bool
        if isinstance(score, (int, float)) and not isinstance(score, bool):
            valid_scores.append(float(score))
            
    if not valid_scores:
        return 0.0
        
    return sum(valid_scores) / len(valid_scores)

def classify_student(average):
    """
    Phân loại học lực dựa trên điểm trung bình.
    """
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"