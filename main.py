patient_name = input("Nhập tên bệnh nhân: ").strip()
patient_age = int(input("Nhập tuổi bệnh nhân: "))

if patient_name == "" or (patient_age < 0 or patient_age > 150):
    print ("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    exit () 
else:
    if patient_age < 6:
        print ("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.")
    elif patient_age > 80:
        print ("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
    else:
        print ("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.") 

# INPUT: tên bệnh nhân (dạng chuỗi), tuổi bệnh nhân (dạng số nguyên)
# OUTPUT: thông báo (dạng chuỗi)