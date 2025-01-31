file = open('woe.txt', 'r')
print(file.read())
# Ini buat baca File, buat bikin file pake 'x'

file = open('woe.txt', 'w')
file.write("Selamat Pagi")
file.close()
# Ini buat nulis isi/konten

file = open('woe.txt', 'a')
file.write("\n")
file.write("Selamat Siang")
file.close()
#Ini buat nulis baris yang baru

with open("woe.txt", "w") as file:
    file.write("Hay Gaes, Capybara nih \n")
print(f'status file: {file.closed}')
# buat nulis tapi pake with biar langsung ke tutup

with open("woe.txt", "a") as file:
    file.write("Selamat Pagi \n")
print(f'status file: {file.closed}')

with open("woe.txt", "a") as file:
    file.write("Pagi \n")
print(f'status file: {file.closed}')
# sama kaya atas, tapi ini buat bikin baris baru

file = open ('woe.txt', 'r')
print(file.readline())
print(file.readlines())