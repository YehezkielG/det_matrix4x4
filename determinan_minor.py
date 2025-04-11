import sympy as sp  # Untuk menampilkan matriks dengan format yang bagus
import time  # Untuk memberikan efek delay

# Hitung determinan matriks secara rekursif menggunakan ekspansi kofaktor
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]  # Basis 1x1
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Basis 2x2
    
    # Rekursi untuk matriks berordo lebih besar
    return sum(((-1) ** c) * matrix[0][c] * determinant(
        [row[:c] + row[c+1:] for row in matrix[1:]]
    ) for c in range(len(matrix)))

# Fungsi untuk menerima input matriks
def inputMatrix(ordo, name):
    print(f"\nMatrix {name}")
    matrix = []
    for i in range(ordo):
        strInput = input(f"Masukkan nilai pada baris ke-{i+1} : ")
        strInput = " ".join(strInput.split())
        rows = [int(n) for n in strInput.split(" ")]
        if len(rows) != ordo:
            print("Jumlah kolom tidak sesuai. Coba lagi!")
            return inputMatrix(ordo, name)  # Validasi input
        matrix.append(rows)
    return matrix

# Tampilkan langkah-langkah perhitungan determinan
def steps(matrix):
    minorDet = []
    for c in range(len(matrix)):  # Iterasi untuk ekspansi kofaktor kolom pertama
        subMatrix = [row[:c] + row[c+1:] for row in matrix[1:]]  # Minor matriks
        minorDet.append(determinant(subMatrix))  
        print(f"Determinan dari matrix minor C 1-{c+1} = {minorDet[c]}")  # Cetak sub-determinan
    det = 0  # Inisialisasi determinan
    print("\nDet(A) = ")
    for c in range(len(minorDet)):  
        element = matrix[0][c]  
        sign = (-1) ** c  
        det += sign * element * minorDet[c]  # Penjumlahan ekspansi kofaktor

        # Cetak proses ekspansi kofaktor
        if c == len(minorDet):
            print(f"({sign})({element})({minorDet[c]})", end="")
        else:
            print(f"({sign})({element})({minorDet[c]}) + ", end="")
    print(f" = {det}")  # Cetak hasil akhir determinan

# Efek delay untuk simulasi loading
def delay(loading):
    for _ in range(20):
        time.sleep(0.1)
        print(loading, end="")

ordo = int(input("Masukkan baris dan kolom matrix : "))
print("<Pisahkan nilai antar kolom dengan spasi>")
matrix_A = inputMatrix(ordo, "A")

delay("-")  # Efek loading
print("\n\nMatriks A :")
print(sp.pretty(sp.Matrix(matrix_A)))

print("\nPenyelesaian :")
steps(matrix_A)