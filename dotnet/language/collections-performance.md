# .NET collections performance

| Collection | Ordering | Contiguous Storage? | Direct Access? | Lookup Efficiency  | Manipulate Efficiency | Based On |
|------------------|------------------------------------------------|---------------------|----------------|-------------------------|-----------------------|-------------|
| Dictionary | Unordered | Yes | Via Key | Key: O(1) | O(1) | hash table |
| SortedDictionary | Sorted | No | Via Key | Key: O(log n) | O(log n) | binary search tree |
| SortedList | Sorted | Yes | Via Key | Key: O(log n) | O(n) | array |
| List | User has precise control over element ordering | Yes | Via Index | Index: O(1) Value: O(n) | O(n) | dynamic array |
| LinkedList | User has precise control over element ordering | No | No | Value: O(n) | O(1) | doubly-linked circular list |
| HashSet | Unordered | Yes | Via Key | Key: O(1) | O(1) | Hash table? |
| SortedSet | Sorted | No | Via Key | Key: O(log n) | O(log n) | BT |
| Stack | LIFO | Yes | Only Top | Top: O(1) | O(1)* | array |
| Queue | FIFO | Yes | Only Front | Front: O(1) | O(1) | Array? |

> From <http://geekswithblogs.net/BlackRabbitCoder/archive/2011/06/16/c.net-fundamentals-choosing-the-right-collection-class.aspx>

## `Dictionary<TKey, TValue>`
* Best for **high performance lookups**.
* **Fastest** class for _associative lookups/inserts/deletes_ because it uses a hash table under the covers
* Because the keys are hashed, the key type _should correctly implement_ `GetHashCode()` and `Equals()` appropriately or you should provide an external `IEqualityComparer` to the dictionary on construction
* The insert/delete/lookup time of items in the dictionary is **amortized constant time** - O(1) - which means no matter how big the dictionary gets, the time it takes to find something remains relatively constant. 
* The _only downside_ is that the dictionary, by nature of using a hash table, is **unordered**, so you cannot easily traverse the items in a Dictionary in order.

## `SortedDictionary<TKey,TValue>`
* **keeps items in order by the key**,  `TKey` _must implement_ `IComparable<TKey>`
* trades lookup time for order
* insert, delete, lookup is _logarithmic_
* use it when perf is not main issue, and must maintain key ordering
* Compromise of Dictionary speed and ordering, uses BST, **binary search tree**.
* `TreeSet` <http://referencesource.microsoft.com/#System/compmod/system/collections/generic/sorteddictionary.cs,1a01ea5555bded49>. `TreeSet` extends a `SortedSet`. Reference to parent node. `SortedSet.Node` is red black.

## `SortedList<TKey,TValue>`
* Very _similar_ to `SortedDictionary`, except tree is implemented in an **array**, so has _faster lookup on preloaded_ data, but _slower loads_.
* **insertions and deletions are linear** - O(n) - because deleting or adding an item may involve shifting all items up or down in the list.
* _use_ when **insertions and deletions are rare**

## `List<T>`
* Vector, **dynamic array**
* Essentially it is an contiguous array of items that grow once its current capacity is exceeded
* Best for smaller lists where direct access required and no sorting.
* inserting and removing in the beginning or middle of the List<T> are very costly because you must shift all the items up or down as you delete or insert respectively
* adding and removing at the end of a List<T> is an amortized constant operation - O(1)
* prefer array only when you know size fixed

## `LinkedList<T>`
* Best for lists where inserting/deleting in middle is common and **no direct access required**.
* basic implementation of a doubly-linked circular list.
* use when **a lot of adding and removing** (over list), _no indexer_ 
* <http://referencesource.microsoft.com/#System/compmod/system/collections/generic/linkedlist.cs,df5a6c7b6b60da4f>
* is a general-purpose linked list. It supports enumerators and implements the ICollection interface, consistent with other collection classes in the .NET Framework. 
* `LinkedList<T>` provides separate nodes of type `LinkedListNode<T>`, so insertion and removal are O(1) operations. You can remove nodes and reinsert them, either in the same list or in another list, which results in no additional objects allocated on the heap. Because the list also maintains an internal count, getting the `Count` property is an O(1) operation. 
* Because the `LinkedList<T>` is doubly linked, each node points forward to the `Next` node and backward to the `Previous` node. 
* Lists that contain reference types perform better when a node and its value are created at the same time. LinkedList<T> accepts null as a valid `Value` property for reference types and allows duplicate values. 
* If the LinkedList<T> is empty, the `First` and `Last` properties contain null. 
* The LinkedList<T> class does not support chaining, splitting, cycles, or other features that can leave the list in an inconsistent state. 
* The list remains consistent on a single thread. The only multithreaded scenario supported by LinkedList<T> is multithreaded read operations. 

## `HashSet<T>`
* **unordered** collection of **unique** items, no duplicates
* useful for super-quick lookups where order is not important
* Unique unordered collection, like a Dictionary except key and value are same object.
* the type T _should have a valid implementation_ of `GetHashCode()` and `Equals()`, _or_ you should provide an appropriate `IEqualityComparer<T>` to the HashSet<T> on construction.
* has `int[] m_buckets` and `Slot[] m_slots`, an array-based implementation similar to `Dictionary<T>`, using a buckets array to map hash values to the Slots array. Items in the Slots array that hash to the same value are chained together through the "next" indices.
> From <http://referencesource.microsoft.com/#System.Core/System/Collections/Generic/HashSet.cs,d0822f25708256c5>

## `SortedSet<T>`
* is to HashSet<T> what the SortedDictionary<TKey,TValue> is to Dictionary<TKey,TValue>.
* Unique sorted collection, like SortedDictionary except key and value are same object.
* type T must implement IComparable<T> or you need to supply an external IComparer<T>.

## `Stack<T>`
* Essentially same as List<T> except only process as LIFO

## `Queue<T>`
* Essentially same as List<T> except only process as FIFO
* <http://referencesource.microsoft.com/#System/compmod/system/collections/generic/stack.cs,c5371bef044c6ab6>

[<<](../csdotnet.md) | [home](../../README.md) | [wiki](https://github.com/illegitimis/Tutorial/wiki)
