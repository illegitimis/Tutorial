## Abstraction
A class type defines a data structure that contains data members (fields) and function members (methods, properties, and others). Classes are the most fundamental of C#’s types. A class is a data structure that combines state (fields) and actions (methods and other function members) in a single unit. A class provides a definition for dynamically created instances of the class, also known as objects.

A struct type is similar to a class type in that it represents a structure with data members and function members. However, unlike classes, structs are **value** types and **do not require heap allocation**. 

**Abstraction Is Selective Ignorance **
- Decide what is important and what is not 
- Focus and depend on what is important 
- Ignore and do not depend on what is unimportant 
- Use encapsulation to enforce an abstraction 

> The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise. (_Edsger Dijkstra_) 

 Abstraction is the tactic of stripping an idea or object of its unnecessary accompaniments until you are left with its essential, minimal form. A good abstraction clears away unimportant details and allows you to focus and concentrate on the important details. 

Abstraction is an important software principle. A well-designed class exposes a minimal set of carefully considered methods that provide the essential behavior of the class in an easy-to-use manner. Unfortunately, creating good software abstractions is not easy. Finding good abstractions usually requires a deep understanding of the problem and its context, great clarity of thought, and plenty of experience. 

**Minimal Dependency** The best software abstractions make complex things simple. They do this by ruthlessly hiding away unessential aspects of a class. These unessential aspects, once truly hidden away, cannot then be seen, used, or depended upon in any way. It is this principle of minimal dependency that makes abstraction so important. One of the few things guaranteed in software development is that the code will need to be changed. Perfect understanding only comes at the end of the development process, if it comes at all; early decisions will be made with an incomplete understanding of the problem and will need to be revisited. Specifications will also change when a clearer understanding of the problem is reached. Future versions will require extra functionality. Change is normal in software development. The best you can do is to minimize the impact of change when it happens. And the less you depend on something, the less you are affected when it changes. 

## Polymorphism

> There is nothing more important to understand about C# than inheritance and polymorphism. These concepts are the heart of the language and the soul of object-oriented programming. These issues are the sine qua non of C#. An **implicit conversion** exists _from a class type to any of its base class types_. Therefore, a variable of a class type can reference an instance of that class or an instance of any derived class. For example, given the previous class declarations, a variable of type Point can reference either a `Point` or a `Point3D` (JESSE LIBERTy) 
````csharp
Point a = new Point(10, 20); 
Point b = new Point3D(10, 20, 30); 
````

_Abstract functions are automatically virtual functions_, which allow the programmer to use polymorphism to make their code simpler. When there is a virtual function, the programmer can _pass around a reference to the abstract class_ rather than the derived class, and **the compiler will write code to call the appropriate version of the function at runtime**.
 
Shape, Oval, rectangle, Circle 

This example demonstrates how behavior can be generalized to a base class (Shape) and, through polymorphism, provides a specific implementation of a Draw method for each type of Shape. The beauty of 

polymorphism is that you can introduce new, specialized behaviors for a Shape without altering anything about the client’s fundamental view of a Shape. If you decide you want to add a Square, you can 

add it and it will immediately be on equal footing with any other Shape in the system. 

So, what is parametric polymorphism? Well, instead of achieving polymorphism through inheritance, generics allow you to achieve the functional equivalent by allowing you to parameterize your types. Where regular polymorphism might use a virtual method table to override the methods of a parent object, parametric polymorphism achieves a similar result by allowing a single class to dynamically substitute the types referenced in its internal implementation. This ability to alter a class’s behavior via a type parameter is seen simply as an alternative form of polymorphism, thus the name parametric polymorphism. 

While I think it would be incomplete to discuss generics without including parametric polymorphism, 

it’s also fair to say that the .NET implementation of generics imposes some constraints that limit the 

amount of polymorphic behavior it can achieve. C++ templates are compile time generics. 

Fundamentally, a delegate is meant to serve as a type-safe reference to a method. When you declare 

a delegate, you are only declaring the signature of a method without any corresponding implementation. That delegate is given a name and can then be referenced like any other type. Now, whenever you declare a method with a signature that matches the signature of your delegate, that method (and its implementation) can be passed as a parameter to any method that references your delegate type. So, you could have three different methods that all match your delegate signature and, at runtime, pass any one of these methods as a parameter to another method that includes your delegate in its signature. This essentially gives you an alternative form of polymorphism.

