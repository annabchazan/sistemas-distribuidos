import socket
import threading
from datetime import datetime

def responder(mensagem):
    mensagem = mensagem.strip().lower()

    if mensagem == "oi":
        return "Olá! Como posso ajudar?"
    elif mensagem == "tudo bem":
        return "Tudo ótimo! E com você?"
    elif mensagem == "hora":
        return datetime.now().strftime("Agora são %H:%M:%S.")
    elif mensagem == "data":
        return datetime.now().strftime("Hoje é %d/%m/%Y.")
    elif mensagem == "ajuda":
        return "Comandos disponíveis: oi, tudo bem, hora, data, tchau."
    elif mensagem == "tchau":
        return "Tchau! Foi bom falar com você."
    else:
        return "Desculpe, não entendi. Digite 'ajuda' para ver os comandos."

def atender(con, addr):
    print(f"[{addr}] conectado")
    try:
        while True:
            data = con.recv(1024)
            if not data:
                break
            mensagem = data.decode()
            print(f"{addr} disse: {mensagem}")
            
            resposta = responder(mensagem)
            con.send(resposta.encode())
    except:
        print(f"Erro com {addr}")
    finally:
        con.close()
        print(f"[{addr}] desconectado")

def servidor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 5555))
    s.listen()
    print("Servidor ligado na porta 5555...")

    while True:
        conn, endereco = s.accept()
        th = threading.Thread(target=atender, args=(conn, endereco))
        th.start()

if __name__ == "__main__":
    servidor()
