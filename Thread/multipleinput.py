# Import socket
import socket
# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# kirim permintaan koneksi ke alamat IP dan port Server
sock.connect( ("127.0.0.1", 7777) )
# kirim data ke server 
stop = "x"
while True :
    data = input("Masukan Kalimat ( untuk stop masukan x ): ")
#data = "Selamat Pagi"
    sock.send(data.encode("ascii"))
#stop looping
    if data == stop :
        break
# Terima data balsan dari server
    data = sock.recv(100)
# decode dan cetak
    data  = data.decode("ascii")
    print(data)