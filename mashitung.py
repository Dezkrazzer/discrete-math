def komparasi_solusi(n_maks):
    #tabel header
    print(f"{'n':<3} | {'Solusi f(n)':<15} | {'Numerik a_n':<15} | {'Hasil'}")
    print("-" * 55)
    
    # Inisialisasi list/array untuk menyimpan riwayat perhitungan numerik
    a = [0] * n_maks
    
    # Looping sesuai pseudocode: for n range (0, 10)
    for n in range(n_maks):
        # 1. Perhitungan Analitik (Rumus Solusi)
        f_n = (-2)**n - (-3)**n
        
        # 2. Perhitungan Numerik (Rekursi manual)
        if n == 0:
            a[n] = 0
        elif n == 1:
            a[n] = 1
        else:
            # Nilai saat ini bergantung pada dua nilai sebelumnya
            a[n] = -5 * a[n-1] - 6 * a[n-2]
            
        # 3. Logika pengecekan (if left == right)
        is_match = (f_n == a[n])
        
        # Mencetak hasil ke dalam baris tabel
        print(f"{n:<3} | {f_n:<15} | {a[n]:<15} | {is_match}")

# Memanggil fungsi untuk range 0 sampai 9
komparasi_solusi(10)