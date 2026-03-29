# DocumentDB

- [Online Query Playground](www.documentdb.com/sql/demo)
- [RU Estimator](www.documentdb.com/capacityplanner) capacity planner
- StackOverflow [1] tagged questions

## BW-Tree

- The BW-Tree: A Latch-Free B-Tree for Log-Structured Flash Storage [2] pdf [2]
- The Bw-Tree: A B-tree for New Hardware Platforms [3] pdf [3]
- **Schema-Agnostic Indexing with Azure DocumentDB** [4] pdf [4]
- The Bw-Tree: A B-Tree On Steroids [5] pdf [5]

## SQL Queries

- Query Using DocumentDB SQL [6]
- SQL queries for Azure Cosmos DB DocumentDB API [7] msdn
- Azure Cosmos DB DocumentDB API: SQL syntax reference [8] msdn

## Cheat Sheet

 Built-in | functions
--- | ---
Mathematical | ABS, CEILING, EXP, FLOOR, LOG, LOG10, POWER, ROUND, SIGN, SQRT, SQUARE, TRUNC, ACOS, ASIN, ATAN, ATN2, COS, COT, DEGREES, PI, RADIANS, SIN, TAN 
Type checking | IS_ARRAY, IS_BOOL, IS_NULL, IS_NUMBER, IS_OBJECT, IS_STRING, IS_DEFINED, IS_PRIMITIVE
String | CONCAT, CONTAINS, ENDSWITH, INDEX_OF, LEFT, LENGTH, LOWER, LTRIM, REPLACE, REPLICATE, REVERSE, RIGHT, RTRIM, STARTSWITH, SUBSTRING, UPPER
Array | ARRAY_CONCAT, ARRAY_CONTAINS, ARRAY_LENGTH,  ARRAY_SLICE
Geospatial | ST_WITHIN, ST_DISTANCE, ST_INTERSECTS, ST_ISVALID, ST_ISVALIDDETAILED

Operators | _
--- | ---
arithmetic | +, -, *, /, %
bitwise | `|`, &, ^, <,>>, >>> (zero-fill right shift)
logical | AND, OR, NOT
comparison | =, !=, >, >=, <, <=, <>, ??
string | || (concatenate)
ternary | ?

Sample | queries
--- | ---
Comparison (range) operators | `SELECT * FROM Families.children[0] c WHERE c.grade >= 5`
Logical operators | `SELECT * FROM Families.children[0] c WHERE c.grade >= 5 AND c.isRegistered = true`
Array Built-in functions | `SELECT Families.id FROM Families WHERE ARRAY_CONTAINS(Families.parents, {givenName: "Robin", familyName: "Wakefield" })`
String Built-in functions | `SELECT Families.id, Families.address.city FROM Families WHERE STARTSWITH(Families.id, "Wakefield")`
Parameterized SQL | `SELECT * FROM Families f WHERE f.lastName = @lastName AND f.address.state = @addressState`
Intradocument JOINS | `SELECT f.id AS familyName, c.givenName AS childGivenName, c.firstName AS childFirstName, p.givenName AS petName FROM Families f JOIN c IN f.children JOIN p IN c.pets`
Value keyword | `SELECT VALUE "Hello World"`, `SELECT VALUE ABS(-4)`
Object/Array Creation | `SELECT [f.address.city, f.address.state] AS CityState FROM Families f`
Escape/quoted accessor | `SELECT f["lastName"] FROM Families f WHERE f["id"] = "AndersenFamily"`
Ternary (?) and Coalesce (??) operators | `SELECT (c.grade < 5)? "elementary": ((c.grade < 9)? "junior": "high") AS gradeLevel FROM Families.children[0] c`
IN keyword | `SELECT * FROM Families WHERE Families.address.state IN ("NY", "WA", "CA", "PA", "OH", "OR", "MI", "WI")`
ORDER BY keyword | `SELECT f.id, f.address.city FROM Families f ORDER BY f.address.city`
Geospatial functions | `SELECT * FROM Families f WHERE ST_Distance(f.location, {"type":"Point", "coordinates":[31.9, -4.8]}) < 30000`
Type Built-in functions | `SELECT IS_DEFINED(f.lastName), IS_NUMBER(4) FROM Families f`
BETWEEN keyword | `SELECT * FROM Families.children[0] c WHERE c.grade BETWEEN 1 AND 5`
_SQL - JavaScript UDF_, define | `function (input, pattern) { return input.match(pattern) !== null; }`
_SQL - JavaScript UDF_, use | `SELECT udf.REGEX_MATCH(Families.address.city, ".*eattle")`

## Execute Stored Procedure

- error Message

    ```txt
    {"Errors":["Encountered exception while compiling Javascript. Exception = SyntaxError: Expected ';'\r\nSource information: line: 1, column: 50, source line:
    (function __docDbMain() { var fn = SELECT * FROM c where c.type=\"FeatureConfiguration\" and c.feature=@featureName;"]}
    ActivityId: 404ab020-0e53-4939-a66e-95e1ce40d8a7, 
    Request URI: /apps/DocDbApp/services/DocDbServer7/partitions/a4cb4953-38c8-11e6-8106-8cdcd42c33be/replicas/1p/
    ```

- server side scripts [9]
- DocumentClientHelper [10]
- [DocDBClientBulk](DocDBClientBulk)
- Calling DocumentDb stored procedures from .net [11]
- Call DocumentDb stored procedure from .Net with parameters. [12]

[<<](../nosql.md) | [home](../../README.md)

[1]: https://stackoverflow.com/questions/tagged/azure-cosmosdb
[2]: http://sites.computer.org/debull/A13june/bwtree1.pdf
[3]: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bw-tree-icde2013-final.pdf
[4]: http://www.vldb.org/pvldb/vol8/p1668-shukla.pdf
[5]: http://www.hpts.ws/papers/2013/bw-tree-hpts2013.pdf
[6]: https://www.documentdb.com/sql/tutorial
[7]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-sql-query
[8]: https://docs.microsoft.com/en-us/azure/cosmos-db/documentdb-sql-query-reference
[9]: https://github.com/Azure/azure-documentdb-dotnet/blob/1ff7e836f73b8622f82dee688d4d0541cf54112d/samples/code-samples/ServerSideScripts/Program.cs
[10]: https://github.com/Azure/azure-documentdb-dotnet/blob/ebb807493ecec06964e1e049b963045fd347a45d/samples/code-samples/Shared/Util/DocumentClientHelper.cs
[11]: https://stackoverflow.com/questions/36655455/calling-documentdb-stored-procedures-from-net
[12]: https://stackoverflow.com/questions/36626257/call-documentdb-stored-procedure-from-net-with-parameters/36668664#36668664
