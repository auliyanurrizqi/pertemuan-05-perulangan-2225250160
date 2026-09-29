print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))
# Lengkapi validasi n dengan while.
while n <= 0:
    print("Banyak suku tidak valid.")
    n = int(input("Banyak suku n: "))
# Lengkapi for untuk menampilkan suku dan menghitung total.
total = 0
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i+1}: {suku}")
print(f"Total deret: {total}")