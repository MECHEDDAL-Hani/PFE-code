# Mongodb

## DB ONE

```shell
mongod -f "/home/hani/dev/DB_One/DB_One.conf"
```

```js
"mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin"
```

## DB Two

```shell
mongod -f "/home/hani/dev/DB_Two/DB_Two.conf"
```

```js
"mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin"
```

## DB Three

```shell
mongod -f "/home/hani/dev/DB_Three/primary/DB_Three.conf"
mongod -f "/home/hani/dev/DB_Three/replication_1/DB_Three_replication_1.conf"
mongod -f "/home/hani/dev/DB_Three/replication_2/DB_Three_replication_2.conf"
mongod -f "/home/hani/dev/DB_Three/replication_3/DB_Three_replication_3.conf"
```

```shell
"mongodb://root:root@127.0.0.1:27020,127.0.0.1:27021,127.0.0.1:27022,127.0.0.1:27023/?replicaSet=my_replication&authSource=admin"
"mongodb://root:root@127.0.0.1:27020/?replicaSet=my_replication&authSource=admin"
```

## DB foure

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

```js
"mongodb://root:root@127.0.0.1:27070/?authSource=admin" 
```
