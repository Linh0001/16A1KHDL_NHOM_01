#  NHÓM SỐ 01 16A1KHDL
#  22174600004 LÊ ĐÌNH TÙNG
#  22174600011 NGUYỄN VĂN DUY
#  22174600005 HUỲNH NGỌC TƯỜNG VI
#  22174600001 PHÙNG THỊ LINH
#  22174600012 TRƯƠNG ANH ĐỨC
import os
import csv
_path="files/ds_cua_hang.csv"
qlcuahang=[]
print("CHƯƠNG TRÌNH QUẢN LÝ CỬA HÀNG")
while True:
    # Menu chương trình
    print("1: Mở file ds_cua_hang.csv") 
    print("2: Nhập thêm thông tin cửa hàng")
    print("3: Lưu thông tin vào file ds_cua_hang.csv")
    print("4: Sắp xếp các cửa hàng theo thứ tự giảm dần của doanh thu")
    print("5: Thoát chương trình")
    chon=int(input("Chọn chức năng cần thực hiện: "))
    if chon==1:
        f=open(_path,'r', encoding ='utf-8')
        for dong in csv.reader(f):
            qlcuahang.append({'Mã cửa hàng':dong[0],'Tên cửa hàng':dong[1], 'Vốn đầu tư':dong[2],'Doanh thu':dong[3],
            'Tiền thuế':dong[4]})
        f.close()
        print("Đã mở file ds_cua_hang.csv !")
    elif chon==2:
        ma_ch=input("Nhập mã cửa hàng: ")
        ten_ch=input("Nhập tên cửa hàng: ")
        von_dt=int(input("Nhập vốn đầu tư: "))
        doanh_thu=int(input("Nhập doanh thu: "))
        #Tính tiền thuế:
        if von_dt>=50000000:
            tien_thue=float((10/100)*doanh_thu)
        else:
            tien_thue=float((5/100)*doanh_thu)
        print("Tiền thuế: ",tien_thue)
        qlcuahang.append({'Mã cửa hàng':ma_ch,'Tên cửa hàng':ten_ch,
                  'Vốn đầu tư':von_dt,'Doanh thu':doanh_thu,'Tiền thuế':tien_thue})
    elif chon==3:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['Mã cửa hàng','Tên cửa hàng','Vốn đầu tư','Doanh thu','Tiền thuế'])
        for ch in qlcuahang:
            csv.writer(f).writerow([ch['Mã cửa hàng'],ch['Tên cửa hàng'], ch['Vốn đầu tư'],ch['Doanh thu'],ch['Tiền thuế']])
        f.close()
        print("Đã lưu file ds_cua_hang.csv !")

    elif chon==4:
        doanh_thu = sorted(qlcuahang,reverse=True, key=lambda x: x['Doanh thu'])
        print("Danh sách trước khi sắp xếp:")
        print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã cửa hàng','Tên cửa hàng',
                      'Vốn đầu tư','Doanh thu','Tiền thuế'))
        for x in qlcuahang:
            print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(x['Mã cửa hàng'],x['Tên cửa hàng'],
            x['Vốn đầu tư'],x['Doanh thu'],x['Tiền thuế']))
        print("Danh sách cửa hàng sau khi sắp xếp: ")
        print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã cửa hàng','Tên cửa hàng',
                      'Vốn đầu tư','Doanh thu','Tiền thuế'))
        for x in doanh_thu:
            print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(x['Mã cửa hàng'],x['Tên cửa hàng'],
            x['Vốn đầu tư'],x['Doanh thu'],x['Tiền thuế']))
    elif chon==5:
        break
    

 

