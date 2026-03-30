---
title: MongoRecipes
layout: default
nav_order: 11
parent: NoSQL
grand_parent: Data
last_modified_date: 2026-03-30 00:00:00 +00:00
---

# MongoRecipes

## JS

+ info

```js
    db.version(); 
    db.stats();
 db.collection.stats();
 db.collection.storageSize()
```

+ Select where field type is string  

```js
 db.collection.find({field:{$type:2}})
```

+ Update ALL records with field  

```js
 db.collection.update(  
  { field: "old value" },  
  { $set: { field: "new value" } },  
  {upsert: 0, multi: 1} ) 
```

+ update schema rename column

```js
 db.fs.files.update({}, {$rename: {'metadata.Height': 'metadata.height'}}, {multi:true});     
 db.fs.files.update({}, {$rename: {'metadata.Width': 'metadata.width'}}, {multi:true});  
```

+ Check field exists  

```js
 db.fs.files.find ({ "metadata": {$exists: true} }) 
 db.fs.files.count({ "metadata.creationTimeUtc": {$exists: false}}) 
 db.fs.files.count({ "metadata.Width": {$exists: true}, "metadata.Height": {$exists: true}}) 
```

+ capped collection [1] with a tailable cursor [2]

```js
    db.createCollection("log", {capped:true, size:100000, max:5000}) /* { "ok" : 1 } */
    db.log.isCapped() /* true */
```

MongoDb C# driver `CursorType` enumeration [3].
MongoDb C# driver wire protocol `QueryMessage.TailableCursor` [4].
`QueryMessage.AwaitData` Gets a value indicating whether the server should await data (used with tailable cursors).

+ bulk insert  

```js
 var bulk = db.items.initializeUnorderedBulkOp(); 
 bulk.insert( { item: "abc123", defaultQty: 100, status: "A", points: 100 } ); 
 bulk.insert( { item: "ijk123", defaultQty: 200, status: "A", points: 200 } ); 
 bulk.insert( { item: "mop123", defaultQty: 0, status: "P", points: 0 } ); 
 bulk.execute();
```

+ rename database OldDb to DbNew

```js
 db.copyDatabase("OldDb","DbNew","localhost") 
 use OldDb 
 db.dropDatabase();
```  

+ db.collection.insertMany() [5] new in 3.2

## GridFS [6]

+ removal

```js
    db.fs.files.remove(); 
    db.getCollection('fs.chunks').remove();
```

+ Most recently updated / modified

```js
    db.fs.files.find({filename :/.*.PNG.*/ }).sort({uploadDate:-1});
 db.fs.files.find({filename :/.*.JPG.*/ }).sort({"metadata.lastWriteTimeUtc":-1})
```

+ and caused me pain

```js
    db.fs.files.count(); 
    db.fs.files.find({length :{"$gt": 0} }).sort({length:-1}); 
 db.fs.files.find({ uploadDate :{"$lt": ISODate("2015-12-15T00:00:00.000Z")} },{"_id":0,"filename":1, uploadDate:1}).sort({uploadDate:-1}).pretty()
 db.fs.files.distinct( "filename")
```

+ group by h x w, push filenames, count filenames in each group  

```js
 db.fs.files.aggregate([ 
  { $group: { 
   _id: { "w":"$metadata.width", "h":"$metadata.height" }, 
   files: { $push: "$filename" }, 
   no: { $sum: 1 } 
  } } 
 ])    ``````````
```

+ old c# api v1 [7]
+ **upload files** 2.2 [8], 2.4 [9]
+ Download files [10]
+ Find files [11]
+ Delete and rename [12]

## CLI

mongoexport docs [13], in pairs, export-import, dump-restore
connect to powershell ps d:\mongodb\server\3.0\bin>  
.\mongoexport -d imagesDB -c fs.files -o 10.11.11.45.fs.files.json
.\mongoexport -d imagesDB -c fs.chunks -o 10.11.11.45.fs.chunks.json

