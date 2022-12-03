# Dari episode 60 :
# cara melihat pip :
# di windows powershell/cmd/running di python, ketik pip + enter.
# Kalo mau liat versi pip : pip --version + enter
# Kalo mau liat list package yang ada di pip kita : pip list + enter

import numpy as np

# print(numpy)

'''bikin vektor matriks'''
vector_a = np.array([1,2,3,4])

## bedanya pake array sama list 
list_a = [1,2,3,4]
print(list_a)
### kalo dioperasikan, hasilnya error, misal :
# print(list_a**5)
# kalo dikali dua, maka listnya ditulis dua kali, bukan jadi operasi matematika, misal
# print(list_a*2)
print(vector_a)
### kalo diperasikan, bisa 
print(vector_a**2)
print(vector_a*4)

'''bikin matriks 2x2'''
matrix_b = np.array([(1,2),(2,5)])
print(matrix_b**2)

'''bikin matriks 0'''
zeros_c = np.zeros((2,2)) # angka 2,2 menunjukkan matriks 2x2
print(zeros_c)

'''bikin matriks 1'''
ones_d = np.ones((2,2))
print(ones_d)

'''operasi matriks'''
jumlah = matrix_b + matrix_b**2 + ones_d
print(jumlah)