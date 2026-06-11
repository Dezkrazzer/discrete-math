import math

def solusi_analitik(c1, c2, a0, a1):
    print("=== KODE 1: PENYELESAIAN ANALITIK (PERSAMAAN KARAKTERISTIK) ===")
    print(f"Persamaan rekursi: a_n + {c1}a_{{n-1}} + {c2}a_{{n-2}} = 0")
    print(f"Kondisi awal: a_0 = {a0}, a_1 = {a1}\n")
    
    # 1. Bentuk persamaan karakteristik r^2 + c1*r + c2 = 0
    # Menggunakan rumus kuadratik (rumus ABC) untuk mencari akar r1 dan r2
    diskriminan = c1**2 - 4*1*c2
    
    # Karena kita tahu diskriminannya positif untuk kasus ini (25 - 24 = 1)
    if diskriminan > 0:
        r1 = int((-c1 + math.sqrt(diskriminan)) / 2)
        r2 = int((-c1 - math.sqrt(diskriminan)) / 2)
        
        print(f"Akar-akar persamaan (r1, r2): {r1} dan {r2}")
        print(f"Bentuk Umum: a_n = A({r1})^n + B({r2})^n\n")
        
        # 2. Mencari Konstanta A dan B dari a_0 dan a_1
        # Sistem persamaannya:
        # A + B = a0  =>  B = a0 - A
        # A*r1 + B*r2 = a1
        
        # Substitusi: A*r1 + (a0 - A)*r2 = a1
        # A*r1 - A*r2 = a1 - a0*r2
        # A = (a1 - a0*r2) / (r1 - r2)
        
        A = (a1 - a0 * r2) / (r1 - r2)
        B = a0 - A
        
        A = int(A)
        B = int(B)
        
        print(f"Sistem Persamaan:")
        print(f"A + B = {a0}")
        print(f"{r1}A + {r2}B = {a1}")
        print(f"Diperoleh nilai A = {A}, B = {B}\n")
        
        # 3. Format hasil akhir (Generating Function & Persamaan Karakteristik akan tiba di kesimpulan yang sama)
        tanda_B = "+" if B >= 0 else "-"
        print(f"Solusi Akhir: a_n = {A}({r1})^n {tanda_B} {abs(B)}({r2})^n")
        # Disederhanakan jika A=1
        if A == 1 and B == -1:
            print(f"Bentuk sederhana: a_n = ({r1})^n - ({r2})^n")

# Menjalankan fungsi dengan c1=5, c2=6, a0=0, a1=1
solusi_analitik(5, 6, 0, 1)