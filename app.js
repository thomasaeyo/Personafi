var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');

// Connection URL
var url = 'mongodb://localhost:27017/test';
// Use connect method to connect to the Server
MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  console.log("Connected correctly to server");

  insertDocuments(db, function() {
    db.close();
  });
});

var insertDocuments = function(db, callback) {
  // Get the documents collection
  var collection = db.collection('people');
  // Insert some documents
  collection.update([
    {bob : "cs"}, {peter : "cs"}, {sarah : "cs"}], function(err, records){   //change the document here!!!!!
    console.log("Record added as "+records[0]._id);
  });
}