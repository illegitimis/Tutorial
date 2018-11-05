# UML

## Class diagrams

**relationships** | **between components**
------------ | -------------
![uml symbols](https://www.smartdraw.com/uml-diagram/img/uml-symbols.png?bn=1510011096) | ![uml notation](https://i.stack.imgur.com/smuC7.jpg)
![association / aggregation / composition](https://i.stack.imgur.com/jNyV5.jpg) | **association / aggregation / composition**. Aggregation and Composition are subsets of association meaning they are _specific cases of association_. Association is a relationship where all objects have their **own lifecycle** and there is **no owner**.
![Differences between Association, Aggregation and Composition](https://i.stack.imgur.com/bfBSY.png) | **Aggregation** is a specialised form of Association where all objects have their own lifecycle_, *but there is ownership* and child objects **can not belong** to another parent object. _Composition_ is again specialised form of Aggregation and we can call this as a “death” relationship. It is a strong type of Aggregation. Child object does not have its lifecycle and if parent object is deleted, all child objects will also be deleted.

[<<](../design.md) | [home](../../README.md)