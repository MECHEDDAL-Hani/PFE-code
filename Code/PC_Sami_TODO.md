# PC Sami TODO

```shell
mkdir -p /home/hani/dev/DB_One /home/hani/dev/ssl
```

```shell
openssl rand -base64 741 > /home/hani/dev/ssl/server.pem
```

```shell
mongod -f "/home/hani/dev/DB_One/DB_One.conf"
```

```shell
mongo --port 27001
```

```js
use admin
db.createUser({
  user: "root",
  pwd: "root",
  roles : [ "root" ]
})

exit
```

```shell
mongo --port 27001 --username root --password root
```

```js
"mongodb://root:root@127.0.0.1:27001/myDB?authSource=admin"
```

```shell
mongosh "mongodb://root:root@127.0.0.1:27001/?authSource=admin"
```

```js
use("mydb");


// cities
db.createCollection("cities");

// lands
db.createCollection("lands");

// roads
db.createCollection("roads");

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

// cities
db.cities.insert({
  "name": "Port James",
  "coordinate": {
    "type": "Point",
    "coordinates": [
      -13.463013,
      -35.078071
    ]
  },
  "description": "Non neque velit modi sit voluptatem est sed. Dolor non quisquam sed neque dolor."
});

// lands
db.lands.insert({
  ""name": "Lake Jose",
  "coordinate": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          20,
          -32
        ],
        [
          11,
          26
        ],
        [
          -17,
          -2
        ],
        [
          20,
          -32
        ]
      ]
    ]
  },
  "description": "Sit dolore ipsum tempora ipsum."
});

// roads
db.roads.insert({
    "name": "Williamsville",
    "coordinate": {
        "type": "LineString",
        "coordinates": [
        [
            41.004369,
            -53.362109
        ],
        [
            58.903211,
            -89.203984
        ],
        [
            -72.671844,
            -14.299842
        ]
        ]
    },
  "description": "Quaerat velit dolorem adipisci sed labore etincidunt."
});

```

## $geoIntersects

### 1.cities

- 1
<!-- Polygon -->
```js
    db.cities.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.cities.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.cities.find(
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.cities.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.cities.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.cities.find({
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

### 1.lands

- 1
<!-- Polygon -->
```js
    db.lands.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.lands.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.lands.find(
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.lands.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.lands.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.lands.find({
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

### 1.roads

- 1
<!-- Polygon -->
```js
    db.roads.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.roads.find(
        {
     "coordinate": {
       "$geoIntersects": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.roads.find(
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.roads.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.roads.find({
        {
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.roads.find({
        "coordinate": {
        "$geoIntersects": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

## $geoWithin

### 2.cities

- 1
<!-- Polygon -->
```js
    db.cities.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.cities.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.cities.find(
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.cities.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.cities.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.cities.find({
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

### 2.lands

- 1
<!-- Polygon -->
```js
    db.lands.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.lands.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.lands.find(
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.lands.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.lands.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.lands.find({
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

### 2.roads

- 1
<!-- Polygon -->
```js
    db.roads.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.roads.find(
        {
     "coordinate": {
       "$geoWithin": {
          "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          }
       }
     }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.roads.find(
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    )
```

- 22
<!-- LineString -->
```js
    print(db.roads.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        }
                }
            }
        }
    }).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.roads.find({
        {
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }
        }
    })
```

- 33
<!-- Point -->
```js
    print(db.roads.find({
        "coordinate": {
        "$geoWithin": {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] } }
            }}
        ).explain("executionStats").executionStats.executionTimeMillis);
```

## $near

### 3.cities

- 1
<!-- Polygon -->
```js
    db.cities.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.cities.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.cities.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

### 3.lands

- 1
<!-- Polygon -->
```js
    db.lands.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.lands.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.lands.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

### 3.roads

- 1
<!-- Polygon -->
```js
    db.roads.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.roads.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.roads.find({
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$near" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

## $nearSphere

### 4.cities

- 1
<!-- Polygon -->
```js
    db.cities.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.cities.find({
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.cities.find({
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.cities.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

### 4.lands

- 1
<!-- Polygon -->
```js
    db.lands.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.lands.find({
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.lands.find({
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.lands.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

### 4.roads

- 1
<!-- Polygon -->
```js
    db.roads.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    )
```

- 11
<!-- Polygon -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": {
             "type": "Polygon" ,
             "coordinates": [
               [[ 0, 0 ],
                [ 3, 6 ],
                [ 6, 1 ],
                [ 0, 0 ] ]
             ]
          },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 2
<!-- LineString -->
```js
    db.roads.find({
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 22
<!-- LineString -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "LineString",
             "coordinates": [ [ 40, 5 ],
                            [ 41, 6 ] ]
                        },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```

- 3
<!-- Point -->
```js
    db.roads.find({"$near"

     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   })
```

- 33
<!-- Point -->
```js
    print(db.roads.find(
        {
     "coordinate": { "$nearSphere" :
          {
            "$geometry": { "type": "Point", "coordinates": [ 40, 5 ] },
            "$minDistance": 1000,
            "$maxDistance": 5000
          }
       }
   }
    ).explain("executionStats").executionStats.executionTimeMillis);
```
