# Indices 

[GetIndices.sql](https://gist.github.com/illegitimis/0dbc3373a8386c12bfc72ae26102cc2f) gist.

## Unique

-   Creates a unique index on a table or view.  
-   A unique index is one in which no two rows are permitted to have the same index key value.  
-   A clustered index on a view must be unique. 
-   The Database Engine does not allow creating a unique index on columns that already include duplicate values, whether or not IGNORE_DUP_KEY is set to ON. If this is tried, the Database Engine displays an error message. Duplicate values must be removed before a unique index can be created on the column or columns.  
-   Columns that are used in a unique index should be set to NOT NULL, because multiple null values are considered duplicates when a unique index is created.

## Clustered

-   Creates an index in which the logical order of the key values determines the physical order of the corresponding rows in a table. The bottom, or leaf, level of the clustered index contains the actual data rows of the table.  
-   A table or view is allowed one clustered index at a time. A view with a unique clustered index is called an indexed view. Creating a unique clustered index on a view physically materializes the view. A unique clustered index must be created on a view before any other indexes can be defined on the same view. For more information, see Create Indexed Views. 
-   Create the clustered index before creating any nonclustered indexes. Existing nonclustered indexes on tables are rebuilt when a clustered index is created. 
-   If CLUSTERED is not specified, a nonclustered index is created. Because the leaf level of a clustered index and the data pages are the same by definition, creating a clustered index and using the ON partition_scheme_name or ON filegroup_name clause effectively moves a table from the filegroup on which the table was created to the new partition scheme or filegroup. Before creating tables or indexes on specific filegroups, verify which filegroups are available and that they have enough empty space for the index. 
-   In some cases creating a clustered index can enable previously disabled indexes. For more information, see [Enable Indexes and Constraints](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/enable-indexes-and-constraints) and [Disable Indexes and Constraints](https://docs.microsoft.com/en-us/sql/relational-databases/indexes/disable-indexes-and-constraints). 
-   In SQL Server, [indexes are organized as B-trees](https://technet.microsoft.com/en-us/library/ms177443(v=sql.105).aspx). Each page in an _index B-tree_ is called an **index node**. The top node of the B-tree is called the root node. The bottom level of nodes in the index is called the leaf nodes. Any index levels between the root and the leaf nodes are collectively known as intermediate levels. In a clustered index, the leaf nodes contain the data pages of the underlying table. The root and intermediate level nodes contain index pages holding index rows. Each index row contains a key value and a pointer to either an intermediate level page in the B-tree, or a data row in the leaf level of the index. The pages in each level of the index are linked in a doubly-linked list.  
-   The pages in the data chain and the rows in them are ordered on the value of the clustered index key. All inserts are made at the point where the key value in the inserted row fits in the ordering sequence among existing rows. The page collections for the B-tree are anchored by page pointers in the sys.system_internals_allocation_units system view. The sys.system_internals_allocation_units system view is reserved for Microsoft SQL Server internal use only. For a clustered index, the root_page column in sys.system_internals_allocation_units points to the top of the clustered index for a specific partition. SQL Server moves down the index to find the row corresponding to a clustered index key. To find a range of keys, SQL Server moves through the index to find the starting key value in the range and then scans through the data pages using the previous or next pointers. To find the first page in the chain of data pages, SQL Server follows the leftmost pointers from the root node of the index. 

![structure of a clustered index in a single partition.](https://i-technet.sec.s-msft.com/dynimg/IC157372.gif "structure of a clustered index in a single partition")

## NONCLUSTERED 

-   [Creates an index that specifies the logical ordering of a table](https://technet.microsoft.com/en-us/library/ms177484(v=sql.105).aspx). With a nonclustered index, the physical order of the data rows is independent of their indexed order. 
-   Each table can have up to 999 nonclustered indexes, regardless of how the indexes are created: either implicitly with PRIMARY KEY and UNIQUE constraints, or explicitly with CREATE INDEX. 
-   For indexed views, nonclustered indexes can be created only on a view that has a unique clustered index already defined. The default is NONCLUSTERED. 
-   Nonclustered indexes have the same B-tree structure as clustered indexes 
-   The data rows of the underlying table are not sorted and stored in order based on their nonclustered keys 
-   The leaf layer of a nonclustered index is made up of index pages instead of data pages. 
-   Nonclustered indexes can be defined on a table or view with a clustered index or a heap. Each index row in the nonclustered index contains the nonclustered key value and a row locator. This locator points to the data row in the clustered index or heap having the key value. The row locators in nonclustered index rows are either a pointer to a row or are a clustered index key for a row 

![nonclustered index in a single partition](https://i-technet.sec.s-msft.com/dynimg/IC88960.gif "nonclustered index in a single partition")

## Heaps

-   [A heap is a table without a clustered index](https://technet.microsoft.com/en-us/library/ms188270(v=sql.105).aspx). Heaps have one row in [sys.partitions](https://technet.microsoft.com/en-us/library/ms175012%28v=sql.105%29.aspx), with index_id = 0 for each partition used by the heap.  
-   The column first_iam_page in the sys.system_internals_allocation_units system view points to the first IAM page in the chain of IAM pages that manage the space allocated to the heap 
-   SQL Server uses the IAM pages to move through the heap. The data pages and the rows within them are not in any specific order and are not linked. The only logical connection between data pages is the information recorded in the IAM pages. 
-   Table scans or serial reads of a heap can be performed by scanning the IAM pages to find the extents that are holding pages for the heap. Using the IAM pages to set the scan sequence also means that rows from the heap are not typically returned in the order in which they were inserted.

![heap structures](https://i-technet.sec.s-msft.com/dynimg/IC22444.gif "heap structures")




[<<](../SQL.md) 
| 
[home](../README.md) 
| 
[wiki](https://github.com/illegitimis/Tutorial/wiki) 

