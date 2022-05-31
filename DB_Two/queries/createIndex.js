// switch to myDB Database
use('myDB');

// cities
db.cities.createIndex(
    { "coordinate": "2dsphere" }
);

// lands
db.lands.createIndex(
    { "coordinate": "2dsphere" }
);

// roads
db.roads.createIndex(
    { "coordinate": "2dsphere" }
);

exit();