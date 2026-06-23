from abc import ABC, abstractmethod

class AWSS3StorageService:
    def upload_lesson(self, lesson):
        print("[Hệ thống AWS S3]: Đang khởi tạo luồng băng thông kết nối tới LMS...")
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
        print(f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.")

class GoogleCloudStorageService:
    def upload_lesson(self, lesson):
        print("[Hệ thống Google Cloud]: Đang kết nối API kết nối tới LMS...")
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
        print(f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.")

def sync_to_cloud(cloud_service, lesson):
    if not hasattr(cloud_service, "upload_lesson") or not callable(getattr(cloud_service, "upload_lesson")):
        raise AttributeError("Dịch vụ lưu trữ đám mây không hợp lệ hoặc chưa ký kết chứng chỉ API liên thông")
    cloud_service.upload_lesson(lesson)

class BaseLesson(ABC):
    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10 

    def __init__(self, lesson_code: str, title: str):
        if type(self) is BaseLesson:
            raise TypeError("Không thể khởi tạo trực tiếp đối tượng từ lớp trừu tượng BaseLesson!")
        self.lesson_code = lesson_code
        self._title = title.strip().upper()
        self.__duration_minutes = 0

    @property
    def duration_minutes(self):
        return self.__duration_minutes

    def set_duration(self, minutes: float):
        if minutes <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
        self.__duration_minutes = minutes

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title: str):
        if not new_title.strip():
            raise ValueError("Tiêu đề không được bỏ trống")
        self._title = new_title.strip().upper()

    @staticmethod
    def validate_lesson_code(lesson_code: str) -> bool:
        return len(lesson_code) == 10 and lesson_code.startswith("LMS")
    
    @classmethod
    def update_base_points(cls, new_points: int):
        if new_points <= 0:
            raise ValueError("Dữ liệu nhập vào không được nhỏ hơn hoặc bằng 0")
        cls.base_completion_points = new_points
    
    @abstractmethod
    def calculate_completion_score(self):
        pass
    
    @abstractmethod
    def update_content(self, new_data):
        pass
    
    def __add__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes
    
    def __lt__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes
    
class VideoLesson(BaseLesson):
    def __init__(self, lesson_code, title):
        super().__init__(lesson_code, title)
        self.video_quality = "1080p"
        self.view_count = 0
        
    def calculate_completion_score(self):
        return self.base_completion_points + (self.duration_minutes * 0.5)
    
    def update_content(self, new_data):
        self.video_quality = str(new_data)
        print(f"Cập nhật thông số thành công! Chất lượng video hiện tại: {self.video_quality}")
        
    def play_video(self):
        self.view_count += 1
        print("Ghi nhận thành công! Học viên đã xem video bài học.")
        print(f"Tổng số lượt xem hiện tại: {self.view_count} lượt.")
    
class CodingChallenge(BaseLesson):
    def __init__(self, lesson_code, title):
        super().__init__(lesson_code, title)
        self.number_of_testcases = 0
        self.difficulty_multiplier = 1.5
    
    def calculate_completion_score(self):
        return self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier
    
    def update_content(self, new_data):
        try:
            cases = int(new_data)
            if cases <= 0:
                raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
            self.number_of_testcases = cases
            print("Cập nhật thông số thành công!")
            print(f"Số lượng testcase hiện tại trên hệ thống: {self.number_of_testcases} testcases.")
        except ValueError as e:
            if "không được nhỏ hơn hoặc bằng 0" in str(e):
                raise e
            raise ValueError("Số lượng testcase phải là một số nguyên hợp lệ!")
    
class HybridAssessment(VideoLesson, CodingChallenge):
    def __init__(self, lesson_code, title):
        super().__init__(lesson_code, title)
        CodingChallenge.__init__(self, lesson_code, title)
        self.video_quality = "1080p"
        self.view_count = 0

    def calculate_completion_score(self):
        coding_score = self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier
        video_bonus = self.duration_minutes * 0.5
        return self.base_completion_points + coding_score + video_bonus
    
    def update_content(self, new_data):
        try:
            cases = int(new_data)
            if cases <= 0:
                raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
            self.number_of_testcases = cases
            print("Cập nhật thông số thành công!")
            print(f"Số lượng testcase hiện tại trên hệ thống: {self.number_of_testcases} testcases.")
        except ValueError as e:
            if "không được nhỏ hơn hoặc bằng 0" in str(e):
                raise e
            raise ValueError("Số lượng testcase phải là một số nguyên hợp lệ!")

def add_input():
    while True:
        lesson_code = input("Nhập mã bài học 10 ký tự: ").strip()
        if BaseLesson.validate_lesson_code(lesson_code):
            break
        print("Mã bài học không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng LMS.")
    while True:
        title = input("Nhập tiêu đề bài học: ")
        if title.strip():
            break
        print("Tiêu đề không được bỏ trống")
    return lesson_code, title

def main():
    lessons = []
    current_lesson = None
    
    while True:
        print("\n===== RIKKEI ACADEMY LMS SIMULATOR PRO =====")
        print("1. Khởi tạo bài học mới (Chọn loại bài học nội dung)")
        print("2. Xem thông tin bài học & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Cập nhật thời lượng & Nội dung bài học (Tính đa hình)")
        print("4. Xem chi tiết điểm thưởng hoàn thành bài học")
        print("5. Kiểm tra gộp thời lượng & So sánh độ dài bài học (Overloading)")
        print("6. Đồng bộ bài giảng lên Nền tảng Đám mây (Duck Typing)")
        print("7. Thoát chương trình")
        print("============================================")
        choice = input("Chọn chức năng (1-7): ").strip()
        
        match choice:
            case "1":
                print("\n--- CHỌN LOẠI BÀI HỌC KHỞI TẠO ---")
                print("1. Video Lesson (Bài học Video Lý Thuyết)")
                print("2. Coding Challenge (Bài tập Thực Hành Code)")
                print("3. Hybrid Assessment (Bài Kiểm Tra Tổng Hợp)")
                choice_add = input("Chọn loại bài học (1-3): ").strip()
                
                lesson_code, title = add_input()
                
                match choice_add:
                    case "1":
                        current_lesson = VideoLesson(lesson_code, title)
                        print("Khởi tạo bài học Video thành công!")
                    case "2":
                        current_lesson = CodingChallenge(lesson_code, title)
                        print("Khởi tạo Bài tập Thực Hành thành công!")
                    case "3":
                        current_lesson = HybridAssessment(lesson_code, title)
                        print("Khởi tạo bài Kiểm Tra Tổng Hợp thành công!")
                    case _:
                        print("Lựa chọn loại bài học không hợp lệ!")
                        continue
                        
                lessons.append(current_lesson)
                print(f"Tiêu đề bài học: {current_lesson.title}")
                
            case "2":
                if not current_lesson:
                    print("Lỗi: Chưa có bài học nào được kích hoạt. Hãy khởi tạo ở chức năng 1 trước!")
                    continue
                
                category = type(current_lesson).__name__
                print("\n--- THÔNG TIN BÀI HỌC HIỆN TẠI ---")
                print(f"Loại bài học: {category}")
                print(f"Nền tảng: {current_lesson.platform_name}")
                print(f"Mã bài học: {current_lesson.lesson_code}")
                print(f"Tiêu đề bài học: {current_lesson.title}")
                print(f"Thời lượng bài học: {current_lesson.duration_minutes} phút")
                
                if isinstance(current_lesson, VideoLesson):
                    print(f"Chất lượng video: {current_lesson.video_quality}")
                if isinstance(current_lesson, CodingChallenge):    
                    print(f"Số lượng testcase lập trình: {current_lesson.number_of_testcases} bài")
                
                list_mro = [cls.__name__ for cls in type(current_lesson).__mro__]
                print(f"Thứ tự kế thừa (MRO): {' -> '.join(list_mro)}")
                
            case "3":
                if not current_lesson:
                    print("Lỗi: Chưa có bài học nào được kích hoạt!")
                    continue
                    
                print("\n--- CẬP NHẬT NỘI DUNG & THỜI LƯỢNG ---")
                print("1. Giả lập học viên tăng lượt xem video (Chỉ dành cho Video/Hybrid)")
                print("2. Cập nhật thông số bài học (Thời lượng, testcase...)")
                task_choice = input("Chọn tác vụ (1-2): ").strip()
                
                if task_choice == "1":
                    if isinstance(current_lesson, VideoLesson):
                        current_lesson.play_video()
                    else:
                        print("Tác vụ này chỉ áp dụng cho Video Lesson hoặc Hybrid Assessment!")
                elif task_choice == "2":
                    try:
                        minutes_input = input("Nhập thời lượng bài học mới (phút): ").strip()
                        if minutes_input:
                            current_lesson.set_duration(float(minutes_input))
                        
                        if isinstance(current_lesson, CodingChallenge):
                            testcase_input = input("Nhập số lượng testcase kiểm thử mới bổ sung: ").strip()
                            current_lesson.update_content(testcase_input)
                        elif isinstance(current_lesson, VideoLesson) and not isinstance(current_lesson, HybridAssessment):
                            quality_input = input("Nhập chất lượng video mới (ví dụ: 1080p, 4K): ").strip()
                            current_lesson.update_content(quality_input)
                    except ValueError as e:
                        print(f"Lỗi cấu hình chỉ số: {e}")
                else:
                    print("Tác vụ không hợp lệ!")
                    
            case "4":
                if not current_lesson:
                    print("Lỗi: Chưa có bài học nào được kích hoạt!")
                    continue
                
                print("\n--- CHI TIẾT ĐIỂM THƯỞNG HOÀN THÀNH ---")
                print(f"Bài học: {current_lesson.title} (Loại: {type(current_lesson).__name__})")
                print(f"Điểm cơ sở hệ thống: {current_lesson.base_completion_points} XP")
                print(f"Thời lượng tích lũy: {current_lesson.duration_minutes} phút")
                if isinstance(current_lesson, CodingChallenge):
                    print(f"Số lượng testcase cấu hình: {current_lesson.number_of_testcases} bài")
                
                total_xp = current_lesson.calculate_completion_score()
                print(f"Tổng điểm kinh nghiệm (XP) nhận được khi hoàn thành: {total_xp} XP")
                
            case "5":
                if not current_lesson:
                    print("Lỗi: Chưa có bài học nào được kích hoạt!")
                    continue
                
                print("\n--- ĐỒNG BỘ & SO SÁNH THỜI LƯỢNG (OPERATOR OVERLOADING) ---")
                print(f"Bài học hiện tại (A): {current_lesson.title} (Thời lượng: {current_lesson.duration_minutes} phút)")
                
                valid_lessons = [l for l in lessons if l.lesson_code != current_lesson.lesson_code]
                if not valid_lessons:
                    print("Hệ thống chưa có đủ bài học đối ứng khác trong danh sách để thực hiện so sánh/cộng gộp.")
                    continue
                
                print("Danh sách bài học đối ứng khả dụng:")
                for idx, l in enumerate(valid_lessons):
                    print(f"[{idx}] {l.lesson_code} ({l.title} - Thời lượng: {l.duration_minutes} phút)")
                
                try:
                    choose_idx = int(input("Chọn số thứ tự bài học đối ứng (B): ").strip())
                    lesson_b = valid_lessons[choose_idx]
                    
                    if current_lesson < lesson_b:
                        res_lt = "Thời lượng bài học A NGẮN HƠN thời lượng bài học B."
                    elif lesson_b < current_lesson:
                        res_lt = "Thời lượng bài học A DÀI HƠN thời lượng bài học B."
                    else:
                        res_lt = "Thời lượng bài học A BẰNG thời lượng bài học B."
                    
                    total_duration = current_lesson + lesson_b
                    
                    print(f"[Kết quả So sánh (__lt__)]: {res_lt}")
                    print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời lượng học tập của cả 2 bài học là: {total_duration} phút.")
                except (ValueError, IndexError):
                    print("Lựa chọn bài học đối ứng không hợp lệ hoặc lỗi kiểu dữ liệu!")
                except TypeError:
                    print("Lỗi: Toán tử Overloading trả về cấu trúc không tương thích (NotImplemented).")

            case "6":
                if not current_lesson:
                    print("Lỗi: Chưa có bài học nào được kích hoạt!")
                    continue
                
                print("\n--- ĐỒNG BỘ BÀI GIẢNG LÊN NỀN TẢNG ĐÁM MÂY ---")
                print("1. Đồng bộ lên máy chủ AWS S3 Storage")
                print("2. Đồng bộ lên máy chủ Google Cloud Storage")
                print("3. Giả lập lỗi nhà cung cấp Cloud không hợp lệ")
                cloud_choice = input("Chọn dịch vụ lưu trữ (1-3): ").strip()
                
                try:
                    if cloud_choice == "1":
                        provider = AWSS3StorageService()
                        sync_to_cloud(provider, current_lesson)
                    elif cloud_choice == "2":
                        provider = GoogleCloudStorageService()
                        sync_to_cloud(provider, current_lesson)
                    elif cloud_choice == "3":
                        class InvalidCloudService: pass
                        provider = InvalidCloudService()
                        sync_to_cloud(provider, current_lesson)
                    else:
                        print("Lựa chọn không hợp lệ!")
                except AttributeError as e:
                    print(f"[LỖI XÁC THỰC]: {e}")
                    
            case "7":
                print("Cảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!")
                break
            case _:
                print("Chức năng không hợp lệ, vui lòng chọn lại từ 1 đến 7.")

if __name__ == "__main__":
    main()