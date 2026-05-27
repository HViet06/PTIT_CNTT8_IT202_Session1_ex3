# luồng: nhập tên, nhập cân nặng 
# dữ liệu lưu dưới dạng chuỗi ký tự, không phải số thực 
# in ra kiểu str

print("---- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ----")
name_patient = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : "))
print("---- KIỂM TRA DỮ LIỆU LƯU TRỮ ----")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))