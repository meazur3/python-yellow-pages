import os

#action:
#main action
# q: quit
# >: next page
# <: prev page
# s: search
# a: add
# u: update
# d: delete

#search action
# s: search again
# c: clear search
# q: quit


yellow_pages = [
    {'name': 'Achmad Fauzi', 'number': '086789012345'},
    {'name': 'Achmad Setiawan', 'number': '088901234567'},
    {'name': 'Aditya Nugraha', 'number': '081234567890'},
    {'name': 'Bayu Pratama', 'number': '083456789012'},
    {'name': 'Bella Suci', 'number': '087890123456'},
    {'name': 'Bella Utami', 'number': '089012345678'},
    {'name': 'Bunga Sari', 'number': '082345678901'},
    {'name': 'Cahya Pratama', 'number': '083456789012'},
    {'name': 'Cahya Surya', 'number': '080123456789'},
    {'name': 'Cakra Pratama', 'number': '088901234567'},
    {'name': 'Citra Kusuma', 'number': '084567890123'},
    {'name': 'Dewi Anggraini', 'number': '084567890123'},
    {'name': 'Dian Ayu', 'number': '089012345678'},
    {'name': 'Dian Rosita', 'number': '081234567890'},
    {'name': 'Dwi Septiani', 'number': '085678901234'},
    {'name': 'Edo Prakoso', 'number': '086789012345'},
    {'name': 'Eko Saputra', 'number': '080123456789'},
    {'name': 'Eko Susanto', 'number': '085678901234'},
    {'name': 'Eko Wibowo', 'number': '082345678901'},
    {'name': 'Fira Safitri', 'number': '083456789012'},
    {'name': 'Fitria Utami', 'number': '087890123456'},
    {'name': 'Fitriani Putri', 'number': '086789012345'},
    {'name': 'Galih Pratama', 'number': '082345678901'},
    {'name': 'Galih Satria', 'number': '084567890123'},
    {'name': 'Gilang Ramadhan', 'number': '088901234567'},
    {'name': 'Gunawan Surya', 'number': '087890123456'},
    {'name': 'Hana Putri', 'number': '088901234567'},
    {'name': 'Heni Wijayanti', 'number': '089012345678'},
    {'name': 'Hesty Rahayu', 'number': '083456789012'},
    {'name': 'Irfan Hakim', 'number': '089012345678'},
    {'name': 'Iqbal Ramadhan', 'number': '084567890123'},
    {'name': 'Iqbal Wijaya', 'number': '086789012345'},
    {'name': 'Ivan Setiawan', 'number': '080123456789'},
    {'name': 'Jihan Putri', 'number': '087890123456'},
    {'name': 'Jihan Safitri', 'number': '085678901234'},
    {'name': 'Juwita Dewi', 'number': '081234567890'},
    {'name': 'Juwita Indah', 'number': '087890123456'},
    {'name': 'Kresna Wijaya', 'number': '082345678901'},
    {'name': 'Krisna Adi', 'number': '088901234567'},
    {'name': 'Krisna Wijaya', 'number': '082345678901'},
    {'name': 'Kusuma Wardani', 'number': '081234567890'},
    {'name': 'Laras Putri', 'number': '087890123456'},
    {'name': 'Laras Wulandari', 'number': '089012345678'},
    {'name': 'Lina Agustina', 'number': '083456789012'},
    {'name': 'Lukman Hakim', 'number': '082345678901'},
    {'name': 'Maulana Indra', 'number': '088901234567'},
    {'name': 'Maulana Surya', 'number': '080123456789'},
    {'name': 'Mega Puspita', 'number': '083456789012'},
    {'name': 'Mochamad Rizki', 'number': '084567890123'},
    {'name': 'Nadia Putri', 'number': '085678901234'},
    {'name': 'Nadia Pratiwi', 'number': '087890123456'},
    {'name': 'Nanda Pratama', 'number': '084567890123'},
    {'name': 'Nia Kusuma', 'number': '089012345678'},
    {'name': 'Nia Pratiwi', 'number': '081234567890'},
    {'name': 'Oktavia Sari', 'number': '084567890123'},
    {'name': 'Oscar Simanjuntak', 'number': '082345678901'},
    {'name': 'Putra Wijaya', 'number': '086789012345'},
    {'name': 'Putra Perdana', 'number': '081234567890'},
    {'name': 'Putri Ayuningrum', 'number': '083456789012'},
    {'name': 'Putri Lestari', 'number': '086789012345'},
    {'name': 'Putri Wulandari', 'number': '085678901234'},
    {'name': 'Rahmat Hidayat', 'number': '088901234567'},
    {'name': 'Rahmat Setiawan', 'number': '081234567890'},
    {'name': 'Rendy Pratama', 'number': '086789012345'},
    {'name': 'Ria Putri', 'number': '084567890123'},
    {'name': 'Rika Widiastuti', 'number': '085678901234'},
    {'name': 'Rio Pratama', 'number': '087890123456'},
    {'name': 'Risa Anggraeni', 'number': '082345678901'},
    {'name': 'Rizki Pratama', 'number': '088901234567'},
    {'name': 'Rudi Setiawan', 'number': '081234567890'},
    {'name': 'Santi Puji', 'number': '088901234567'},
    {'name': 'Sari Mulyani', 'number': '083456789012'},
    {'name': 'Satria Wibowo', 'number': '086789012345'},
    {'name': 'Setiawan Guna', 'number': '083456789012'},
    {'name': 'Silvia Anggraini', 'number': '082345678901'},
    {'name': 'Siska Wijaya', 'number': '084567890123'},
    {'name': 'Surya Adi', 'number': '086789012345'},
    {'name': 'Tania Putri', 'number': '087890123456'},
    {'name': 'Teguh Setiawan', 'number': '088901234567'},
    {'name': 'Toni Saputra', 'number': '083456789012'},
    {'name': 'Tri Utami', 'number': '085678901234'},
    {'name': 'Umar Firmansyah', 'number': '088901234567'},
    {'name': 'Vicky Prasetyo', 'number': '081234567890'},
    {'name': 'Vina Agustina', 'number': '083456789012'},
    {'name': 'Vivi Permata', 'number': '089012345678'},
    {'name': 'Wahyu Prasetyo', 'number': '084567890123'},
    {'name': 'Wahyu Wijaya', 'number': '080123456789'},
    {'name': 'Widi Setiawan', 'number': '086789012345'},
    {'name': 'Widya Ayu', 'number': '085678901234'},
    {'name': 'Winda Lestari', 'number': '088901234567'},
    {'name': 'Wulan Sari', 'number': '088901234567'},
    {'name': 'Yoga Prakoso', 'number': '086789012345'},
    {'name': 'Yoga Pratama', 'number': '087890123456'},
    {'name': 'Yoga Setiawan', 'number': '081234567890'},
    {'name': 'Yoga Wijaya', 'number': '086789012345'},
    {'name': 'Yoga Ramadhan', 'number': '089012345678'},
    {'name': 'Yuli Wulandari', 'number': '084567890123'},
    {'name': 'Zahra Cahyaningrum', 'number': '087890123456'},
    {'name': 'Zainal Abidin', 'number': '085678901234'},
    {'name': 'Zulfikar Setiawan', 'number': '086789012345'}
];
header = "| {:<5} | {:<20} | {:<15} |".format("Index", "Name", "Number")
line = '-' * len(header)
page = 1
size = 10
search = ''
wrong_action = False
notify = ''

