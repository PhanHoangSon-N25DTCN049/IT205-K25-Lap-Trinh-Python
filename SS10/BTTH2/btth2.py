# Khởi tạo danh sách phát nhạc trống ban đầu
playlist = []

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DANH SÁCH PHÁT NHẠC =====")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")
    print("================================================")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    

    match choice:
        # CHỨC NĂNG 1: THÊM BÀI HÁT VÀO DANH SÁCH PHÁT
        case "1":
            print("\n--- CHỌN CÁCH THÊM BÀI HÁT ---")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào vị trí bất kỳ")
            sub_choice = input("Nhập lựa chọn của bạn (1-2): ").strip()
            
            match sub_choice:
                case "1":
                    song_name = input("Nhập tên bài hát: ").strip()
                    if song_name == "":
                        print("Tên bài hát không được để trống!")
                    else:
                        playlist.append(song_name)
                        print(f"Đã thêm thành công bài hát '{song_name}' vào cuối danh sách.")
                        print(f"Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                        
                case "2":
                    song_name = input("Nhập tên bài hát: ").strip()
                    if song_name == "":
                        print("Tên bài hát không được để trống!")
                    else:
                        pos_input = input("Nhập số thứ tự muốn chèn: ").strip()
                        
                        # Bẫy 4 (Menu phụ): Kiểm tra số thứ tự phải là số nguyên
                        if not pos_input.isdigit():
                            print("Vị trí phải là số nguyên hợp lệ!")
                        else:
                            pos = int(pos_input)
                            index = pos - 1  # Chuyển đổi từ số thứ tự người dùng sang index trong Python
                            
                            # Bẫy 3: Kiểm tra giới hạn index (chỉ cho phép chèn từ vị trí đầu đến sát cuối + 1)
                            if 0 <= index <= len(playlist):
                                playlist.insert(index, song_name)
                                print(f"Đã chèn thành công bài hát '{song_name}' vào vị trí {pos}.")
                                print(f"Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                            else:
                                print("Vị trí không hợp lệ.")
                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                    
        # CHỨC NĂNG 2: XEM DANH SÁCH PHÁT
        case "2":
            # Bẫy 1: Thao tác khi danh sách trống
            if not playlist:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- DANH SÁCH PHÁT HIỆN TẠI ---")
                for index, song in enumerate(playlist, start=1):
                    print(f"{index}. {song}")
                    
        # CHỨC NĂNG 3: XÓA BÀI HÁT KHỎI DANH SÁCH
        case "3":
            # Bẫy 1: Thao tác khi danh sách trống
            if not playlist:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- CHỌN CÁCH XÓA BÀI HÁT ---")
                print("1. Xóa theo tên bài hát")
                print("2. Xóa theo số thứ tự")
                sub_choice = input("Nhập lựa chọn của bạn (1-2): ").strip()
                
                match sub_choice:
                    case "1":
                        song_name = input("Nhập tên bài hát cần xóa: ").strip()
                        
                        # Duyệt tìm bài hát chính xác (có phân biệt hoa thường theo yêu cầu)
                        if song_name in playlist:
                            playlist.remove(song_name)
                            print(f"Đã xóa bài hát [{song_name}] khỏi danh sách.")
                        else:
                            # Bẫy 2: Xóa bài hát không tồn tại
                            print("Không tìm thấy bài hát trong danh sách phát.")
                            
                    case "2":
                        pos_input = input("Nhập số thứ tự bài hát cần xóa: ").strip()
                        
                        if not pos_input.isdigit():
                            print("Số thứ tự phải là số nguyên hợp lệ!")
                        else:
                            pos = int(pos_input)
                            index = pos - 1
                            
                            # Bẫy 3: Chỉ số index vượt quá giới hạn list hiện tại
                            if 0 <= index < len(playlist):
                                removed_song = playlist.pop(index)
                                print(f"Đã xóa bài hát [{removed_song}] khỏi danh sách.")
                            else:
                                print("Vị trí không hợp lệ.")
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                        
        # CHỨC NĂNG 4: SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH
        case "4":
            # Bẫy 1: Thao tác khi danh sách trống
            if not playlist:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- SẮP XẾP VÀ TRÍCH XUẤT ---")
                print("1. Sắp xếp danh sách phát theo bảng chữ cái (A-Z)")
                print("2. Nghe thử 3 bài hát đầu tiên")
                sub_choice = input("Nhập lựa chọn của bạn (1-2): ").strip()
                
                match sub_choice:
                    case "1":
                        playlist.sort()
                        print("Đã sắp xếp danh sách phát theo thứ tự bảng chữ cái thành công.")
                        
                    case "2":
                        print("\n--- ĐANG PHÁT THỬ 3 BÀI HÁT ĐẦU TIÊN ---")
                        # Sử dụng kỹ thuật Slicing để lấy ra tối đa 3 bài hát đầu tiên
                        preview_list = playlist[:3]
                        for index, song in enumerate(preview_list, start=1):
                            print(f"Đang phát bài {index}: {song}")
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                        
        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
            
        # BẪY 4: Khớp tất cả các trường hợp nhập sai ký tự lạ hoặc số ngoài 1-5 ở menu chính
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")