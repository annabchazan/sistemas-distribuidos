import socket
import asyncio

async def escutar_servidor(sock):
    while True:
        dados = await asyncio.to_thread(sock.recv, 1024)
        if not dados:
            break
        print("-> Resposta:", dados.decode())

async def cliente():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 5555))

    print("Cliente conectado. Escreva algo ou 'sair' para fechar.")

    tarefa_escuta = asyncio.create_task(escutar_servidor(sock))

    while True:
        texto = input("Você: ")
        if texto.strip().lower() == "sair":
            break
        sock.send(texto.encode())

    sock.close()
    await tarefa_escuta

if __name__ == "__main__":
    asyncio.run(cliente())
