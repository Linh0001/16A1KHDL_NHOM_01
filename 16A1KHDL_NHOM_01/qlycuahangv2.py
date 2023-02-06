#  NHÓM SỐ 01 16A1KHDL
#  22174600004 LÊ ĐÌNH TÙNG
#  22174600011 NGUYỄN VĂN DUY
#  22174600005 HUỲNH NGỌC TƯỜNG VI
#  22174600001 PHÙNG THỊ LINH
#  22174600012 TRƯƠNG ANH ĐỨC
_path="files/ds_cua_hang.csv"
print("CHƯƠNG TRÌNH QUẢN LÝ CỬA HÀNG:")
while True:
    print("1: Mở file quản lí cửa hàng")
    print("2: Thêm thông tin các cửa hàng")
    print("3: In danh sách cửa hàng")
    print("4: Lưu file quản lí cửa hàng")
    print("5: Tìm cửa hàng theo mã cửa hàng")
    print("6: Xoá cửa hàng theo mã cửa hàng")
    print("7: Thống kê doanh thu")
    print("8: Lọc cửa hàng theo vốn đầu tư")
    print("9: Cửa hàng có doanh thu cao nhất")
    print("10: Thoát chương trình")
    chon=int(input('Chọn chức năng cần thực hiện: '))
    from libs.xu_ly_cua_hang import*
    if chon==1:
        mo_file(_path,qlcuahang)
    elif chon==2:
        them_thong_tin(qlcuahang)
    elif chon==3:
        in_ds(qlcuahang)
    elif chon==4:
        luu_file(_path,qlcuahang)
    elif chon==5:
        a=tim_cua_hang(qlcuahang)
        if a==0:
            print("Không tồn tại cửa hàng")
    elif chon==6:
        xoa_ch(qlcuahang)
    elif chon==7:
        thong_ke(qlcuahang)
    elif chon==8:
        loc(qlcuahang)
    elif chon==9:
        dt_cao_nhat(qlcuahang)
    elif chon==10:
        break
        

