# Program Hitung Gaji Karyawan
print("=" * 50)
print("PROGRAM HITUNG GAJI KARYAWAN")
print("=" * 50)

# Input data karyawan
nama_karyawan = input("Nama Karyawan\t\t: ")
golongan_jabatan = input("Golongan Jabatan (1-3)\t: ")
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Jumlah jam kerja\t: "))

print("\n" + "=" * 50)
print("LAYOUT KELUARAN")
print("=" * 50)

# Gaji pokok
gaji_pokok = 300000

# Hitung tunjangan jabatan
if golongan_jabatan == "1":
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan_jabatan == "2":
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan_jabatan == "3":
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0

# Hitung tunjangan pendidikan
if pendidikan.upper() == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan.upper() == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan.upper() == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan.upper() == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0

# Hitung honor lembur
jam_normal = 8
honor_per_jam = 3500

if jam_kerja > jam_normal:
    jam_lembur = jam_kerja - jam_normal
    honor_lembur = jam_lembur * honor_per_jam
else:
    honor_lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Output hasil
print(f"Karyawan yang bernama {nama_karyawan}")
print(f"Honor yang diterima")
print(f"Tunjangan Jabatan\t: Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan\t: Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur\t\t: Rp {honor_lembur:,.0f}")
print(f"\nTotal Gaji\t\t: Rp {total_gaji:,.0f}")
print("=" * 50)