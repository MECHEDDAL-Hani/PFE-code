# All Step i made for create Project and run it

## 1 Secend DataBase (with indexing)

### 1.1 Create necessaries folder

```shell
mkdir -p /home/hani/dev/DB_Two /home/hani/dev/ssl
```

### 1.2 Create ssl certificate

<!-- * https://www.openssl.org/docs/man1.1.1/man1/openssl-rand.html -->
```shell
openssl rand -base64 741 > /home/hani/dev/ssl/server.pem
chmod 600 /home/hani/dev/ssl/server.pem
```

### 1.3 lunch first mongod service

Start mongod process

```shell
mongod -f "/home/hani/dev/DB_Two/DB_Two.conf"
```

run this command

```shell
mongo --port 27010
```

Stop mongod process

```shell
killall mongod
```

and i create root user

```js
use("admin");

db.createUser({
  user: "root",
  pwd: "root",
  roles : [ "root" ]
});

exit();
```

and now connect with this commend

```shell
mongo --port 27010 --username root --password root
```

and the svr is

```js
"mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin"
```

### 1.4 Creat index

and now we create different  index for all collection

```shell
mongosh "mongodb://root:root@127.0.0.1:27010/" --file "/home/hani/dev/DB_Two/queries/createIndex.js"
```

### 1.5 Generated dataset

```shell
python -u "/home/hani/dev/Code/progress_insert_data.py"
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --file "/home/hani/dev/insert.js"
```

```shell
mongoimport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --collection="cities" --file "/home/hani/dev/Dataset/db2/cities.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --collection "cities" --file "/home/hani/dev/Dataset/db2/cities_2.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --collection="lands" --file "/home/hani/dev/Dataset/db2/dza.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --collection="lands" --file "/home/hani/dev/Dataset/db2/all-willayas.json"

mongosh "mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --file "/home/hani/dev/insert.js"

```

### 1.6 Export DataSet

```shell
mongoexport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin"  --collection="cities"  --out="/home/hani/dev/Dataset/db2/cities.json"

mongoexport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin"  --collection="lands"  --out="/home/hani/dev/Dataset/db2/lands.json"

mongoexport --uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin"  --collection="roads"  --out="/home/hani/dev/Dataset/db2/roads.json"

```

and now we test different queries, just for sure its correct

- first with command line

```shell
mongosh "mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin" --file "/home/hani/dev/request.js"
```

- Secend without command line using Python

```shell
python -u "/home/hani/dev/DB_Two/queries/request.py"
```

## 2 First DataBase (without indexing)

### 2.1 Create necessaries folder

```shell
mkdir -p /home/hani/dev/DB_One
```

### 2.2 ssl certificate

We used last certificate

```shell
/home/hani/dev/ssl/server.pem
```

### 2.3 lunch first mongod service

Start mongod process

```shell
mongod -f "/home/hani/dev/DB_One/DB_One.conf"
```

run this command

```shell
mongo --port 27001
```

Stop mongod process

```shell
killall mongod
```

and i create root user

```js
use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles : [ "root" ]
});

exit();
```

and now connect with this commend

```shell
mongo --port 27001 --username root --password root
```

and the svr is

```js
"mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin"
```

### 2.4 import dataset

```shell
mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection "cities" --drop --file "/home/hani/dev/Dataset/db2/cities.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection "lands" --drop --file "/home/hani/dev/Dataset/db2/lands.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection "roads" --drop --file "/home/hani/dev/Dataset/db2/roads.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection "cities" --file "/home/hani/dev/Dataset/db2/cities_2.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection="lands" --file "/home/hani/dev/Dataset/db2/dza.json"

mongoimport --uri="mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --collection="lands" --file "/home/hani/dev/Dataset/db2/all-willayas.json"

mongosh "mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --file "/home/hani/dev/insert2.js"

```

```shell
mongosh "mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --file "/home/hani/dev/insert.js"
```

