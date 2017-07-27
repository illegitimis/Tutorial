# SOLID Programming Principles 

The SOLID Principles of programming are a good set of rules to follow when you are designing and developing an object oriented application. 

|   |                                 |                                                                                                                                                                                                                                                               |
|---|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S |  [Single Responsiblity Principle](http://fohjin.blogspot.ro/2008/04/srp-single-responsibility-principle.html) |                                                       A class should do one thing and do it well.  If you can think of more than one reason to change a class, then it has more than one responsibility.                                                      |
| O |     [Open / Closed Principle](http://www.eventhelix.com/RealtimeMantra/Object_Oriented/open_closed_principle.htm#.WMc7AvJOIsQ)     |                                                   A class should be open for extension but closed for modification.  Classes should be designed so they can be inherited from without having to modify them.                                                  |
| L |  [Liskov Substitution Principle](https://lostechies.com/chadmyers/2008/03/12/ptom-the-liskov-substitution-principle/)  |                          Derived classes must be substitutable for their base class. When a class method accepts an object, the method should be able to accept children of that object without knowing anything about the children.                          |
| I | [Interface Segregation Principle](http://www.oodesign.com/interface-segregation-principle.html) |                                            Interfaces should be fine grained and only provide for your needs.  When building your interfaces, you should not add more functionality than what you need at the time.                                           |
| D |  [Dependency Inversion Principle](http://www.oodesign.com/dependency-inversion-principle.html) | High,level modules should not depend on low level modules, but instead both,should depend on abstractions.  Interfaces should be used as placeholders,and factory classes should be used to instantiate objects.  This causes,loose coupling between classes. |

> From <http://www.cmjackson.net/2009/09/04/solid-programming-principles/> 


[[<<|OOP]]