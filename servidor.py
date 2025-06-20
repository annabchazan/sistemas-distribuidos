import socket
import threading

def tratar_cliente(conexao, endereco):
    print(f"[+] Nova conexão de {endereco}")
    while True:
        try:
            dados = conexao.recv(1024)
            if not dados:
                break
            mensagem = dados.decode()
            print(f"[{endereco}] {mensagem}")
            conexao.send(f"Recebido: {mensagem}".encode())
        except:
            break
    print(f"[-] Conexão encerrada com {endereco}")
    conexao.close()

def iniciar_servidor(host='127.0.0.1', porta=5555):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"[🟢] Servidor ouvindo em {host}:{porta}")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
