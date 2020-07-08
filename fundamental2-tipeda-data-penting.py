print('tipe data skalar => tipe data sederhana')
anak1 = 'dudu'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'toto'

print('anak1')
print('anak2')
print('anak3')
print('anak4')

print('\ntipe data list/daftar/array')
anak = ['Eko', 'Dwi', 'Tutu', 'Nini']
print(anak)
anak.append('Lika') # Fungsi append ini untuk menambahkan Lika ke dalam variable anak
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[2]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak cara ribet')
for a in range(0, len(anak)): # Fungsi Len untuk menghitung jumlah list, karena kita tidak tau brapa bnyk anak karena sudah append
    print(f'{a+1}. Hai {anak[a]}')