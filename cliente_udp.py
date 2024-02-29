import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente UDP criado com sucesso')

hot = 'localhost'
porta = 5433
mensagem = 'Olá servidor, de boa?'

try:
    print(f'Cliente {mensagem}')
    s.sendto(mensagem.encode(), (hot, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente {dados}')
finally:
    print(f'Cliente: fechando a conexão')
    s.close()