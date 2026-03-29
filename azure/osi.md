# OSI Model

> Open Systems Interconnection (OSI)

| Layer | Name | Description |
|---|---|---|
| 7 | application | end-user software: HTTP, FTP, POP, SMTP, DNS |
| 6 | presentation | encode, encrypt, and compress data |
| 5 | session | creates communication channels/session, controls ports |
| 4 | transport | data transmission segments, flow and error control, TCP/UDP |
| 3 | network | breaks up segments into network packets when sending and reassembles on receive, routing |
| 2 | data link | data format over network, establishes and terminates a connection between two physically-connected nodes on a network. Breaks up packets into **frames** and sends them from source to destination. Composed of two parts: Logical Link Control (LLC), which identifies network protocols, performs error checking and synchronizes frames; and Media Access Control (MAC), which uses MAC addresses to connect devices and define permissions to transmit and receive data. |
| 1 | physical | physical cable or wireless connection between network nodes |

[osi-imperva]: https://www.imperva.com/learn/application-security/osi-model/

[<<](./index.md) | [home](../README.md)
