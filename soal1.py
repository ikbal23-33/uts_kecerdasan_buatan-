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

def masukkan_gejala():
    print("Masukkan gejala satu per satu. Ketik 'selesai' jika sudah selesai.")
    gejala = []
    while True:
        input_gejala = input("Gejala: ").strip().lower()
        if input_gejala == 'selesai':
            break
        if input_gejala != '':
            gejala.append(input_gejala)
    return gejala

if __name__ == "__main__":
    gejala_input = masukkan_gejala()
    hasil = identifikasi_hama(gejala_input)
    print("Jenis hama teridentifikasi:", hasil)