and now we test different queries, just for sure its correct

first with command line

```shell
mongosh "mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin" --file "/home/hani/dev/DB_One/queries/request.js"
```

first without command line using Python

```shell
python -u "/home/hani/dev/DB_One/queries/request.py"
```

## Replication database

### 3.1 Create necessaries folder

```shell
mkdir -p /home/hani/dev/DB_Three/primary \
/home/hani/dev/DB_Three/replication_1 \
/home/hani/dev/DB_Three/replication_2 \
/home/hani/dev/DB_Three/replication_3
```

### 3.2 ssl certificate

We used last certificate

```shell
/home/hani/dev/ssl/server.pem
```

### 3.3 lunch first mongod service

Start mongod process

```shell
mongod -f "/home/hani/dev/DB_Three/primary/DB_Three.conf"
mongod -f "/home/hani/dev/DB_Three/replication_1/DB_Three_replication_1.conf"
mongod -f "/home/hani/dev/DB_Three/replication_2/DB_Three_replication_2.conf"
mongod -f "/home/hani/dev/DB_Three/replication_3/DB_Three_replication_3.conf"
```

run this command

```shell
mongosh --port 27020
```

initiate replication and create root user

```js
rs.initiate();

use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles: [
    {role: "root", db: "admin"}
  ]
});

exit();
```

reconnect with this commadn

```shell
mongo "mongodb://root:root@127.0.0.1:27020/?authSource=admin"
```

```js
rs.add("localhost:27021");
rs.add("localhost:27022");
rs.add("localhost:27023");

// rs.status();

// rs.stepDown();

// rs.isMaster();

exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27021/?authSource=admin"
```

```js
db.getMongo().setReadPref('secondary')
exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27022/?authSource=admin"
```

```js
db.getMongo().setReadPref('secondary')
exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27023/?authSource=admin"
```

```js
db.getMongo().setReadPref('secondary')
exit();
```

```shell
mongosh "mongodb://root:root@2127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/?replicaSet=my_replication&authSource=admin" \
 --file "/home/hani/dev/DB_Three/createIndex.js"
```

Stop mongod process

```shell
killall mongod
```

### 3.4 import dataset

```shell
URI="mongodb://root:root@127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/myDB?replicaSet=my_replication&authSource=admin"

mongoimport --uri=$URI --collection "cities" --file "/home/hani/dev/Dataset/db2/cities.json"

mongoimport --uri=$URI --collection "lands" --file "/home/hani/dev/Dataset/db2/lands.json"

mongoimport --uri=$URI --collection "roads" --file "/home/hani/dev/Dataset/db2/roads.json"

mongoimport --uri=$URI --collection "cities" --file "/home/hani/dev/Dataset/db2/cities_2.json"

mongoimport --uri=$URI --collection="lands" --file "/home/hani/dev/Dataset/db2/dza.json"

mongoimport --uri=$URI --collection="lands" --file "/home/hani/dev/Dataset/db2/all-willayas.json"

mongosh $URI --file "/home/hani/dev/insert2.js"

```

```shell
mongosh "mongodb://root:root@127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/?replicaSet=my_replication&authSource=admin" \
 --file "/home/hani/dev/insert.js"
```

and now we test different queries, just for sure its correct

first with command line

```shell
mongosh "mongodb://root:root@127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/?replicaSet=my_replication&authSource=admin" \
 --file "/home/hani/dev/request.js"
```

first without command line using Python

```shell
python -u "/home/hani/dev/DB_One/queries/request.py"
```

## Sharding database

### 4.1 Create necessaries folder

