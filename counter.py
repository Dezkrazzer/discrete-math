# ==============================================================
# Anggota Kelompok:
# Gilang Ridho Wicaksana 	L0125044
# Rasyid Yusuf Sugiyono 	L0125028
# Miftahul Habibi 		    L0125084
# Lazuardi Akbar Imani 	    L0125105
# Muhammad Haidar Ramzy 	L0125109
# ==============================================================

def komparasi_solusi(n_maks):
    print(f"{'n':<3} | {'Solusi f(n)':<15} | {'Numerik a_n':<15} | {'Hasil'}")
    print("-" * 55)
    
    a = [0] * n_maks
    
    for n in range(n_maks):
        f_n = (-2)**n - (-3)**n

        if n == 0:
            a[n] = 0
        elif n == 1:
            a[n] = 1
        else:
            a[n] = -5 * a[n-1] - 6 * a[n-2]
            
        is_match = (f_n == a[n])
        
        print(f"{n:<3} | {f_n:<15} | {a[n]:<15} | {is_match}")

komparasi_solusi(11)