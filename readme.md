# Projeto de Sistemas Distribuídos – Comunicação Cliente/Servidor

Este projeto simula a comunicação entre um cliente e um servidor em uma arquitetura distribuída ponto a ponto. Foram realizadas duas formas de execução, ambas utilizando comunicação via sockets TCP/IP entre máquinas conectadas na mesma rede local.

---

## 🌐 Objetivo

Demonstrar o funcionamento básico de um sistema distribuído, onde cliente e servidor trocam mensagens por meio de sockets TCP/IP, permitindo a comunicação entre máquinas distintas. O projeto também evidencia a interoperabilidade entre linguagens e a execução em ambientes reais e distribuídos.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagens:** Python (servidor) e Java (cliente)
- **Comunicação:** Sockets TCP/IP
- **Ambiente:** Máquinas reais conectadas à mesma rede local

---

## ⚙️ Modos de Execução

### 🔹 Execução 1: Máquina Virtual + Máquina Física

- **Servidor:** Python rodando em uma máquina virtual com Linux
- **Cliente:** Java rodando no VS Code em uma máquina física com Windows
- **Objetivo:** Demonstrar interoperabilidade entre linguagens diferentes e execução em ambientes distintos (VM e host)

### 🔹 Execução 2: Três Máquinas Físicas (todas Windows)

- **Servidor:** Python rodando em uma máquina física com Windows
- **Cliente:** Java rodando em outra máquina física com Windows
- **Terceira máquina:** Utilizada para observação, testes adicionais ou execução de múltiplos clientes
- **Objetivo:** Demonstrar execução totalmente distribuída em três máquinas físicas reais com sistema operacional igual, evidenciando a troca de mensagens em rede local.

---

## 📁 Estrutura do Projeto

```bash
Sistemas-distribuidos/
├── cliente/
│   └── Cliente.java
├── servidor/
│   └── servidor.py
└── README.md
```