Message: connected to: localhost; exported 115 records  
mongoimport.exe --db ImageCache10111145 --collection fs.files --file 10.11.11.45.fs.files.json
mongoimport.exe --db ImageCache10111145 --collection fs.chunks --file 10.11.11.45.fs.chunks.json

## C# Driver

+ driver releases [14]
+ update [15]
+ old driver cheat sheet [16]
+ Query by a Field in an Embedded Document [17]
+ distinct array subdocuments SO [18],
api [19]
+ Using a Tailable Cursor [20]
+ Configure GridFS Chunksize in MongoDB [21], todo update
+ Mongo DB support for Hangfire [22] sources
+ Building MongoDB Applications with Binary Files Using GridFS 1 [23] and 2 [24]
+ Driver v1.11 [25] install tutorial
+ Getting started with GridFS driver v2 [26]
+ cursor with filter

```cs
 using (var cursor = await FsFiles.FindAsync(filter)) { 
             while (cursor.MoveNext()) { 
                 foreach (var bsonDoc in cursor.Current) {
     // bsonDoc.DoSomething(); 
 } } }
```


[1]: https://docs.mongodb.com/manual/core/capped-collections
[2]: https://docs.mongodb.com/manual/tutorial/create-tailable-cursor/
[3]: http://api.mongodb.com/csharp/current/html/T_MongoDB_Driver_CursorType.htm
[4]: http://api.mongodb.com/csharp/current/html/P_MongoDB_Driver_Core_WireProtocol_Messages_QueryMessage_TailableCursor.htm
[5]: https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/
[6]: https://stackoverflow.com/tags/gridfs/info
[7]: http://api.mongodb.com/csharp/1.2/html/0e461cba-c217-b8a4-b03f-cf05cf59ba97.htm
[8]: http://mongodb.github.io/mongo-csharp-driver/2.2/reference/gridfs/uploadingfiles/
[9]: http://mongodb.github.io/mongo-csharp-driver/2.4/reference/gridfs/
[10]: http://mongodb.github.io/mongo-csharp-driver/2.2/reference/gridfs/downloadingfiles/
[11]: http://mongodb.github.io/mongo-csharp-driver/2.2/reference/gridfs/findingfiles/
[12]: http://mongodb.github.io/mongo-csharp-driver/2.2/reference/gridfs/deletingandrenamingfiles/
[13]: https://docs.mongodb.com/manual/reference/program/mongoexport/
[14]: https://github.com/mongodb/mongo-csharp-driver/releases
[15]: https://docs.mongodb.com/getting-started/csharp/update/
[16]: http://www.layerworks.com/blog/2014/11/11/mongodb-shell-csharp-driver-comparison-cheat-cheet
[17]: https://docs.mongodb.com/getting-started/csharp/query/#query-by-a-field-in-an-embedded-document
[18]: https://stackoverflow.com/questions/29906247/distinctasync-against-array-sub-documents-with-mongodb-c-sharp-2-0-driver
[19]: http://api.mongodb.com/csharp/2.0/html/M_MongoDB_Driver_IMongoCollection_1_DistinctAsync__1.htm
[20]: http://mongodb.github.io/mongo-csharp-driver/2.0/examples/tailable_cursor/
[21]: https://stackoverflow.com/questions/10384307/configure-gridfs-chunksize-in-mongodb
[22]: https://github.com/sergeyzwezdin/Hangfire.Mongo
[23]: https://www.mongodb.com/blog/post/building-mongodb-applications-binary-files-using-gridfs-part-1?jmp=docs
[24]: https://www.mongodb.com/blog/post/building-mongodb-applications-binary-files-using-gridfs-part-2
[25]: http://mongodb.github.io/mongo-csharp-driver/1.11/driver/
[26]: http://mongodb.github.io/mongo-csharp-driver/2.2/reference/gridfs/gettingstarted/


[<](./index.md) | [<<](/index.md)
