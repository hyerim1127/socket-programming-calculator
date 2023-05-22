import socket

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버에 연결
    client_socket.connect((host, port))
    print('Server Connected')

    # 수식 입력
    expression = input('Enter the Formula : ')

    # 수식 전송
    client_socket.send(expression.encode())

    # 서버로부터 결과 수신
    response = client_socket.recv(1024).decode()

    if response.startswith('Error Occurred'):
        print(response)
    else:
        print('Calculate Result :', response)

    # 클라이언트 소켓 종료
    client_socket.close()

if __name__ == '__main__':
    main()