```shell
# mkdir -p /home/hani/dev/DB_Four
mkdir -p \
/home/hani/dev/DB_Four/Mongos/DB \
/home/hani/dev/DB_Four/CSRS/replication_1/DB \
/home/hani/dev/DB_Four/CSRS/replication_1/DB \
/home/hani/dev/DB_Four/CSRS/replication_2/DB \
/home/hani/dev/DB_Four/CSRS/replication_3/DB \
/home/hani/dev/DB_Four/CSRS/replication_4/DB \
/home/hani/dev/DB_Four/shared_1/replication_1/DB \
/home/hani/dev/DB_Four/shared_1/replication_2/DB \
/home/hani/dev/DB_Four/shared_1/replication_3/DB \
/home/hani/dev/DB_Four/shared_1/replication_4/DB \
/home/hani/dev/DB_Four/shared_2/replication_1/DB \
/home/hani/dev/DB_Four/shared_2/replication_2/DB \
/home/hani/dev/DB_Four/shared_2/replication_3/DB \
/home/hani/dev/DB_Four/shared_2/replication_4/DB \
/home/hani/dev/DB_Four/shared_3/replication_1/DB \
/home/hani/dev/DB_Four/shared_3/replication_2/DB \
/home/hani/dev/DB_Four/shared_3/replication_3/DB \
/home/hani/dev/DB_Four/shared_3/replication_4/DB


DB_Four_Mongos.conf
DB_Four_CSRS_replication_1.conf
DB_Four_CSRS_replication_1.conf
DB_Four_CSRS_replication_2.conf
DB_Four_CSRS_replication_3.conf
DB_Four_CSRS_replication_4.conf
DB_Four_shared_1_replication_1.conf
DB_Four_shared_1_replication_2.conf
DB_Four_shared_1_replication_3.conf
DB_Four_shared_1_replication_4.conf
DB_Four_shared_2_replication_1.conf
DB_Four_shared_2_replication_2.conf
DB_Four_shared_2_replication_3.conf
DB_Four_shared_2_replication_4.conf
DB_Four_shared_3_replication_1.conf
DB_Four_shared_3_replication_2.conf
DB_Four_shared_3_replication_3.conf
DB_Four_shared_3_replication_4.conf
```

### 4.2 ssl certificate

We used last certificate

```shell
/home/hani/dev/ssl/server.pem
```

### 4.3 lunch first mongod service

Start mongod process

```shell
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_1/DB_Four_CSRS_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_2/DB_Four_CSRS_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_3/DB_Four_CSRS_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_4/DB_Four_CSRS_replication_4.conf"
```

run this command

```shell
mongosh --port 27031
```

initiate replication and create root user

```js
rs.initiate();

use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles: [
    {role: "root", db: "admin"}
  ]
});

db.auth("root", "root");

rs.add("localhost:27032");
rs.add("localhost:27033");
rs.add("localhost:27034");

exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27031,127.0.0.1:27032,127.0.0.1:27033,127.0.0.1:27034/?replicaSet=sharding_csrs&authSource=admin"
```

```shell
mongos -f "/home/hani/dev/DB_Four/Mongos/DB_Four_Mongos.conf"
```

connect with this commadn

```shell
mongosh "mongodb://root:root@127.0.0.1:27070/?authSource=admin"
```

```shell
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_1/DB_Four_shared_1_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_2/DB_Four_shared_1_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_3/DB_Four_shared_1_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_4/DB_Four_shared_1_replication_4.conf"
```

```shell
mongosh --port 27040
```

initiate replication and create root user

```js
rs.initiate();

use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles: [
    {role: "root", db: "admin"}
  ]
});

db.auth("root", "root");

rs.add("localhost:27041");
rs.add("localhost:27042");
rs.add("localhost:27043");

exit();
```

```shell
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_1/DB_Four_shared_2_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_2/DB_Four_shared_2_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_3/DB_Four_shared_2_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_4/DB_Four_shared_2_replication_4.conf"
```

```shell
mongosh --port 27050
```

initiate replication and create root user

```js
rs.initiate();

use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles: [
    {role: "root", db: "admin"}
  ]
});

db.auth("root", "root");

rs.add("localhost:27051");
rs.add("localhost:27052");
rs.add("localhost:27053");

exit();
```

