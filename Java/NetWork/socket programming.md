# Socket

* TCP/IP 네트워크를 이용하여 쉽게 통신 프로그램을 작성하도록 지원하는 기술

### 1. 소켓
* 두 응용 프로그램 간의 양방향 통신 링크의 한쪽 끝 단을 의미
* 소켓끼리 데이터를 주고받음
* 소켓은 특정 IP 포트 번호와 결합함
* 서버 소켓과 클라이언트 소켓이 존재
* 자바로 소켓 통신할 수 있는 라이브러리를 지원함
    * `java.net` 패키지
    * `Socket` 생성자 : 연결되지 않은 상태의 소켓 생성
    * `Socket(InetAddress address, int port)` 생성자 : 소켓을 생성하고, 지정된 IP 주소(address)와 포트 번호(port)에서 대기하는 원격 응용프로그램의 소켓에 연결
    * `Socket(String host, int port)` 생성자 : 소켓을 생성하여 지정된 호스트(host)와 포트 번호(port)에 연결한다. 호스트 이름이 null인 경우는 루프백 주소로 가정.