# message maker 

from termcolor import colored
import qrcode

print(" ")

pesan = input("Tulis Pesannya : ")
nama_file = input("Nama File Nya  : ")
png = (nama_file , ".png")
img=qrcode.make(data=pesan)
img.save(nama_file)

cpesan = (colored(pesan,'green'))
cfile = (colored(nama_file,'green'))


print(" ")
print ("Pesannya             :",cpesan)
print ("Disimpan Dengan Nama :",cfile)
print(" ")
