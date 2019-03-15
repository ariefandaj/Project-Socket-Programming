#import socket
import socket
#import library untuk threading
import threading

#inisiasi objek socket TC/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind
sock.bind( ("0.0.0.0", 7777) )

#listen permintaan koneksi
sock.listen(100)

#fungsi yang akan di eksekusi pada thread baru
def handle_thread(conn) :
    while True :
        try :
            #menerima data
            data = conn.recv(100)
            #decode jadi string dan ditamabahh Ok di depannya
            data = data.decode("ascii")
            data = "OK "+ data
            #mengirim ke client
            conn.send(data.encode("ascii"))
        except(socket.error) :
            #tutup koneksi ketika client menutup koneksi secara paksa
            conn.close()
            print("client menutup koneksi")
            break

while True :
    #Terima permintaan koneksi
    # - return value : variabel koneksi dan alamat client
    conn, client_addr = sock.accept()
    #buat thread baru
    t = threading.Thread(target=handle_thread, args=(conn,))
    t.start()
