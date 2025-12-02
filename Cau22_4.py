print(" Sinh vien: Dau Van Khanh Duc")
print(" MSV : 245752021610021")
ket_qua = []
for num in range(1000, 3001):
    s = str(num)
    if all(int(d) % 2 == 0 for d in s):
        ket_qua.append(s)

print(','.join(ket_qua))
