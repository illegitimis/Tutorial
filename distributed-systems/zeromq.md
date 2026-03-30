---
title: ZeroMQ
layout: default
nav_order: 9
parent: Distributed Systems
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# ZeroMQ

## Table of Contents

- [ZeroMQ base](#zeromq-base)
  - [Socket types and NetMQ counterparts](#socket-types-and-netmq-counterparts)
  - [Socket pairs](#socket-pairs)
- [NetMQ](#netmq)
  - [Sacha barber demos](#sacha-barber-demos)
  - [ZeroMQ and services](#zeromq-and-services)

## ZeroMQ Base

### Socket Types and NetMQ Counterparts

| ZeroMQ pattern | NetMQ corresponding class | comments |
|---|---|---|
| PUB | PublisherSocket | used to publish messages |
| SUB | SubscriberSocket | subscribe to message(s) |
| XPUB | XPublisherSocket | used to publish messages. _XPUB and XSUB are used where you may have to bridge different networks_. |
| XSUB | XSubscriberSocket | used to subscribe to message(s) where you may have to bridge different networks |
| REQ | RequestSocket | _synchronous blocking socket_, that would initiate a request message. |
| REP | ResponseSocket | synchronous blocking socket, that would provide a response to a message. |
| ROUTER | RouterSocket | broker socket. _Fully asynchronous_ (non blocking). tracks every connection. identity frame. **ROUTER is like an asynchronous REP socket** |
| DEALER | DealerSocket | Dealer is typically a _worker_ socket, and doesn't provide any routing (ie it doesn't know about the calling sockets identity), but it is fully asynchronous (non blocking). **DEALER is like an asynchronous REQ socket**. |
| PUSH | PushSocket | push messages at worker, within a pipeline pattern |
| PULL | PullSocket | within a _pipeline_ pattern, which would pull from a PUSH socket and then do some work. |
| PAIR | PairSocket | PairSocket |

### Socket Pairs

ROUTER Broker and REQ Workers.

| Standard ZeroMQ Socket Pairs | comments |
|---|---|
| PUB and SUB | Pub/Sub arrangement |
| XPUB and XSUB | Pub/Sub arrangement |
| REQ/DEALER and REP/ROUTER | _In the same way that we can replace REQ with DEALER ….we can replace REP with ROUTER. This gives us an asnchronous server that can talk to multiple REQ clients at the same time._ . Where we use a REQ socket, we can use a DEALER; we just have to read and write the envelope ourselves. Where we use a REP socket, we can stick a ROUTER; we just need to manage the identities ourselves |
| REQ client talking to a REP server | A **standard synchronous request/response** arrangement. The REQ client must initiate the message flow |
| REQ and ROUTER | A _standard synchronous request_ with an _asynchronous server_ responding, where the router will know how to do the routing back the correct request socket |
| DEALER and REP | An _asynchronous request_ with a _synchronous server_ responding. When we use a standard REQ (ie not a DEALER for the client) socket, it does one extra thing for us, which is to include an empty frame. So when we switch to using a Dealer for the client, we need to do that part ourselves, by using **SendMore** |
| DEALER and ROUTER | _An asynchronous request with an asynchronous server responding_, where the router will know how to do the routing back the correct request socket. ROUTER Broker and DEALER Workers. 1-to-N use case where one server talks asynchronously to multiple workers. Turn this upside down to get a very useful N-to-1 architecture where various clients talk to a single server, and do this asynchronously |
| DEALER and DEALER | An asynchronous request with an asynchronous server responding (this should be used if the DEALER is talking to one and only one peer). |
| ROUTER and ROUTER | An asynchronous request with an asynchronous server responding. perfect for N-to-N connections, but it's the most difficult combination to use. |
| PUSH and PULL | Push socket connected to a Pull, which you may see in a **divide and conquer type arrangement**. |
| PAIR and PAIR | Pair sockets _should ONLY talk to another pair_, it is a well defined pair, Typically you would use this for **connecting two threads in a process**. |

In the request-reply pattern, the message envelope holds the return address for replies. It is how a ŘMQ network with no state can create round-trip request-reply dialogs.

The ŘMQ reply envelope formally consists of zero or more reply addresses, followed by an empty frame (the envelope delimiter), followed by the message body (zero or more frames). The envelope is created by multiple sockets working together in a chain.

- zguide [7]
- cs:hwclient [8]
- cs:hwserver [9]
- hintjens blog [10]
- 0mq Labs [11]
- 0mq Messaging Presentation Slides Pdf [12]
- **(Pieter Hintjens) ZeroMQ: Messaging for Many Applications (ebook)** [13]
- [**(Pieter Hintjens) ZeroMQ: Messaging for Many Applications (local)**](../../CARTI/0mq/2013.Zeromq.Messaging.For.many.Applications.pdf)

## NetMQ

Update: As of 2014 C# binding (CLRZMQ) is no longer maintained and NetMQ is the default choice for ZeroMQ and .Net.

Update: As of 2014 NetMQ is a stable project with a growing community and is in production use by multiple companies.

January 20th, 2016

| Id | Version | Description | Authors | DownloadCount |
|---|---|---|---|---|
| NetMQ | 3.3.2.2 | **A 100% native C# port of the lightweight high performance messaging library ZeroMQ** | NetMQ | 36985 |
| clrzmq | 2.2.5 | The clrzmq project contains .NET bindings for ŘMQ (ZeroMQ), an open source, high performance transport layer. Includes a compiled version of the native libzmq library. WARNING: This package targets the x86 build platform. | zeromq | 25312 |
| clrzmq-x64 | 2.2.5 | The clrzmq project contains .NET bindings for ŘMQ (ZeroMQ), an open source, high performance transport layer. Includes a compiled version of the native libzmq library. WARNING: This package targets the x64 build platform. | zeromq | 10238 |
| ZeroMQ | 4.1.0.17 | ZeroMQ CLR namespace | metadings, Pieter Hintjens, Martin Sustrik | 7272 |

- netmq-asp-net [14]
- netmq-xpub-xsub [15]
- ZeroMQ-NetMq-Quick-Intro [16]
- Comparing OpenDDS and ZeroMQ Usage and Performance [17]
- SO tag netmq [18]
- NetMQ on GitHub [19]

## Sacha Barber Demos

- **All demos on GitHub** [20]
- zeromq-1-introduction [21] _request response pattern, single client and server, multiple clients and server in a single process, multiple clients Running In Separate Threads and a server_
- ZeroMQ #2 : The Socket Types [22]
- ZeroMQ #3 : Socket Options/Identity And SendMore [23]
- ZeroMQ #4 : Multiple Sockets Polling [24]
- ZeroMQ #5 : Sending From Multiple Sockets [25]
- ZeroMQ #6: Divide And Conquer [26]
- ZeroMQ #7: A Simple Actor Model [27] _ventilator, sink, workers_

## ZeroMQ and Services

- WebAPI-or-WCF [28]
- NetMQ-RX-Streaming-Data-Demo-App [29]
- Lightweihjt rpc 0mq and proto [30]
- omq and proto [31]
- rpcz [32]
- zmqpbexample [33]
- cpp zmq_protobuf [34]
- brokerless whitepaper zguide [35]
- NetMQRxDemo Sacha [36]

[7]: http://zguide.zeromq.org/php:all
[8]: http://zguide.zeromq.org/cs:hwclient
[9]: http://zguide.zeromq.org/cs:hwserver
[10]: http://hintjens.com/blog:86
[11]: http://zeromq.org/docs:labs
[12]: http://zeromq.wdfiles.com/local--files/area%3Awhitepapers/messaging-2010-02-17.pdf
[13]: http://www.reedbushey.com/89Zeromq.pdf
[14]: http://somdoron.com/2014/08/netmq-asp-net/
[15]: http://netmq.readthedocs.org/en/latest/xpub-xsub/
[16]: http://blog.scottlogic.com/2015/03/20/ZeroMQ-Quick-Intro.html
[17]: http://mnb.ociweb.com/mnb/MiddlewareNewsBrief-201004.html
[18]: http://stackoverflow.com/questions/tagged/netmq
[19]: https://github.com/zeromq/netmq
[20]: https://github.com/sachabarber/ZeroMqDemos
[21]: https://sachabarbs.wordpress.com/2014/08/19/zeromq-1-introduction/
[22]: https://sachabarbs.wordpress.com/2014/08/21/zeromq-2-the-socket-types-2/
[23]: https://sachabarbs.wordpress.com/2014/08/26/zeromq-3-socket-optionsidentity-and-sendmore/
[24]: https://sachabarbs.wordpress.com/2014/08/27/zeromq-4-multiple-sockets-polling/
[25]: https://sachabarbs.wordpress.com/2014/08/30/zeromq-sending-from-multiple-sockets/
[26]: https://sachabarbs.wordpress.com/2014/09/01/zeromq-6-divide-and-conquer/
[27]: https://sachabarbs.wordpress.com/2014/09/05/zeromq-7-a-simple-actor-model/
[28]: http://mattmilner.com/Milner/Blog/post/2012/02/28/WebAPI-or-WCF.aspx
[29]: http://www.codeproject.com/Articles/853476/NetMQplus-RX-Streaming-Data-Demo-App-of
[30]: http://blogs.mulesoft.com/biz/mule/lightweight-rpc-with-%C3%B8mq-and-protocol-buffers/
[31]: http://www.dotkam.com/2011/09/09/zeromq-and-google-protocol-buffers/
[32]: https://github.com/thesamet/rpcz
[33]: https://github.com/joshrotenberg/zmqpbexample
[34]: http://docs.biicode.com/c++/examples/zmq_protobuf.html
[35]: http://zeromq.org/whitepapers:brokerless
[36]: https://github.com/sachabarber/NetMQRxDemo

[<](./index.md) | [<<](/index.md)
