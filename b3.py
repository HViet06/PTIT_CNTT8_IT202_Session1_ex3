# input: patient_name, medical_code, department
# output: Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám]
# hiển thị tiêu đề, nhập họ tên, nhập mã bệnh, nhập phòng, hiển thị phiếu, kêt thúc

print("===== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN =====")
patient_name = input("Nhập họ tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")
print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")

print(f"Bệnh nhân: {patient_name} - " f"Mã BA: {medical_code} - " f"Chuyển tới: {department}")

print("===== TIẾP NHẬN THÀNH CÔNG =====")