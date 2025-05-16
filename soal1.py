# File: soal1.py
# Sistem Pakar Identifikasi Hama Tanaman

# Fungsi untuk mengidentifikasi hama berdasarkan gejala

def identifikasi_hama(gejala):
    if 'daun_menguning' in gejala and 'bercak_hitam' in gejala:
        return 'Kutu Daun'
    elif 'daun_berlubang' in gejala:
        return 'Ulat'
    elif 'bercak_hitam' in gejala and 'tanaman_layu' in gejala:
        return 'Jamur'
    elif 'daun_menguning' in gejala and 'bercak_hitam' not in gejala:
        return 'Kekurangan Nutrisi'
    else:
        return 'Hama Tidak Diketahui'

# Contoh penggunaan
if __name__ == "__main__":
    gejala_input = ['daun_menguning', 'bercak_hitam']
    hasil = identifikasi_hama(gejala_input)
    print("Jenis hama teridentifikasi:", hasil)
