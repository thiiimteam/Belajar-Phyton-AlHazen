def greeting(name):
    print(f"Woy {name}")

greeting("George")
greeting("Kamiel")
greeting("Colapinto")

Sapa = lambda name : print(f"Woy {name}")
Sapa("Carlos")
Sapa("Jude")

def addition(num1, num2):
    hasil = num1 + num2
    return hasil

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number "))

add1 = addition(num1, num2)
print(f"{num1} + {num2} = {add1}")


tambah = lambda num1, num2 : num1 + num2
print(f"14 + 3 = {tambah(14,3)}")

kurang = lambda num1, num2 : num1 - num2
print(f"14 - 3 = {kurang(14,3)}")

kali = lambda num1, num2 : num1 * num2
print(f"14 x 3 = {kali(14,3)}")

bagi = lambda num1, num2 : num1 / num2 if num2 != 0 else "tidak bisa dibagi 0"
print(f"14 : 0 = {bagi(14,0)}")



c_to_f = lambda c : 9 / 5 * c + 32
c_to_k = lambda c : c + 273.15
c_to_r = lambda c : 4 / 5 * c


suhu = float(input("Nasukkan suhu celcius: "))
konversi = input('Konversi ke k/f/r:').lower()
if konversi == 'f':
    print(f"{suhu} derajat celcius = {c_to_f(suhu)} derajat farenheit")
elif konversi == 'k':
    print(f"{suhu} derajat celcius = {c_to_k(suhu)} derajat kelvin")
elif konversi == 'r':
    print(f"{suhu} derajat celcius = {c_to_r(suhu)} derajat reamur")
else :
    print ("gaada")