```shell
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_1/DB_Four_shared_3_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_2/DB_Four_shared_3_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_3/DB_Four_shared_3_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_4/DB_Four_shared_3_replication_4.conf"
```

```shell
mongosh --port 27060
```

initiate replication and create root user

```js
rs.initiate();

use("admin");
db.createUser({
  user: "root",
  pwd: "root",
  roles: [
    {role: "root", db: "admin"}
  ]
});

db.auth("root", "root");

rs.add("localhost:27061");
rs.add("localhost:27062");
rs.add("localhost:27063");

exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27070/?authSource=admin"
```

```shell
sh.addShard("sharding_one_replication/127.0.0.1:27040");
sh.addShard("sharding_two_replication/127.0.0.1:27050");
sh.addShard("sharding_three_replication/127.0.0.1:27060");

exit();
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27070/?authSource=admin" \
 --file "/home/hani/dev/DB_Four/createIndex.js"
```

Stop mongod process

```shell
killall mongod && killall mongos
```

### 4.4 import dataset

```shell
mongosh "mongodb://root:root@127.0.0.1:27070/?authSource=admin" \
 --file "/home/hani/dev/insert.js"
```

```shell
URI="mongodb://root:root@127.0.0.1:27070/myDB?authSource=admin"

mongoimport --uri=$URI --collection "cities" --file "/home/hani/dev/Dataset/db2/cities.json"

mongoimport --uri=$URI --collection "lands" --file "/home/hani/dev/Dataset/db2/lands.json"

mongoimport --uri=$URI --collection "roads" --file "/home/hani/dev/Dataset/db2/roads.json"

mongoimport --uri=$URI --collection "cities" --file "/home/hani/dev/Dataset/db2/cities_2.json"

mongoimport --uri=$URI --collection="lands" --file "/home/hani/dev/Dataset/db2/dza.json"

mongoimport --uri=$URI --collection="lands" --file "/home/hani/dev/Dataset/db2/all-willayas.json"

mongosh $URI --file "/home/hani/dev/insert2.js"

```

```shell
mongosh "mongodb://root:root@2127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/?replicaSet=my_replication&authSource=admin" \
 --file "/home/hani/dev/insert.js"
```

```shell
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_1/DB_Four_CSRS_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_2/DB_Four_CSRS_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_3/DB_Four_CSRS_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/CSRS/replication_4/DB_Four_CSRS_replication_4.conf"

mongod -f "/home/hani/dev/DB_Four/shared_1/replication_1/DB_Four_shared_1_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_2/DB_Four_shared_1_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_3/DB_Four_shared_1_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_1/replication_4/DB_Four_shared_1_replication_4.conf"

mongod -f "/home/hani/dev/DB_Four/shared_2/replication_1/DB_Four_shared_2_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_2/DB_Four_shared_2_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_3/DB_Four_shared_2_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_2/replication_4/DB_Four_shared_2_replication_4.conf"

mongod -f "/home/hani/dev/DB_Four/shared_3/replication_1/DB_Four_shared_3_replication_1.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_2/DB_Four_shared_3_replication_2.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_3/DB_Four_shared_3_replication_3.conf"
mongod -f "/home/hani/dev/DB_Four/shared_3/replication_4/DB_Four_shared_3_replication_4.conf"

mongos -f "/home/hani/dev/DB_Four/Mongos/DB_Four_Mongos.conf"
```

and now we test different queries, just for sure its correct

first with command line

```shell
mongosh "mongodb://root:root@127.0.0.1:27070/myDB?authSource=admin" \
 --file "/home/hani/dev/request.js"
```

first without command line using Python

```shell
python -u "/home/hani/dev/DB_Four/queries/request.py"
```

```js
// switch to myDB Database
use('myDB');

//  cities
db.cities.deleteMany({});

// lands
db.lands.deleteMany({});

// roads
db.roads.deleteMany({});

exit();
```
