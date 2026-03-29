# DocumentDB SQL Query Cheat Sheet

Quick reference for writing Azure DocumentDB (Cosmos DB) queries. All examples use two sample `Families` documents — `AndersenFamily` (WA) and `WakefieldFamily` (NY).

## Example JSON Documents

```json
{
  "id": "AndersenFamily",
  "lastName": "Andersen",
  "parents": [ { "firstName": "Thomas" }, { "firstName": "Mary Kay" } ],
  "children": [
    {
      "firstName": "Henriette Thaulow",
      "gender": "female",
      "grade": 5,
      "pets": [ { "givenName": "Fluffy" } ]
    }
  ],
  "address": { "state": "WA", "county": "King", "city": "seattle" },
  "creationDate": "2015-01-03T12:00Z",
  "isRegistered": true,
  "location": { "type": "Point", "coordinates": [31.9, -4.8] }
}
```

```json
{
  "id": "WakefieldFamily",
  "parents": [
    { "familyName": "Wakefield", "givenName": "Robin" },
    { "familyName": "Miller",    "givenName": "Ben"   }
  ],
  "children": [
    {
      "familyName": "Merriam", "givenName": "Jesse",
      "gender": "female", "grade": 1,
      "pets": [ { "givenName": "Goofy" }, { "givenName": "Shadow" } ]
    },
    { "familyName": "Miller", "givenName": "Lisa", "gender": "female", "grade": 8 }
  ],
  "address": { "state": "NY", "county": "Manhattan", "city": "NY" },
  "creationDate": "2015-07-20T12:00Z",
  "isRegistered": false
}
```

## SELECT

```sql
-- All fields
SELECT * FROM Families f WHERE f.id = "AndersenFamily"

-- Specific fields
SELECT f.id, f.address.city FROM Families f ORDER BY f.address.city

-- Projected object
SELECT {"Name": f.id, "City": f.address.city} AS Family
FROM Families f
WHERE f.address.city = f.address.state

-- TOP N rows
SELECT TOP 100 * FROM Families f

-- VALUE keyword (unwrap scalar)
SELECT VALUE "Hello World"
```

## FROM and Array Indexing

```sql
-- Root collection
SELECT * FROM Families f WHERE f.lastName = "Andersen"

-- Array element by index
SELECT * FROM Families.children[0] c WHERE c.grade >= 5
```

## WHERE

```sql
-- Equality
SELECT * FROM Families f WHERE f.id = "AndersenFamily"

-- Compound condition
SELECT * FROM Families.children[0] c
WHERE c.grade >= 5 AND c.isRegistered = true

-- IN keyword
SELECT * FROM Families
WHERE Families.address.state IN ("NY", "WA", "CA", "PA", "OH", "OR", "MI", "WI")

-- BETWEEN keyword
SELECT * FROM Families.children[0] c WHERE c.grade BETWEEN 1 AND 5
```

## ORDER BY

```sql
SELECT f.id, f.address.city
FROM Families f
ORDER BY f.address.city ASC
```

## JOIN (Intra-Document)

DocumentDB JOIN is an intra-document self-join — it does not join across documents.

```sql
-- Flatten children array
SELECT c.givenName
FROM Families f
JOIN c IN f.children
WHERE f.id = 'WakefieldFamily'
ORDER BY f.address.city ASC

-- Multi-level join (children → pets)
SELECT
    f.id         AS familyName,
    c.givenName  AS childGivenName,
    c.firstName  AS childFirstName,
    p.givenName  AS petName
FROM Families f
JOIN c IN f.children
JOIN p IN c.pets
```

## Parameterized SQL

```sql
SELECT *
FROM Families f
WHERE f.lastName       = @lastName
  AND f.address.state  = @addressState
```

## Object and Array Creation

```sql
-- Array literal
SELECT [f.address.city, f.address.state] AS CityState FROM Families f

-- Object literal
SELECT {"Name": f.id, "City": f.address.city} AS Family FROM Families f
```

## Escape / Quoted Accessor

```sql
SELECT f["lastName"] FROM Families f WHERE f["id"] = "AndersenFamily"
```

## Operators

### Arithmetic

```sql
SELECT VALUE (2 + 3 * 4)   -- +, -, *, /, %
```

### Comparison

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `!=` / `<>` | Not equal |
| `>`, `>=` | Greater than / or equal |
| `<`, `<=` | Less than / or equal |
| `??` | Coalesce |

### Logical

```sql
-- AND, OR, NOT
SELECT * FROM Families.children[0] c
WHERE c.grade >= 5 AND c.isRegistered = true
```

### Bitwise

`|`, `&`, `^`, `<<`, `>>`, `>>>` (zero-fill right shift)

### String Concatenation

```sql
SELECT VALUE ("Hello" || " " || "World")
```

### Ternary `?` and Coalesce `??`

```sql
SELECT (c.grade < 5) ? "elementary" : ((c.grade < 9) ? "junior" : "high") AS gradeLevel
FROM Families.children[0] c
```

## JavaScript UDF

```sql
-- Register UDF (JavaScript)
-- function REGEX_MATCH(input, pattern) { return input.match(pattern) !== null; }

-- Use in query
SELECT udf.REGEX_MATCH(Families.address.city, ".*eattle")
```

## Built-in Functions

### Mathematical

```sql
SELECT VALUE ABS(-4)
-- ABS, CEILING, EXP, FLOOR, LOG, LOG10, POWER, ROUND, SIGN, SQRT, SQUARE, TRUNC
-- ACOS, ASIN, ATAN, ATN2, COS, COT, DEGREES, PI, RADIANS, SIN, TAN
```

### Type Checking

```sql
SELECT IS_DEFINED(f.lastName), IS_NUMBER(4) FROM Families f
-- IS_ARRAY, IS_BOOL, IS_NULL, IS_NUMBER, IS_OBJECT, IS_STRING, IS_DEFINED, IS_PRIMITIVE
```

### String

```sql
SELECT Families.id, Families.address.city
FROM Families
WHERE STARTSWITH(Families.id, "Wakefield")
-- CONCAT, CONTAINS, ENDSWITH, INDEX_OF, LEFT, LENGTH, LOWER, LTRIM,
-- REPLACE, REPLICATE, REVERSE, RIGHT, RTRIM, STARTSWITH, SUBSTRING, UPPER
```

### Array

```sql
SELECT Families.id
FROM Families
WHERE ARRAY_CONTAINS(Families.parents, { givenName: "Robin", familyName: "Wakefield" })
-- ARRAY_CONCAT, ARRAY_CONTAINS, ARRAY_LENGTH, ARRAY_SLICE
```

### Geospatial

```sql
SELECT * FROM Families f
WHERE ST_Distance(f.location, {"type": "Point", "coordinates": [31.9, -4.8]}) < 30000
-- ST_WITHIN, ST_DISTANCE, ST_INTERSECTS, ST_ISVALID, ST_ISVALIDDETAILED
```

## Query Interfaces

| Interface | Details |
|---|---|
| Server-side | SQL, JavaScript integrated query |
| Client-side | .NET (LINQ), Java, JavaScript, Node.js, Python |
| Online playground | <https://www.documentdb.com/sql/demo> |

---

[1]: https://docs.microsoft.com/en-us/azure/cosmos-db/sql-query-getting-started

[<<](./index.md) | [home](../../README.md)
