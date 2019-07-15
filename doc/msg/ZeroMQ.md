# ZeroMQ

## table of contents

- [ZeroMQ base](https://github.com/illegitimis/Tutorial/blob/v10/ZeroMQ.md#zeromq-base)
  - [Socket types and NetMQ counterparts](https://github.com/illegitimis/Tutorial/blob/v10/ZeroMQ.md#socket-types-and-netmq-counterpart)s
  - [Socket pairs](https://github.com/illegitimis/Tutorial/wiki/ZeroMQ#socket-pairs)
- [NetMQ](https://github.com/illegitimis/Tutorial/wiki/ZeroMQ#netmq)
  - [Sacha barber demos](https://github.com/illegitimis/Tutorial/wiki/ZeroMQ#sacha-barber-demos)
  - [ZeroMQ and services](https://github.com/illegitimis/Tutorial/wiki/ZeroMQ#zeromq-and-services)

## ZeroMQ base

### Socket types and NetMQ counterparts

<div id="socketTypes">

<table>
<thead class="hed">
<tr>
<th>ZeroMQ pattern</th>
<th>NetMQ corresponding class</th>
<th>comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>PUB</td>
<td>PublisherSocket</td>
<td>used to publish messages</td>
</tr>
<tr>
<td>SUB</td>
<td>SubscriberSocket</td>
<td>subscribe to message(s)</td>
</tr>
<tr>
<td>XPUB</td>
<td>XPublisherSocket</td>
<td>used to publish messages. <span class="lite">XPUB and XSUB are used where you may have to bridge different networks</span>.</td>
</tr>
<tr>
<td>XSUB</td>
<td>XSubscriberSocket</td>
<td>used to subscribe to message(s) where you may have to bridge different networks</td>
</tr>
<tr>
<td>REQ</td>
<td>RequestSocket</td>
<td><span class="lite">synchronous blocking socket</span>, that would initiate a request message.</td>
</tr>
<tr>
<td>REP</td>
<td>ResponseSocket</td>
<td>synchronous blocking socket, that would provide a response to a message.</td>
</tr>
<tr>
<td>ROUTER</td>
<td>RouterSocket</td>
<td>broker socket. <span class="lite">Fully asynchronous</span> (non blocking). tracks every connection. identity frame. <span class="dark">ROUTER is like an asynchronous REP socket</span></td>
</tr>
<tr>
<td>DEALER</td>
<td>DealerSocket</td>
<td>Dealer is typically a <span class="lite">worker</span> socket, and doesn’t provide any routing (ie it doesn’t know about the calling sockets identity), but it is fully asynchronous (non blocking). <span class="dark">DEALER is like an asynchronous REQ socket</span>.</td>
</tr>
<tr>
<td>PUSH</td>
<td>PushSocket</td>
<td>push messages at worker, within a pipeline pattern</td>
</tr>
<tr>
<td>PULL</td>
<td>PullSocket</td>
<td>within a <span class="lite">pipeline</span> pattern, which would pull from a PUSH socket and then do some work.</td>
</tr>
<tr>
<td>PAIR</td>
<td>PairSocket</td>
<td>PairSocket</td>
</tr>
</tbody>
</table>
</div>

### Socket pairs

<div id="socketPairs">ROUTER Broker and REQ Workers.
<table>
<thead class="hed">
<tr>
<th>Standard ZeroMQ Socket Pairs</th>
<th>comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>PUB and SUB</td>
<td>Pub/Sub arrangement</td>
</tr>
<tr>
<td>XPUB and XSUB</td>
<td>Pub/Sub arrangement</td>
</tr>
<tr>
<td>REQ/DEALER and REP/ROUTER</td>
<td>_In the same way that we can replace REQ with DEALER ….we can replace REP with ROUTER. This gives us an asnchronous server that can talk to multiple REQ clients at the same time._ . Where we use a REQ socket, we can use a DEALER; we just have to read and write the envelope ourselves. Where we use a REP socket, we can stick a ROUTER; we just need to manage the identities ourselves</td>
</tr>
<tr>
<td>REQ client talking to a REP server</td>
<td>A <span class="dark">standard synchronous request/response</span> arrangement. The REQ client must initiate the message flow</td>
</tr>
<tr>
<td>REQ and ROUTER</td>
<td>A <span class="lite">standard synchronous request</span> with an <span class="lite">asynchronous server</span> responding, where the router will know how to do the routing back the correct request socket</td>
</tr>
<tr>
<td>DEALER and REP</td>
<td>An <span class="lite">asynchronous request</span> with a <span class="lite">synchronous server</span> responding. When we use a standard REQ (ie not a DEALER for the client) socket, it does one extra thing for us, which is to include an empty frame. So when we switch to using a Dealer for the client, we need to do that part ourselves, by using <span class="dark">SendMore</span></td>
</tr>
<tr>
<td>DEALER and ROUTER</td>
<td><span class="lite">An asynchronous request with an asynchronous server responding</span>, where the router will know how to do the routing back the correct request socket. ROUTER Broker and DEALER Workers. 1-to-N use case where one server talks asynchronously to multiple workers. Turn this upside down to get a very useful N-to-1 architecture where various clients talk to a single server, and do this asynchronously</td>
</tr>
<tr>
<td>DEALER and DEALER</td>
<td>An asynchronous request with an asynchronous server responding (this should be used if the DEALER is talking to one and only one peer).</td>
</tr>
<tr>
<td>ROUTER and ROUTER</td>
<td>An asynchronous request with an asynchronous server responding. perfect for N-to-N connections, but it’s the most difficult combination to use.</td>
</tr>
<tr>
<td>PUSH and PULL</td>
<td>Push socket connected to a Pull, which you may see in a <span class="dark">divide and conquer type arrangement</span>.</td>
</tr>
<tr>
<td>PAIR and PAIR</td>
<td>Pair sockets <span class="lite">should ONLY talk to another pair</span>, it is a well defined pair, Typically you would use this for <span class="dark">connecting two threads in a process</span>.</td>
</tr>
</tbody>
</table>
</div>
<div>
In the request-reply pattern, the message envelope holds the return address for replies. It is how a ŘMQ network with no state can create round-trip request-reply dialogs.

The ŘMQ reply envelope formally consists of zero or more reply addresses, followed by an empty frame (the envelope delimiter), followed by the message body (zero or more frames). The envelope is created by multiple sockets working together in a chain.

- [zguide](http://zguide.zeromq.org/php:all)
- [cs:hwclient](http://zguide.zeromq.org/cs:hwclient)
- [cs:hwserver](http://zguide.zeromq.org/cs:hwserver)
- [hintjens blog](http://hintjens.com/blog:86)
- [0mq Labs](http://zeromq.org/docs:labs)
- [0mq Messaging Presentation Slides Pdf](http://zeromq.wdfiles.com/local--files/area%3Awhitepapers/messaging-2010-02-17.pdf)
- [**(Pieter Hintjens) ZeroMQ: Messaging for Many Applications (ebook)**](http://www.reedbushey.com/89Zeromq.pdf)
- [**(Pieter Hintjens) ZeroMQ: Messaging for Many Applications (local)**](../../CARTI/0mq/2013.Zeromq.Messaging.For.many.Applications.pdf )

## NetMQ

Update: As of 2014 C# binding (CLRZMQ) is no longer maintained and NetMQ is the default choice for ZeroMQ and .Net.

Update: As of 2014 NetMQ is a stable project with a growing community and is in production use by multiple companies.

January 20th, 2016

<div id="nuget">

<table>

<thead class="hed">

<tr>

<th>Id</th>

<th>Version</th>

<th>Description</th>

<th>Authors</th>

<th>DownloadCount</th>

</tr>

</thead>

<tbody>

<tr>

<td>NetMQ</td>

<td>3.3.2.2</td>

<td class="dark">A 100% native C# port of the lightweight high performance messaging library ZeroMQ</td>

<td>NetMQ</td>

<td>36985</td>

</tr>

<tr>

<td>clrzmq</td>

<td>2.2.5</td>

<td>The clrzmq project contains .NET bindings for ŘMQ (ZeroMQ), an open source, high performance transport layer. Includes a compiled version of the native libzmq library. WARNING: This package targets the x86 build platform.</td>

<td>zeromq</td>

<td>25312</td>

</tr>

<tr>

<td>clrzmq-x64</td>

<td>2.2.5</td>

<td>The clrzmq project contains .NET bindings for ŘMQ (ZeroMQ), an open source, high performance transport layer. Includes a compiled version of the native libzmq library. WARNING: This package targets the x64 build platform.</td>

<td>zeromq</td>

<td>10238</td>

</tr>

<tr>

<td>ZeroMQ</td>

<td>4.1.0.17</td>

<td>ZeroMQ CLR namespace</td>

<td>metadings, Pieter Hintjens, Martin Sustrik</td>

<td>7272</td>

</tr>

</tbody>

</table>

</div>

- [netmq-asp-net](http://somdoron.com/2014/08/netmq-asp-net/)
- [netmq-xpub-xsub](http://netmq.readthedocs.org/en/latest/xpub-xsub/)
- [ZeroMQ-NetMq-Quick-Intro](http://blog.scottlogic.com/2015/03/20/ZeroMQ-Quick-Intro.html)
- [Comparing OpenDDS and ZeroMQ Usage and Performance](http://mnb.ociweb.com/mnb/MiddlewareNewsBrief-201004.html)
- [SO tag netmq](http://stackoverflow.com/questions/tagged/netmq)
- [NetMQ on GitHub](https://github.com/zeromq/netmq)

## Sacha barber demos

- [**All demos on GitHub**](https://github.com/sachabarber/ZeroMqDemos)
- [zeromq-1-introduction](https://sachabarbs.wordpress.com/2014/08/19/zeromq-1-introduction/) <label class="lite">request response pattern, single client and server, multiple clients and server in a single process, multiple clients Running In Separate Threads and a server</label>
- [ZeroMQ #2 : The Socket Types](https://sachabarbs.wordpress.com/2014/08/21/zeromq-2-the-socket-types-2/)
- [ZeroMQ #3 : Socket Options/Identity And SendMore](https://sachabarbs.wordpress.com/2014/08/26/zeromq-3-socket-optionsidentity-and-sendmore/)
- [ZeroMQ #4 : Multiple Sockets Polling](https://sachabarbs.wordpress.com/2014/08/27/zeromq-4-multiple-sockets-polling/)
- [ZeroMQ #5 : Sending From Multiple Sockets](https://sachabarbs.wordpress.com/2014/08/30/zeromq-sending-from-multiple-sockets/)
- [ZeroMQ #6: Divide And Conquer](https://sachabarbs.wordpress.com/2014/09/01/zeromq-6-divide-and-conquer/)
- [ZeroMQ #7: A Simple Actor Model](https://sachabarbs.wordpress.com/2014/09/05/zeromq-7-a-simple-actor-model/) <label class="lite">ventilator, sink, workers</label>

## ZeroMQ and services

- [WebAPI-or-WCF](http://mattmilner.com/Milner/Blog/post/2012/02/28/WebAPI-or-WCF.aspx)
- [NetMQ-RX-Streaming-Data-Demo-App](http://www.codeproject.com/Articles/853476/NetMQplus-RX-Streaming-Data-Demo-App-of)
- [Lightweihjt rpc 0mq and proto](http://blogs.mulesoft.com/biz/mule/lightweight-rpc-with-%C3%B8mq-and-protocol-buffers/)
- [omq and proto](http://www.dotkam.com/2011/09/09/zeromq-and-google-protocol-buffers/)
- [rpcz](https://github.com/thesamet/rpcz)
- [zmqpbexample](https://github.com/joshrotenberg/zmqpbexample)
- [cpp zmq_protobuf](http://docs.biicode.com/c++/examples/zmq_protobuf.html)
- [brokerless whitepaper zguide](http://zeromq.org/whitepapers:brokerless)
- [NetMQRxDemo Sacha](https://github.com/sachabarber/NetMQRxDemo)

</div>

[<<](../messaging.md) | [home](../../README.md)