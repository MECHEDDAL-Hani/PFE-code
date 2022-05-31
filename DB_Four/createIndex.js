// switch to myDB Database

use("myDB");

sh.enableSharding("myDB");

// cities

db.cities.createIndex(
    { "coordinate": "hashed" }
);

db.cities.createIndex(
    { "coordinate": "2dsphere" }
);

sh.shardCollection("myDB.cities", { "coordinate": 1 });

// lands

db.lands.createIndex(
    { "coordinate": "hashed" }
);

db.lands.createIndex(
    { "coordinate": "2dsphere" }
);

sh.shardCollection("myDB.lands", { "coordinate": 1 });

// roads

db.roads.createIndex(
    { "coordinate": "hashed" }
);

db.roads.createIndex(
    { "coordinate": "2dsphere" }
);

sh.shardCollection("myDB.roads", { "coordinate": 1 });

exit();