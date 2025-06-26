import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Scanner;

public class ClienteSocket {
    public static void main(String[] args) {
        String host = "localhost";
        int porta = 5555;

        try (Socket socket = new Socket(host, porta)) {
            System.out.println("Cliente conectado. Escreva algo ou 'sair' para fechar.");
            
            InputStream in = socket.getInputStream();
            OutputStream out = socket.getOutputStream();
            Scanner scanner = new Scanner(System.in);

            System.out.print("Você: ");
            System.out.flush();

            Thread escutaServidor = new Thread(() -> {
                byte[] buffer = new byte[1024];
                try {
                    int bytesLidos;
                    while ((bytesLidos = in.read(buffer)) != -1) {
                        String resposta = new String(buffer, 0, bytesLidos);

                        System.out.println();
                        System.out.println("-> Resposta: " + resposta);

                        System.out.print("Você: ");
                        System.out.flush();
                    }
                } catch (Exception e) {
                    System.out.println("\nConexão encerrada pelo servidor.");
                }
            });
            escutaServidor.start();

            while (true) {
                String mensagem = scanner.nextLine();
                if (mensagem.strip().equalsIgnoreCase("sair")) {
                    break;
                }

                out.write(mensagem.getBytes());
                out.flush();
            }

            scanner.close();
            socket.close();
            escutaServidor.join();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
