import socket
import ast

def handle_client(client_socket):
    # 수식 수신
    expression = client_socket.recv(1024).decode()
    print('Received Formula :', expression)

    try:
        # 수식 계산
        result = eval(expression)
        result_str = str(result)
        print('Calculate Result :', result_str)

        # 결과 전송
        client_socket.send(result_str.encode())
        print('Result sent')
    except Exception as e:
        error_message = 'Error Occurred'
        client_socket.send(error_message.encode())
        print('Error Message Send', error_message)
        print('Error Message', str(e))

    client_socket.close()

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 소켓을 주소에 바인딩
    server_socket.bind((host, port))

    # 클라이언트의 연결 요청 대기
    server_socket.listen(1)
    print('Server Started')

    while True:
        # 클라이언트와 연결 수락
        # addr = 서버와 연결된 클라이언트의 주소 정보
        client_socket, addr = server_socket.accept()
        print('Client Connected')
        print('Client Addr :', addr)

        # 클라이언트 요청 처리
        handle_client(client_socket)

if __name__ == '__main__':
    main()
