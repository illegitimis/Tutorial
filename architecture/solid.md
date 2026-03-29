# SOLID Programming Principles

The **SOLID** Principles of programming are a good set of rules to follow when you are designing and developing an object oriented application.
> From <cmjackson.net: Solid Programming Principles [1]>

||||
|---|--|---|
| S |Single Responsiblity Principle [2]|A class should do one thing and do it well.  If you can think of more than one reason to change a class, then it has more than one responsibility.|
| O | Open / Closed Principle [3] | A class should be open for extension but closed for modification.  Classes should be designed so they can be inherited from without having to modify them. |
| L | Liskov Substitution Principle [4] | Derived classes must be substitutable for their base class. When a class method accepts an object, the method should be able to accept children of that object without knowing anything about the children. |
| I | Interface Segregation Principle [5] | Interfaces should be fine grained and only provide for your needs. When building your interfaces, you should not add more functionality than what you need at the time. |
| D | Dependency Inversion Principle [6] | High,level modules should not depend on low level modules, but instead both,should depend on abstractions. Interfaces should be used as placeholders,and factory classes should be used to instantiate objects. This causes,loose coupling between classes. |

[<<](../design.md) | [home](../../README.md)

[1]: http://www.cmjackson.net/2009/09/04/solid-programming-principles/
[2]: http://fohjin.blogspot.ro/2008/04/srp-single-responsibility-principle.html
[3]: http://www.eventhelix.com/RealtimeMantra/Object_Oriented/open_closed_principle.htm#.WMc7AvJOIsQ
[4]: https://lostechies.com/chadmyers/2008/03/12/ptom-the-liskov-substitution-principle/
[5]: http://www.oodesign.com/interface-segregation-principle.html
[6]: http://www.oodesign.com/dependency-inversion-principle.html
