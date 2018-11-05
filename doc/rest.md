# REST


## Links
+ [**Zalando API design principles**](http://zalando.github.io/restful-api-guidelines/design-principles/DesignPrinciples.html)
+ [Thoughts on RESTful API Design](http://restful-api-design.readthedocs.io/en/latest/), _Geert Jansen_, 2012
+ [_The Atom Publishing Protocol_ (RFC text)](https://tools.ietf.org/rfc/rfc5023.txt)  
+ [Registry of link relations](http://www.iana.org/assignments/link-relations/link-relations.xhtml)
+ [Call a REST API](./rest/call.md) from .NET
[![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./rest/call.md)
+ [Web API](./rest/webapi.md) general, recipes and design principles
[![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./rest/webapi.md)
+ [Web API upload & download files](./rest/webApiUpDownLoad.md) 
[![wiki page](https://img.shields.io/badge/wiki-page-green.svg)](./rest/webApiUpDownLoad.md)
+ [Microsoft REST API Guidelines](https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md) 

## Principles / constraints of REST
1. An important principle for (RESTful) API design and usage is Postel's Law, aka the [Robustness Principle](https://en.wikipedia.org/wiki/Robustness_principle) (_RFC 1122_): “**Be liberal in what you accept, be conservative in what you send**.” 
2. [REST APIs must be hypertext-driven](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven) 
3. Resource-Oriented Architecture (ROA) Representational State Transfer, or REST 
4. SOAP, WSDL, and the WS-* stack = Big web services. _Big Web Services don’t expose resources_. The Web is based on URIs and links, but a typical Big Web Service exposes one URI and zero links.
5. [HATEOAS](https://www.crummy.com/writing/speaking/2008-QCon/act2.html) hypermedia-as-the-engine-of-application-state 
6. Client-Server
7. **Stateless Server**: No side effects on the server when calls are made into it. No State Preserved between  requests. Can't lean on older ideas, like _ASP.NET Session State_, or even _Application State_. This would include authentication information on each call.
8. **Cache and ETags**. There isn't extra work being pushed onto the system for every request. No data store roundtrip unless necessary. Cache also implies that we're going to use some mechanic to version the object that was retrieved from the server, _not just the ID_, _but also the version of that_. 
9. *Uniform Interface*. Broken down into: the _Identification of Resources_, the Representations that support _modification_, Self-Description, and HATEOAS.
10. _Layered System_: client -> firewall -> gateway (proxy) -> load balancer -> multiple servers.
11. *Code On-Demand* optional by Fleming, ability to deliver code to be run by client.

## Books
+ [**Architectural Styles and the Design of Network-based Software Architectures**](http://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf), 
[_Roy Thomas Fielding_](http://www.ics.uci.edu/%7Efielding/), 2000, [_also html_](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) 
+ [**Richardson Maturity Model**, steps toward the glory of REST](http://martinfowler.com/articles/richardsonMaturityModel.html), _Martin Fowler_, 2010
+ [**Restful** Web Services](https://www.crummy.com/writing/RESTful-Web-Services/RESTful_Web_Services.pdf), Leonard Richardson & Sam Ruby, 2007, 
[source code](http://restinpractice.com/book/sourcecode.html), 
[alternative](https://1drv.ms/b/s!As0cxZAk26SzjMAr1KDVcWXr5H6A7w)
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!As0cxZAk26SzjMAr1KDVcWXr5H6A7w)
+ [REST in Practice: Hypermedia and Systems Architecture](http://www.seoexpertcompany.com/aa.php?isbn=ISBN:9780596805821&name=REST_in_Practice), Webber, Parastatidis, Robinson, 2010 (google book)
+ [**RESTful Service Best Practices**/](http://www.restapitutorial.com/media/RESTful_Best_Practices-v1_1.pdf)_Recommendations for Creating Web Services_, 
[alternative](https://1drv.ms/b/s!As0cxZAk26SzjMAq2NbJI_KV1raiWg)
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://1drv.ms/b/s!As0cxZAk26SzjMAq2NbJI_KV1raiWg)
+ [**REST in Practice**](http://www.slideshare.net/guilhermecaelum/rest-in-practice), The slides for the REST tutorial that Ian Robinson and Jim Webber gave at QCON 

## COURSES
+ __Web API Design__ by Wildermuth 
[slides](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2), 
[![One Drive](https://img.shields.io/badge/One-Drive-blue.svg)](https://onedrive.live.com/embed?cid=B3A4DB2490C51CCD&resid=B3A4DB2490C51CCD%21204889&authkey=AJdXhKx3Nh8gzvo&em=2)
course [link](https://app.pluralsight.com/library/courses/web-api-design/table-of-contents)
+ _Implementing an API in ASP.NET Web API_ by Shawn Wildermuth on [Pluralsight](https://app.pluralsight.com/library/courses/implementing-restful-aspdotnet-web-api/)
[![Pluralsight course page](https://img.shields.io/badge/Pluralsight-course-lightgrey.svg)](https://app.pluralsight.com/library/courses/implementing-restful-aspdotnet-web-api/)

## http-decision-diagram
- [readme](https://github.com/for-GET/http-decision-diagram/blob/master/doc/README.md)
- ![pic](https://raw.githubusercontent.com/for-GET/http-decision-diagram/master/httpdd.png) 3250x2146, v4.0.201410
- [httpdd](http://for-get.github.io/http-decision-diagram/httpdd.fsm.html) html diagram
- [RFC2616](https://www.w3.org/Protocols/rfc2616/rfc2616.html), Hypertext Transfer Protocol -- HTTP/1.1

[home](./README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 