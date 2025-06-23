import socket
import threading

def atender(con, addr):
    print(f"[{addr}] conectado")
    try:
        while True:
            data = con.recv(1024)
            if not data:
                break
            print(f"{addr} disse: {data.decode()}")
            con.send(f"OK: {data.decode()}".encode())
    except:
        print(f"Erro com {addr}")
    finally:
        con.close()
        print(f"[{addr}] desconectado")

def servidor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 5555))
    s.listen()
    print("Servidor ligado na porta 5555...")

    while True:
        conn, endereco = s.accept()
        th = threading.Thread(target=atender, args=(conn, endereco))
        th.start()

if __name__ == "__main__":
    servidor()
