"""
Tipe data ductuibary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Vallue Pair
dictionary = kamus

tipe data dict ditandai dengan {}
"""

# Contoh kamus indo to english
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

# Contoh kamus english to indo
kamus_eng_ind = {'son': 'anak', 'wife': 'istri', 'father': 'ayah', 'mother': 'ibu'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_eng_ind['mother'])

print('\nData ni dikirimkan oelh server gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-07-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak':10},
        {'nama': 'Dwi','jarak': 100},
        {'nama': 'Tutu', 'jarak': 1000},
        {'nama': 'Nini', 'jarak': 10000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Jarak driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
