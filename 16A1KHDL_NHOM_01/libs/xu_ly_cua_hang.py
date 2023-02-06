import os
import csv
_path="files/ds_cua_hang.csv"
qlcuahang=[]
# Hàm mở file quản lý cửa hàng
def mo_file(_path,qlcuahang):
    f=open(_path,'r', encoding ='utf-8')
    for dong in csv.reader(f):
        if dong[0]=='Mã cửa hàng':
            continue
        qlcuahang.append({'Mã cửa hàng':dong[0],'Tên cửa hàng':dong[1], 'Vốn đầu tư':dong[2],
        'Doanh thu':dong[3],'Tiền thuế':dong[4]})
    f.close()
    print ("Đã mở file ds_cua_hang.csv !")
    return 
  
#Hàm thêm thông tin các cửa hàng
def them_thong_tin(qlcuahang):
    while True:
        ma_ch=input("Nhập mã cửa hàng: ")
        ten_ch=input("Nhập tên cửa hàng: ")
        von_dt=int(input("Nhập vốn đầu tư: "))
        doanh_thu=int(input("Nhập doanh thu: "))
        if von_dt>=50000000:
            tien_thue=float((10/100)*doanh_thu)
            print("Tiền thuế: ",tien_thue)
        else:
            tien_thue=float((5/100)*doanh_thu)
            print("Tiền thuế: ",tien_thue)
        qlcuahang.append({'Mã cửa hàng':ma_ch,'Tên cửa hàng':ten_ch,
        'Vốn đầu tư':von_dt,'Doanh thu':doanh_thu,'Tiền thuế':tien_thue})
        tt=int(input("Bạn có muốn nhập thêm không ? số bất kì: có; 0: không "))
        if tt==0:
            break
    return
#Hàm in danh sách cửa hàng với đầy đủ thông tin
def in_ds(qlcuahang):
    print("Danh sách cửa hàng: ")
    print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã cửa hàng','Tên cửa hàng',
    'Vốn đầu tư','Doanh thu','Tiền thuế'))
    for x in qlcuahang:
        print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(x['Mã cửa hàng'],x['Tên cửa hàng'],
    x['Vốn đầu tư'],x['Doanh thu'],x['Tiền thuế']))
    return
#Hàm lưu file quản lí của hàng
def luu_file(_path,qlcuahang):
    f=open(_path,'w',newline='', encoding = 'utf-8')
    csv.writer(f).writerow(['Mã cửa hàng','Tên cửa hàng','Vốn đầu tư',
    'Doanh thu','Tiền thuế'])
    for ch in qlcuahang:
        csv.writer(f).writerow([ch['Mã cửa hàng'],ch['Tên cửa hàng'], ch['Vốn đầu tư'],
        ch['Doanh thu'],ch['Tiền thuế']])
    f.close()
    print("Đã lưu thông tin vào ds_cua_hang.csv !")
    return 
  
#Hàm tìm cửa hàng theo mã cửa hàng 
def tim_cua_hang(qlcuahang):
    while True: 
        a=input("Nhập mã cửa hàng của cửa hàng cần tìm: ")
        for ch in qlcuahang:
            if ch['Mã cửa hàng']==a:
                print("Cửa hàng cần tìm: ")
                print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã cửa hàng','Tên cửa hàng',
                   'Vốn đầu tư','Doanh thu','Tiền thuế'))
                print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(ch['Mã cửa hàng'],ch['Tên cửa hàng'],
                    ch['Vốn đầu tư'],ch['Doanh thu'],ch['Tiền thuế']))
        tt=int(input("Bạn có muốn tiếp tục không ? số bất kì: có; 0: không "))
        if tt==0:
            break
    return
#Hàm xoá cửa hàng theo mã cửa hàng
def xoa_ch(qlcuahang):
    while True:
        a=input("Nhập mã cửa hàng của cửa hàng cần xoá: ")
        for ch in qlcuahang:
            if ch['Mã cửa hàng']==a:
                vi_tri=qlcuahang.index(ch)
                del(qlcuahang[vi_tri])
                print("Danh sách cửa hàng sau khi xoá: ")
                print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã cửa hàng','Tên cửa hàng',
                'Vốn đầu tư','Doanh thu','Tiền thuế'))
                for x in qlcuahang:
                    print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(x['Mã cửa hàng'],x['Tên cửa hàng'],
                    x['Vốn đầu tư'],x['Doanh thu'],x['Tiền thuế']))
        tt=int(input("Bạn có muốn tiếp tục không ? số bất kì: có; 0: không "))
        if tt==0:
            break
    return

# Hàm thống kê doanh thu
def thong_ke(qlcuahang):
    tong=0
    lstdoanhthu=[]
    for ch in qlcuahang:
        lstdoanhthu.append(ch['Doanh thu'])
        tong+=int(ch['Doanh thu'])
    print('Thống kê doanh thu cửa hàng: ')
    print('{:^20}{:^20}'.format('Tên cửa hàng','Doanh thu'))
    for ch in qlcuahang:
        print('{:^20}{:^20}'.format(ch['Tên cửa hàng'],ch['Doanh thu']))
    print("Tổng doanh thu:",tong)
    print("Trung bình doanh thu:",tong/len(lstdoanhthu))
    return
#Hàm lọc cửa hàng theo vốn đầu tư
def loc(qlcuahang):
    nho_hon=[]
    for ch in qlcuahang:
        if int(ch['Vốn đầu tư'])<50000000:
            nho_hon.append(ch)
    print("Danh sách cửa hàng có vốn đầu tư nhỏ hơn 50 triệu: ")
    print('{:^20}{:^20}'.format('Tên cửa hàng','Vốn đầu tư'))
    for ch in nho_hon:
        print('{:^20}{:^20}'.format(ch['Tên cửa hàng'],ch['Vốn đầu tư']))
    lon_hon=[]
    for ch in qlcuahang:
        if int(ch['Vốn đầu tư'])>=50000000:
            lon_hon.append(ch)
    print("Danh sách cửa hàng có vốn đầu tư lớn hơn 50 triệu: ")
    print('{:^20}{:^20}'.format('Tên cửa hàng','Vốn đầu tư'))
    for ch in lon_hon:
        print('{:^20}{:^20}'.format(ch['Tên cửa hàng'],ch['Vốn đầu tư']))    
            
    return
#Hàm tìm cửa hàng có doanh thu cao nhất
def dt_cao_nhat(qlcuahang):
    doanh_thu = sorted(qlcuahang,reverse=True, key=lambda x: int(x['Doanh thu']))
    a=doanh_thu[0]
    print(" Cửa hàng có doanh thu cao nhất là:",a['Tên cửa hàng'])
    return    
            

