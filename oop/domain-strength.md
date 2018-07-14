# Strengthening your domain

_30 March, 2010_. _Jimmy Bogard._

## toc

+ [Services in Domain-Driven Design](https://lostechies.com/jimmybogard/2008/08/21/services-in-domain-driven-design/)
+ [primer](https://lostechies.com/jimmybogard/2010/02/04/strengthening-your-domain-a-primer/)
+ [Aggregate Construction](https://lostechies.com/jimmybogard/2010/02/24/strengthening-your-domain-aggregate-construction/)
+ [Encapsulated collections](https://lostechies.com/jimmybogard/2010/03/10/strengthening-your-domain-encapsulated-collections/)
+ [Encapsulating operations](https://lostechies.com/jimmybogard/2010/03/24/strengthening-your-domain-encapsulating-operations/)
+ [The double dispatch pattern](https://lostechies.com/jimmybogard/2010/03/30/strengthening-your-domain-the-double-dispatch-pattern/)

***

## services

Services are **first-class citizens** of the domain model. When concepts of the model would _distort_ any Entity or Value Object, a Service is appropriate.

A good Service has these characteristics:
+ The operation relates to a domain concept that is _not a natural part_ of an Entity or Value Object
+ The interface is defined _in terms of_ other elements in the domain model
+ The operation is **stateless**

Services are always exposed as an interface, not for “swappability”, testability or the like, but to expose a set of cohesive operations in the form of a contract. On a sidenote, it always bothered me when people say that an interface with one implementation is a design smell. No, an interface is used to expose a contract. Interfaces communicate design intent, far better than a class might.

But most examples I see of Services are something trivial, such as `IEmailSender`. But Services exist in most layers of the DDD layered architecture: _Application_, _Domain_, _Infrastructure_.

An _Infrastructure Service_ would be something like our `IEmailSender`, that _communicates directly with external resources_, such as the file system, registry, SMTP, database, etc.  Something like NHibernate would show up in the Infrastructure.

_Domain services_ are the **coordinators**, allowing higher level functionality between many different smaller parts.  These would include things like `OrderProcessor`, `ProductFinder`, `FundsTransferService`, and so on. Since Domain Services are first-class citizens of our domain model, their names and usages should be part of the Ubiquitous Language. _Meanings and responsibilities_ **should make sense** to the stakeholders or domain experts.

In many cases, the software we write is replacing or supplementing a human’s job, such as _Order Processor_, so it’s often we find inspiration in the existing business process for names and responsibilities. Where an existing name doesn’t fit, we dive into the domain to try and surface a hidden concept with the domain expert, which might have existed but didn’t have a name.

Finally, we have _Application Services_. In many cases, Application Services are the **interface used by the outside world**, where the outside world can’t communicate via our Entity objects, but may have other representations of them. Application Services could map outside messages to internal operations and processes, communicating with services in the Domain and Infrastructure layers to provide cohesive operations for outside clients. Messaging patterns tend to rule Application Services, as the other service layers don’t have a reference back out to the Application Services. _Business rules are not allowed in an Application Service_, those belong in the Domain layer.

In top-down design, we typically start from the Application or Domain Service, defining the actual interface clients use, then use TDD to drive out the implementation. As we’re always starting from the client perspective with actual client scenarios, we get a high degree of confidence that what we’re building will create success and add value.  When stories are vertical slices of functionality, this is fairly straightforward, at least mechanically so.

I used to make the mistake of dismissing Services as a necessary evil, I’ve started to realize the potential the Application and Domain services have in creating a well-designed model.

***

## primer
### Code smells
A lot of DDD is just plain good OO programming. Unit tests and code smells are the best indication that our domain is wrong, along with conversations with our domain experts. In systems that start to move beyond merely CRUD, _specific code smells start to surface that should indicate that our system is starting to accumulate behavior_, but it just might not be in the right place. In a behavior-rich, but anemic domain, the domain is surrounded by a multitude of services that do the actual work, and fiddle with state on our domain objects. The domain objects _contain state to be persisted_, but it’s _not the domain objects themselves exposing any operations_. But this is just code smell! Lots of code smells indicate that our domain is not as rich as at could be. The behavior is out there, but just needs to be moved around. Some smells I look for include:
+ Primitive Obsession
+ Data Class
+ Inappropriate Intimacy
+ Lazy Class
+ Feature Envy
+ Middle Man

All these are smells between classes, where usually a domain service is waaaay to concerned with a set of entities, when behavior could just be moved down into those entities.

### Aggregate Roots
One of the most quoted, but most misunderstood ideas in DDD is the concept of `aggregate roots`. But what is this aggregate root? Is it just an entity with a screen in front of it? A row in a database? Evans defined a set of rules for Aggregates:
+ The root Entity has **global identity** and is _ultimately responsible for checking invariants_
+ Entities inside the boundary have _local identity_, **unique only within the Aggregate**.
+ _Nothing outside_ the Aggregate boundary can hold a reference to anything inside, except to the root Entity. The root Entity _can hand references to the internal Entities_ to other objects, but they can only use them **transiently** (within a single method or block).
+ Only Aggregate Roots can be obtained _directly_ with database queries. Everything else must be done through **traversal**.
+ Objects within the Aggregate _can hold references_ to other Aggregate roots.
+ A _delete_ operation **must remove everything within the Aggregate boundary all at once**
+ When a _change_ to any object within the Aggregate boundary is _committed_, _all invariants of the whole Aggregate must be satisfied_.
+ It’s a lot, but I generally think of Aggregate roots as consistency boundaries. **When I interact with an Aggregate, its invariants must always be satisfied**. Keeping invariants satisfied strengthens the design and responsibility of the objects, as the logic that defines the Aggregate is then self-contained.

### Strategic Design
We may not like it, but not all of our system’s model will ever reach our vision of perfection. Which is fine, as a perfect model across our entire system would be _prohibitively expensive_ with little ROI on all that work.  Instead, we have to focus on specific areas of the core domain that provide the most value to the customer. The better our core domain model, the better our system represents the conceptual model we’ve defined with our customers, and the better we will be able to serve their needs.

Unfortunately, all the interesting _Strategic Design_ chapters are after the basic DDD patterns in the book, so that many folks get lost discussing repositories, entities, aggregates and so on. But in recent interviews, Evans mentions that these later discussions are more important than the earlier ones. The bottom line is that we have to choose carefully where we spend our time refining our domain model. Some areas will not be as refined as others, but that’s perfectly acceptable. The trick is to find which areas will give us the most value for our time spent in refactoring, refinement and modeling.
Finally, it’s worth noting that there is no “best” design. There is only the **best design given our current understanding**. _Software development is a process of discovery_, where concepts that seemed unimportant or hidden may suddenly become obvious and critical later. That’s still normal, and not a negative thing. Lots of concepts around an idea will be thrown around, but only the most important ones will rise to the top, and sometimes that just takes time.

***

## Aggregate Construction

Our application complexity has hit its tipping point, and we decide to move past [anemic domain models](http://martinfowler.com/bliki/AnemicDomainModel.html) to rich, behavioral models.  But what is this anemic domain model?  Let's look at Fowler's definition, now over 6 years old:

> The basic symptom of an Anemic Domain Model is that at first blush it looks like the real thing. There are objects, many named after the nouns in the domain space, and these objects are connected with the rich relationships and structure that true domain models have. The catch comes when you look at the behavior, and you realize that there is hardly any behavior on these objects, making them little more than bags of getters and setters. Indeed often these models come with design rules that say that you are not to put any domain logic in the the domain objects. Instead there are a set of service objects which capture all the domain logic. These services live on top of the domain model and use the domain model for data.

For CRUD applications, these "domain services" should number very few.  But as the number of domain services begins to grow, it should be a signal to us that we need richer behavior, in the form of Domain-Driven Design.  Building an application with DDD in mind is quite different than [Model-Driven Architecture](http://en.wikipedia.org/wiki/Model-driven_architecture). In MDA, we start with database table diagrams or ERDs, and build objects to match.  In DDD, we start with interactions and behaviors, and build models to match.  But one of the first issues we run into is, how do we create entities in the first place?  Our first unit test needs to create an entity, so where should it come from?

### Creating Valid Aggregates

Validation can be a tricky beast in applications, as we often see validation has less to do with _data_ than it does with _commands_.  For example, a Person might have a required "BirthDate" field on a screen.  But we then have the requirement that legacy, imported Persons might not have a BirthDate.  So it then becomes clear that the requirement of a BirthDate depends on who is doing the creation.

But beyond validation are the invariants of an entity. **Invariants are the essence of what it means for an entity to be an entity**. We may ask our customers, can a Person be a Person (in our system) without a BirthDate? Yes, sometimes. How about without a Name? No, a Person in our system must have some identifying features, that together define this "Person".  An Order needs an OrderNumber and a Customer. If the business got a paper order form without customer information, they'd throw it out! Notice this is not _validation_, but something else entirely. We're asking now, what does it mean for an Order to be an Order? Those are its invariants.

Suppose then we have a rather simple set of logic.  We indicate our Orders as "local" if the billing province is equal to the customer's province. Rather easy method:

```cs
public class Order
{
    public bool IsLocal()
    {
        return Customer.Province == BillingProvince;
    }
```

I simply interrogate the Customer's province against the Order's BillingProvince. But now I can get myself into rather odd situations:

```cs
[Test]
public void Should_be_a_local_customer_when_provinces_are_equal()
{
    var order = new Order
    {
       BillingProvince = "Ontario"
    };
    var customer = new Customer
    {
        Province = "Ontario"
    };

    var isLocal = order.IsLocal();

    isLocal.ShouldBeTrue();
}
```

Instead of a normal assertion pass/fail, I get a NullReferenceException! I forgot to set the Customer on the Order object.

But wait – how was I able to create an Order without a Customer?  An Order isn't an Order without a Customer, as our domain experts explained to us. _We could go the slightly ridiculous route, and put in null checks_.

But wait – this will _never_ happen in production. We should just fix our test code and move on, right?  Yes, I'd agree if you were building a transaction-script based CRUD system (the 90% case).  However, if we're doing DDD, we want to satisfy that requirement about aggregate roots, that its invariants must be satisfied with all operation.  _Creating an aggregate root is an operation_, and therefore in our code "new" is an operation.  Right now, invariants are decidedly _not_ satisfied.

Let's modify our Order class slightly:

```cs
public class Order
{
    public Order(Customer customer)
    {
        Customer = customer;
    }
```

We added a constructor to our Order class, so that when an Order is created, all invariants are satisfied.  Our test now needs to be modified with our new invariant in place:

```cs
[TestFixture]
public class Invariants
{
    [Test]
    public void Should_be_a_local_customer_when_provinces_are_equal()
    {
        var customer = new Customer
        {
            Province = "Ontario"
        };
        var order = new Order(customer)
        {
            BillingProvince = "Ontario"
        };

        var isLocal = order.IsLocal();

        isLocal.ShouldBeTrue();
    }
}
```

And now our test passes!

### Summary and alternatives

Going from a data-driven approach, this will cause pain. If we write our persistence tests first, we run into "why do I need a Customer just to test Order persistence?" Or, why do we need a `Customer` to test order totalling logic? The problem occurs further down the line when you start writing code against a domain model that doesn't enforce its own invariants. _If invariants are only satisfied through domain services, it becomes quite tricky to understand_ what a true `Order` is at any time. Should we always code assuming the Customer is there? Should we code it only when we "need" it?

If our entity always satisfies its invariants because its design doesn't allow invariants to be violated, the violated invariants can never occur.  We no longer need to even _think_ about the possibility of a missing Customer, and can build our software under that enforced rule going forward. In practice, I've found this approach actually requires _less_ code, as we don't allow ourselves to get into ridiculous scenarios that we now have to think about going forward.

But building entities through a constructor isn't the only way to go. We also have:

* [Builder pattern](http://martinfowler.com/bliki/ExpressionBuilder.html)
* [Creation method](http://www.industriallogic.com/xp/refactoring/constructorCreation.html)
* [Through existing aggregate roots](http://www.udidahan.com/2009/06/29/dont-create-aggregate-roots/)

The bottom line is – if our entity needs certain information for it to be considered an entity in its essence, then don't let it be created without its invariants satisfied!

***

## Encapsulated collections

One of the common themes throughout the [DDD book](http://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215) is that much of the nuts and bolts of structural domain-driven design is just plain good use of object-oriented programming.  This is certainly true, but DDD adds some direction to OOP, along with roles, stereotypes and patterns. _Much of the direction for building entities at the class level can, and should, come from test-driven development_. TDD is a great tool for building OO systems, as we incrementally build our design with only the behavior that is needed to pass the test. Our big challenge then is to write good tests.

To fully harness TDD, we need to be highly attuned to the design that comes out of our tests. For example, suppose we have our traditional Customer and Order objects. In our world, an `Order` has a `Customer`, and a `Customer` can have many `Orders`.  We have this directionality because we can navigate this relationship from both directions in our application. In the last post, we worked to satisfy invariants to prevent an unsupported and nonsensical state for our objects.

We can start with a fairly simple test:

```cs
[Test]
public void Should_add_the_order_to_the_customers_order_lists_when_an_order_is_created()
{
    var customer = new Customer();
    var order = new Order(customer);

    customer.Orders.ShouldContain(order);
}
```

At first, this test does not compile, as Customer does not yet contain an Orders member.
To make this test compile (and subsequently fail), we add an Orders list to Customer:

```cs
public class Customer
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Province { get; set; }
    public List<Order> Orders { get; set; }

    public string GetFullName()
    {
        return LastName + ", " + FirstName;
    }
}
```

With the Orders now exposed on Customer, we can make our test pass from the Order constructor:

```cs
public class Order
{
    public Order(Customer customer)
    {
        Customer = customer;
        customer.Orders.Add(this);
    }
```

And all is well in our development world, right? Not quite. This design exposes quite a bit of functionality that I don't think our domain experts need, or want. The design above allows some very interesting and very wrong scenarios:

```cs
[Test]
public void Not_supported_situations()
{
    // Removing orders?
    var customer1 = new Customer();
    var order1 = new Order(customer1);

    customer1.Orders.Remove(order1);

    // Clearing orders?
    var customer2 = new Customer();
    var order2 = new Order(customer1);

    customer2.Orders.Clear();

    // Duplicate orders?
    var customer3 = new Customer();
    var customer4 = new Customer();
    var order3 = new Order(customer3);

    customer4.Orders.Add(order3);
}
```

With the API I just created, I allow a number of rather bizarre scenarios, most of which make absolutely no sense to the domain experts:

* Clearing orders
* Removing orders
* Adding an order from one customer to another
* Inserting orders
* Re-arranging orders
* Adding an order without the Order's Customer property being correct

This is where we have to be a little more judicious in the API we expose for our system. All of these scenarios are _possible_ in the API we created, but now we have some confusion on whether we should support these scenarios or not. If I'm working in a similar area of the system, and I see that I can do a `Customer.Orders.Remove` operation, it's not immediately clear that this is a scenario not actually coded for.  Worse, I don't have the ability to correctly handle these situations if the collection is exposed directly.

Suppose I want to clear a Customer's Orders. It logically follows that each Order's Customer property would be null at that point. But I can't hook in easily to the `List`

### Moving towards intention-revealing interfaces

Let's fix the Customer object first. It exposes a List

```cs
public class Customer
{
    private readonly IList<Order> _orders = new List<Order>();

    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Province { get; set; }
    public IEnumerable<Order> Orders { get { return _orders; } }

    public string GetFullName()
    {
        return LastName + ", " + FirstName;
    }
}
```

This interface explicitly tells users of Customer two things:

* Orders are **readonly**, and cannot be modified through this aggregate
* Adding orders are done somewhere else

I now have the issue of the Order constructor needing to add itself to the Customer's Order collection. I want to do this:

```cs
public class Order
{
    public Order(Customer customer)
    {
        Customer = customer;
        customer.AddOrder(this);
    }
```

Instead of exposing the Orders collection directly, I work through a specific method to add an order. But, I don't want that AddOrder available everywhere, I want to only support the enforcement of the Order-Customer relationship through this explicitly defined interface. I'll do this by exposing an AddOrder method, but exposing it as internal:

```cs
public class Customer
{
    private readonly IList<Order> _orders = new List<Order>();

    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Province { get; set; }
    public IEnumerable<Order> Orders { get { return _orders; } }

    internal void AddOrder(Order order)
    {
        _orders.Add(order);
    } 
}
```

There are many different ways I could enforce this relationship, from exposing an AddOrder method publicly on Customer or through the approach above. But either way, I'm moving towards an **intention-revealing interface**, and only exposing the operations I intend to support through my application.  Additionally, I'm ensuring that all invariants of my aggregates are satisfied at the completion of the Create Order operation. _When I create an Order, the domain model takes care of the relationship between Customer and Order without any additional manipulation_.

If I publicly expose a collection class, I'm opening the doors for confusion and future bugs as I've now allowed my system to tinker with the implementation details of the relationship. It's my belief that the API of my domain model should explicitly support the operations needed to fulfill the needs of the application and interaction of the UI, **but nothing more**.