## Inheritance
_Class types_ support **single inheritance** and _polymorphism_, mechanisms whereby derived classes can **extend** and **specialize** base classes. 

> Choosing to support _single rather than multiple inheritance_ on classes eliminates in one stroke many of the complicated corner cases found in multiple inheritance languages.
(ERIC LIPPERT)

**Classes support only single inheritance. Interfaces offer a form of multiple inheritance.** Value types do not support inheritance at all. One reason for this is that value types are not normally used by reference, which removes one of the main benefits of inheritance: runtime polymorphism. Inheritance is not necessarily incompatible with value-like behavior—some languages manage it—but it often has problems. For example, assigning a value of some derived type into a variable of its base type ends up losing all of the fields that the derived type added, a problem known as slicing. C# sidesteps this by restricting inheritance to reference types. When you assign a variable of some derived type into a variable of a base type, you’re copying a reference, not the object itself, so the object remains intact. Slicing is only an issue if the base class offers a method that clones the object, and doesn’t provide a way for derived classes to extend that (or it does, but some derived class fails to extend it).

Interfaces support inheritance, but it’s not quite the same as class inheritance. The syntax is similar, but  an interface can specify multiple base interfaces, because C# supports multiple inheritance for interfaces. The reason .NET supports this despite only offering single implementation inheritance is that most of the complications and potential ambiguities that can arise with multiple inheritance do not apply to purely abstract types.
````csharp
IQueryable<T> : IQueryable, IEnumerable, IEnumerable<T> {}
````


Struct types **do not support user-specified inheritance**, and all struct types implicitly inherit from type object.
> Structs _inherit from object indirectly_. Their implicit direct base class is `System.ValueType`, which in turn _directly inherits from_ `object`. An interface type defines a contract as a named set of public function members.  
A class or struct that implements an interface must provide implementations of the interface’s function members. An interface may inherit from multiple base interfaces, and a class or struct may implement multiple interfaces.
(VLADIMIR RESHETNIkoV)

+ A class declaration may specify a base class by following the class name and type parameters with a _colon_ and the name of the base class. 
+ _Omitting a base class specification_ is the same as **deriving from type object**.
+ A class inherits the members of its base class, _except_ for the **instance and static constructors**, and the **destructors** of the base class.  
+ A derived class can add new members to those it inherits, but it cannot remove the definition of an inherited member.


## Encapsulation
- C# programs use **type declarations** to create new types. A type declaration specifies the name and the members of the new type. 
- Five of C#’s categories of types are _user-definable_: `class` types, `struct` types, `interface` types, `enum` types, and `delegate` types.

When designing objects, the programmer gets to decide how much of the object is visible to the user, and how much is private within the object. Details that aren’t visible to the user are said to be encapsulated in the class. 

In general, the goal when designing an object is to encapsulate as much of the class as possible.  

The most important reasons for doing this are these: 

a) The user can’t change private things in the object, which reduces the chance that the user will either change or depend upon such details in their code. If the user does depend on these details, changes made to the object may break the user’s code. 

b) Changes made in the public parts of an object must remain compatible with the previous version. The more that is visible to the user, the fewer things that can be changed without breaking the user’s code. 

c) Larger interfaces increase the complexity of the entire system. Private fields can only be accessed from within the class; public fields can be accessed through any instance of the class


## Books
> todo: move these book links somewhere else
+ [Code Complete: A Practical Handbook of Software Construction](https://1drv.ms/b/s!As0cxZAk26SzjMBqoNGGDAoyHrlKpQ), Development/Architect, Steve McConnell, 2004, 2ed	
+ The Pragmatic Programmer: From Journeyman to Master; Andrew Hunt & David Thomas. Publisher: Addison Wesley. First Edition October 13, 1999. ISBN: 0-201-61622-X, 352 pages. [1drv](https://1drv.ms/b/s!As0cxZAk26SzjMBr1XLzUux0-93YYw)
+ Mike Rother - Toyota Kata. Managing People for Improvement Adaptiveness and Superior Results - 2009 [1drv](https://1drv.ms/b/s!As0cxZAk26SzjMBsyqaVv3J-wNlYcg)
	
	
[OOP](../OOP.md) | [Home](https://github.com/illegitimis/Tutorial/)