def is_valid_index(i, data):
    return 0 <= i < len(data)

def is_int(data):
    try:
        hasil = int(data)
        return True
    except ValueError as e:
        return False
    
def ceiling(num):
    return int(-(-num // 1))

def filter_data(data,search_value):
    searched = []
    if(search_value!=''):
        for elm in data:
            if(search_value.lower() in elm['name'].lower() or search_value.lower() in elm['number'].lower()):
                searched.append(elm)
    else:
        searched = data
    return searched

def show_header():
    print(line)
    print(header)
    print(line)
    
def show_action(ln,_page,_size):
    action = " 'q': quit"
    if(len(search)==0):
        action = f"'s': search | 'a': add | 'u': update | 'd': delete | {action}"
    else:
        action = f"'s': search again | 'c':clear search | {action}"
    if(_page < (ln/_size)):
        action = f"'>': next page | {action}"
    if(_page > 1):
        action = f"'<': prev page | {action}"
    print(line)
    print(action)
    print(line)


def show_data(data,_page,_size):
    ln = len(data)
    # print(ln,_size)
    show_header()
    pfrom = (_page-1)*_size
    pto = (_page-1)*_size + _size
    # print(pfrom,pto,ln)
    for i in range(pfrom,pto):
        if(i<len(data)):
            print("| {:<5} | {:<20} | {:<15} |".format((i+1),data[i]['name'], data[i]['number']))
    print(line)
    print("| Total: {:<21} | {:>6} of {:<6}|".format(ln,_page,ceiling(ln/_size)))
    
def reset():
    page = 1
    size = 10

while True:
    if(wrong_action == False):
        os.system('cls' if os.name == 'nt' else 'clear') 
        data = filter_data(yellow_pages,search)
        show_data(data,page,size)
        if not notify=='':
            print(line)
            print(notify)
            notify = ''
        show_action(len(data),page,size)
    command = input('Show the action: ').lower()
    if(command == 'q'):
        break
    elif(command == 'a' or command == 'u' or command=='d'):
        idx = 0
        no_hp = ''
        nama = ''
        if command == 'u' or command=='d':
            idx = -1
            while not (is_int(idx) and int(idx)>=0 and int(idx)<len(data)):
                idx = input('Masukkan Index: ')
                idx = int(idx) - 1
                if not (is_int(idx) and int(idx)>=0 and int(idx)<len(data)):
                    print(f'Index {idx} harus string / tidak ada di dalam table')
        if(command=='a' or command=='u'):
            while nama == '':
                nama = input('Masukkan nama: ')
                if nama=='':
                    print('Nama tidak boleh kosong')
            while not (no_hp.startswith('08') and len(no_hp)==12 and is_int(no_hp)):
                no_hp = input('Masukkan nomor hp (awalan 08): ')
                if not (no_hp.startswith('08') and len(no_hp)==12 and is_int(no_hp)):
                    print('Format nomor hp tidak berawalan 08 dan 12 angka dan berisi angka semua')
        if(command=='a'):
            yellow_pages.insert(int(idx),{'name':nama,'number':no_hp})
            notify = f"Sukses insert nama: {nama} dengan number: {no_hp} di index {idx+1}"
        elif(command=='u'):
            yellow_pages[idx] = {'name':nama,'number':no_hp}
            notify = f"Sukses update nama: {nama} dengan number: {no_hp} di index {idx+1}"
        elif(command=='d'):
            notify = f"Sukses delete data di index 1"
            yellow_pages.pop(idx)
        wrong_action = False
    elif(command == 's'):
        search = input('Input what you search:')
        reset()
        wrong_action = False
    elif(command == 'c'):
        reset()
        search = ''
        wrong_action = False
    elif(command == '>' and page < len(data)/size):
        page = page+1
        wrong_action = False
    elif(command == '<' and page > 1):
        page = page-1
        wrong_action = False
    else:
        print('Wrong action, try again')
        wrong_action = True
    

