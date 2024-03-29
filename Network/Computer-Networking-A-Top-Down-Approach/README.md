# 《计算机网络——自顶向下方法（7nd）》笔记

#### 0. 目标

最近在看计算机网络领域经典的一本书——《计算机网络——自顶向下方法（7nd）》，豆瓣评分到了**9.3**。

毕竟是入门的书，而且是教材，因此难度逐层增加，上手曲线平缓。且配备丰富的课后作业，主要分为：

- 套接字编程
- Wireshark实验

两个部分。

计算机的学习，纸上得来终觉浅，还是要**实践！实践！实践！**

#### 1. 资源

1. [Programming Assignments](https://gaia.cs.umass.edu/kurose_ross/programming.php)
2. [Wireshark Labs](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)

*注意：网站似乎一直在更新。我做的是第八版的（2022.09）。*

#### 2. 套接字作业

##### 2.1 A simple client/server socket program

- 文档：[K_R_sockets_in_Java.pdf](https://gaia.cs.umass.edu/kurose_ross/programming/simple_socket/K_R_sockets_in_Java.pdf)
- 习题：[01 simple_socket_program](https://gaia.cs.umass.edu/kurose_ross/programming/simple_socket/simple_socket_program_PA1.docx)
- 解答：[01 simple_socket_program](./Socket/01_Simple_Socket/Code/)

##### 2.2 Webserver 

- 文档&习题：[WebServer Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/WebServer_programming_lab_only.pdf)
- 解答：[WebServer.py](./Socket/02_WebServer/Code/WebServer.py)

##### 2.3 UDPPingerServer

- 文档&习题：[UDP Pinger Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/UDP_Pinger_programming_lab_only.pdf)
- 解答：[UDPPingerClient.py](./Socket/02_WebServer/Code/UDPPingerClient.py)

##### 2.4 UDPPingerServer

- 文档&习题：[SMTP Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/SMTP_programming_lab_only.pdf)
- 解答：[MailClient.py](./Socket/02_WebServer/Code/MailClient.py)

##### 2.5 ICMP Pinger

- 文档&习题：[ICMP Pinger Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/ICMP_ping_programming_lab_only.pdf)
- 解答：[ICMPPinger.py](./Socket/02_WebServer/Code/ICMPPinger.py)

##### 2.6 ICMP Traceroute Lab

- 文档&习题：[Traceroute Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/Traceroute_programming_lab_only.pdf)
- 解答：[ICMPPinger.py](./Socket/02_WebServer/Code/ICMPTraceroute.py)

##### 2.7 HTTP Web Proxy Server Lab

- 文档&习题：[HTTP Web Proxy Server Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/Web_Proxy_programming_only.pdf)
- 解答：[WebProxy.py](./Socket/02_WebServer/Code/WebProxy.py)

##### 2.8 Video Streaming with RTSP and RTP Lab

- 文档&习题：[Video Streaming with RTSP and RTP Lab](https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/VideoStreaming_programming_lab_only.pdf)
- 解答：

#### 3. Wireshark作业

##### 3.1 Getting Started

- 文档：[Getting Started](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_Intro_v8.0.pdf)

##### 3.2 HTTP

- 文档：[HTTP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_HTTP_v8.0.pdf)

##### 3.3 DNS

- 文档：[DNS](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_DNS_v8.0.pdf)

##### 3.4 TCP

- 文档：[TCP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_TCP_v8.0.pdf)

##### 3.5 UDP

- 文档： [UDP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_UDP_v8.0.pdf)

##### 3.6 IP

- 文档：[IP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_IP_v8.0.pdf)

##### 3.7 NAT

- 文档：[NAT](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_NAT_v8.0.pdf)

##### 3.8 DHCP

- 文档：[DHCP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_DHCP_v8.0.pdf)

##### 3.9 ICMP

- 文档：[ICMP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_ICMP_v8.0.pdf)

##### 3.10 Ethernet and ARP

- 文档：[Ethernet and ARP](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_Ethernet_ARP_v8.0.pdf)

##### 3.11 802.11 WiFi

- 文档：[802.11 WiFi](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_802.11_v8.0.pdf)

##### 3.12 TLS

- 文档：[TLS](http://www-net.cs.umass.edu/wireshark-labs/Wireshark_SSL_v8.0.pdf)

#### 参考

1. [《计算机网络——自顶向下方法（7nd）》](https://book.douban.com/subject/30280001/)
2. [Computer-Networking-A-Top-Down-Approach-NOTES](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)
3. [WIRESHARK LABS](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
4. [ICMP Wikipedia](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol)