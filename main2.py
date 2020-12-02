print ("selamat target anda sukses,, mohon cek penyimpanan ") 
for x in range(2):
    f = open(f"worm{x}.txt","w")
    f.write("Selamat termux anda saya isi dengan text")
f.close()
