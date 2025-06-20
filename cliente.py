import socket
import asyncio

async def receber_respostas(sock):
    loop = asyncio.get_event_loop()
    while True:
        dados = await loop.run_in_executor(None, sock.recv, 1024)
        if not dados:
            break
        resposta = dados.decode()
        tratar_mensagem(resposta)

def tratar_mensagem(mensagem):
    print(f"[🔁 Callback] Servidor respondeu: {mensagem}")

async def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5555))

    asyncio.create_task(receber_respostas(sock))

    print("[✉️] Envie mensagens (digite 'sair' para encerrar)")
    while True:
        msg = input("> ")
        if msg.lower() == 'sair':
            break
        sock.send(msg.encode())

    sock.close()

if __name__ == "__main__":
    asyncio.run(main())
