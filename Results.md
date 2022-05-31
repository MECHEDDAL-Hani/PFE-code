# Results

## DB_One

<!-- markdownlint-disable no-inline-html -->
| Storage size |           Collections            | Indexes |
| :----------: | :------------------------------: | :-----: |
|   1.06 GB    | cities <br /> lands <br /> roads |    3    |

### DB_One Collection

![DB One Collection cities](Image/db1.png)

#### DB_One Collection cities

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       1300010       |   266.6 MB   |         450 B          |    1    |      24.4 MB       |

Example of one document:

```JSON
{
    "_id": {
        "$oid": "62813a243b20e67505403c7d"
    },
    "name": "Lake Marissamouth",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            -40.300215,
            -65.60481
        ]
    },
    "description": "Velit voluptatem tempora dolorem modi dolorem tempora sit. Quaerat sit consectetur dolorem ipsum velit dolore. Sed quiquia porro quaerat quaerat non. Est magnam magnam dolore. Quaerat eius sit labore adipisci quaerat non. Est dolorem labore eius magnam. Etincidunt porro porro quaerat porro quiquia consectetur. Sed quiquia est quaerat."
}
```

#### DB_One Collection lands

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200064        |   73.3 MB    |         884 B          |    1    |       3.6 MB       |

Example of one document:

```JSON
{
    "_id": {
        "$oid": "62813a243b20e67505403cb7"
    },
    "name": "Port Michelle",
    "coordinate": {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    -24,
                    -63
                ],
                [
                    20,
                    -5
                ],
                [
                    15,
                    72
                ],
                [
                    -44,
                    15
                ],
                [
                    -24,
                    -63
                ]
            ]
        ]
    },
    "description": "Consectetur sit labore dolore. Tempora eius dolore dolore neque est est. Velit sit velit dolore. Quiquia eius adipisci velit numquam porro. Neque magnam sit dolorem quiquia non dolore dolorem. Amet dolorem ipsum sit. Dolore neque quisquam dolore. Quaerat eius sit adipisci. Velit voluptatem quiquia magnam sed sit."
}
```

#### DB_One Collection roads

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200005        |   757.2 MB   |        5.18 KB         |    1    |       3.7 MB       |

Example of one Document:

```JSON
{
    "_id": {
        "$oid": "62813a243b20e67505403ba1"
    },
    "name": "Lake Mary",
    "coordinate": {
        "type": "LineString",
        "coordinates": [
            [
                -96.789448,
                -4.674807
            ],
            [
                -29.014001,
                -81.689868
            ],
            [
                92.267362,
                17.601576
            ],
            [
                91.571754,
                -71.332535
            ],
            [
                47.310937,
                68.557508
            ],
            [
                22.860059,
                -78.548149
            ],
            [
                20.732049,
                -67.359155
            ],
            [
                -123.083722,
                53.848689
            ],
            [
                148.470179,
                78.977981
            ],
            [
                26.73466,
                31.164212
            ],
            [
                146.235312,
                4.799648
            ],
            [
                25.921109,
                31.790678
            ],
            [
                -7.073893,
                -68.449167
            ],
            [
                -1.565896,
                -71.650494
            ],
            [
                -112.926271,
                38.493319
            ],
            [
                -116.223814,
                -56.694859
            ],
            [
                140.827814,
                20.79376
            ],
            [
                102.739557,
                73.926858
            ],
            [
                104.938331,
                55.960699
            ],
            [
                -44.892899,
                -75.786625
            ]
        ]
    },
    "description": "Sit consectetur quiquia est. Dolore quaerat tempora dolorem. Quiquia porro velit dolorem non consectetur. Sed adipisci quiquia quisquam neque. Porro sit voluptatem magnam. Labore eius aliquam non quiquia etincidunt. Aliquam sit sed voluptatem consectetur velit ut. Eius numquam dolor etincidunt est sit labore est."
}
```

## DB_Two

| Storage size |           Collections            | Indexes |
| :----------: | :------------------------------: | :-----: |
|   1.07 GB    | cities <br /> lands <br /> roads |    6    |

### DB_Two Collection

![DB Two Collection](Image/db2.png)

#### DB_Two Collection cities

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       1300010       |   266.6 MB   |         450 B          |    2    |      72.63 MB      |

#### DB_Two Collection lands

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200064        |   80.79 MB   |         884 B          |    2    |      65.86MB       |

#### DB_Two Collection roads

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200005        |  755.13 MB   |        5.18 KB         |    2    |      134.5 MB      |

## DB_Three

| Storage size |           Collections            | Indexes |
| :----------: | :------------------------------: | :-----: |
|   1.09 GB    | cities <br /> lands <br /> roads |    6    |

### DB_Three Collection

![DB Three Collection](Image/db3.png)

#### DB_Three Collection cities

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       1300010       |  229.28 MB   |         450 B          |    2    |     132.24 MB      |

#### DB_Three Collection lands

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200064        |   69.77 MB   |         884 B          |    2    |      57.65 MB      |

#### DB_Three Collection roads

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200005        |  789.55 MB   |        5.18 KB         |    2    |     132.68 MB      |

## DB_Foure

| Storage size |           Collections            | Indexes |
| :----------: | :------------------------------: | :-----: |
|   1.56 GB    | cities <br /> lands <br /> roads |   36    |

### DB_Foure Collection

![DB Four Collection](Image/db4.png)

#### DB_Foure Collection cities

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       1300010       |  433.23 MB   |        450.27 B        |    4    |     389.69 MB      |

#### DB_Foure Collection lands

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200064        |   69.85 MB   |        884.58 B        |    4    |     297.64 MB      |

#### DB_Foure Collection roads

| Number Of Doucuemnt | Storage Size | AVG Size One Doucuemnt | Indexes | Indexes Total Size |
| :-----------------: | :----------: | :--------------------: | :-----: | :----------------: |
|       200005        |   1.06 GB    |        5.18 KB         |    4    |      1.88 GB       |

## Query

### Query 1

- Description
<!-- TODO ADD Description -->

- Code Of Query

```js
db.cities.find(
    {
        "coordinate": {
            "$geoIntersects": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -2.1752929687499996,
                                35.22767235493586
                            ],
                            [
                                -1.6809082031249998,
                                33.165145408240285
                            ],
                            [
                                -0.8679199218749999,
                                32.41706632846282
                            ],
                            [
                                7.767333984374999,
                                33.00866349457558
                            ],
                            [
                                7.22900390625,
                                33.96158628979907
                            ],
                            [
                                8.096923828125,
                                34.687427949314845
                            ],
                            [
                                8.63525390625,
                                37.16031654673677
                            ],
                            [
                                2.61474609375,
                                37.17782559332976
                            ],
                            [
                                -2.1752929687499996,
                                35.22767235493586
                            ]
                        ]
                    ]
                }
            }
        }
    }
)
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |          0          |      1300010       |               2300               |        no        |  No Index  |

**COLLSCAN**
nRetuned: 826
Execution Time: 348 ms
Documents Examined: 1300010

![DB one Query 1](Image/Query1-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1249         |        1225        |                30                |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1225
Execution Time: 0 ms

**FETCH**
nRetuned: 826
Execution Time: 30 ms

![DB Two Query 1](Image/Query1-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1249         |        1225        |                29                |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1225
Execution Time: 0 ms

**FETCH**
nRetuned: 826
Execution Time: 20 ms

![DB Three Query 1](Image/Query1-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1249         |        1225        |                12                |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 826
Execution Time: 11 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 1225
Execution Time: 0 ms

**IXSAN**
nRetuned: 1225
Execution Time: 1 ms

**FETCH**
nRetuned: 826
Execution Time: 0 ms

**SHARDING_TWO_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

![DB Foure Query 1](Image/Query1-4.png)

### Query 2

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.cities.find(
    {
        "coordinate": {
            "$geoIntersects": {
                "$geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [
                            -1.307373046875,
                            34.88593094075317
                        ],
                        [
                            -0.626220703125,
                            35.16482750605027
                        ],
                        [
                            0.06591796875,
                            35.9157474194997
                        ],
                        [
                            1.329345703125,
                            36.155617833818525
                        ],
                        [
                            3.8891601562499996,
                            36.34167804918315
                        ],
                        [
                            5.359053611755371,
                            36.195352001083535
                        ],
                        [
                            5.410080253975188,
                            36.191711170919284
                        ],
                        [
                            7.750854492187499,
                            36.910372213522535
                        ],
                        [
                            8.3001708984375,
                            36.760891249565624
                        ]
                    ]
                }
            }
        }
    }
)
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |          0          |      1300010       |               2816               |        no        |  No Index  |

COLLSCAN
nRetuned: 1
Execution Time: 477 ms
Documents Examined: 1300010

![DB one Query 2](Image/Query2-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |         175         |        124         |                4                 |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1
Execution Time: 0 ms

**FETCH**
nRetuned: 142
Execution Time: 0 ms

![DB Two Query 2](Image/Query2-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |         175         |        124         |                3                 |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1
Execution Time: 0 ms

**FETCH**
nRetuned: 142
Execution Time: 0 ms

![DB Three Query 2](Image/Query2-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |         178         |        142         |                3                 |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 1
Execution Time: 3 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 1
Execution Time: 0 ms

**IXSAN**
nRetuned: 142
Execution Time: 0 ms

**FETCH**
nRetuned: 1
Execution Time: 0 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

![DB Foure Query 2](Image/Query2-4.png)

### Query 3

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.lands.find(
    {
        "coordinate": {
            "$geoIntersects": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                4.88616943359375,
                                36.357163062654365
                            ],
                            [
                                5.0042724609375,
                                35.72421761691415
                            ],
                            [
                                5.92987060546875,
                                35.766572101173516
                            ],
                            [
                                5.943603515625,
                                36.45000844447082
                            ],
                            [
                                4.88616943359375,
                                36.357163062654365
                            ]
                        ]
                    ]
                }
            }
        }
    }
)
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       153422       |          0          |       200064       |               5447               |        no        |  No Index  |

COLLSCAN
nRetuned: 153422
Execution Time: 5364 ms
Documents Examined: 200064

![DB one Query 3](Image/Query3-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       153422       |       189440        |       189357       |               2720               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 189357
Execution Time: 140 ms

**FETCH**
nRetuned: 153422
Execution Time: 1807 ms

![DB Two Query 3](Image/Query3-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       153422       |       189440        |       189357       |               2707               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 189357
Execution Time: 185 ms

**FETCH**
nRetuned: 153422
Execution Time: 1778 ms

![DB Three Query 3](Image/Query3-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       153422       |       189431        |       189356       |               2769               |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 153422
Execution Time: 739 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 2
Execution Time: 0 ms

**IXSAN**
nRetuned: 2
Execution Time: 0 ms

**FETCH**
nRetuned: 2
Execution Time: 0 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 1
Execution Time: 0 ms

**IXSAN**
nRetuned: 1
Execution Time: 0 ms

**FETCH**
nRetuned: 1
Execution Time: 0 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 153419
Execution Time: 464 ms

**IXSAN**
nRetuned: 153453
Execution Time: 75 ms

**FETCH**
nRetuned: 153419
Execution Time: 1419 ms

![DB Foure Query 3](Image/Query3-4.png)

### Query 4

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.roads.find(
    {
        "coordinate": {
            "$geoIntersects": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                5.358881950378418,
                                36.19462470395782
                            ],
                            [
                                5.369052886962891,
                                36.192581309214255
                            ],
                            [
                                5.3694820404052725,
                                36.1939666674039
                            ],
                            [
                                5.371112823486328,
                                36.195248101907744
                            ],
                            [
                                5.370726585388184,
                                36.196668045376434
                            ],
                            [
                                5.372915267944336,
                                36.20193200133552
                            ],
                            [
                                5.372185707092285,
                                36.20404441045111
                            ],
                            [
                                5.35858154296875,
                                36.200200475940555
                            ],
                            [
                                5.358881950378418,
                                36.19462470395782
                            ]
                        ]
                    ]
                }
            }
        }
    }
)
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        722         |          0          |       200005       |              16676               |        no        |  No Index  |

COLLSCAN
nRetuned: 722
Execution Time: 16650 ms
Documents Examined: 200005

![DB one Query 4](Image/Query4-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        722         |       183649        |       183638       |              18613               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183638
Execution Time: 188 ms

**FETCH**
nRetuned: 722
Execution Time: 18414 ms

![DB Two Query 4](Image/Query4-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        722         |       183649        |       183638       |              16475               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183638
Execution Time: 254 ms

**FETCH**
nRetuned: 722
Execution Time: 16144 ms

![DB Three Query 4](Image/Query4-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        722         |       183650        |       183637       |               4472               |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 722
Execution Time: 9 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 254
Execution Time: 4 ms

**IXSAN**
nRetuned: 60383
Execution Time: 55 ms

**FETCH**
nRetuned: 254
Execution Time: 3994 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 208
Execution Time: 10 ms

**IXSAN**
nRetuned: 58753
Execution Time: 86 ms

**FETCH**
nRetuned: 208
Execution Time: 3886 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 250
Execution Time: 20 ms

**IXSAN**
nRetuned: 64501
Execution Time: 60 ms

**FETCH**
nRetuned: 250
Execution Time: 4383 ms

![DB Foure Query 4](Image/Query4-4.png)

### Query 5

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.roads.find({
    "coordinate": {
        "$geoIntersects": {
            "$geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        5.358853787183762,
                        36.19515042573396
                    ],
                    [
                        5.359081774950027,
                        36.19512850945663
                    ],
                    [
                        5.359869003295898,
                        36.1951550254457
                    ],
                    [
                        5.360151305794716,
                        36.19850137941764
                    ],
                    [
                        5.360189527273178,
                        36.198600945326575
                    ],
                    [
                        5.360252559185027,
                        36.19865668053554
                    ],
                    [
                        5.360347107052802,
                        36.198682654211595
                    ],
                    [
                        5.3606729954481125,
                        36.19866642066508
                    ]
                ]
            }
        }
    }
})
```

Result

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        144         |          0          |       200005       |              15556               |        no        |  No Index  |

COLLSCAN
nRetuned: 144
Execution Time: 15539 ms
Documents Examined: 200005

![DB one Query 5](Image/Query5-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        144         |       183649        |       183638       |              15306               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183638
Execution Time: 216 ms

**FETCH**
nRetuned: 144
Execution Time: 15064 ms

![DB Two Query 5](Image/Query5-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        144         |       183649        |       183638       |              15711               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183638
Execution Time: 510 ms

**FETCH**
nRetuned: 144
Execution Time: 14991 ms

![DB Three Query 5](Image/Query5-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        144         |       183650        |       183637       |               4115               |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 144
Execution Time: 9 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 60
Execution Time: 10 ms

**IXSAN**
nRetuned: 60383
Execution Time: 101 ms

**FETCH**
nRetuned: 60
Execution Time: 3745 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 37
Execution Time: 10 ms

**IXSAN**
nRetuned: 58753
Execution Time: 29 ms

**FETCH**
nRetuned: 37
Execution Time: 3723 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 47
Execution Time: 0 ms

**IXSAN**
nRetuned: 64501
Execution Time: 86 ms

**FETCH**
nRetuned: 47
Execution Time: 4020 ms

![DB Foure Query 5](Image/Query5-4.png)

### Query 6

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.cities.find(
    {
        "coordinate": {
            "$geoWithin": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -2.1752929687499996,
                                35.22767235493586
                            ],
                            [
                                -1.6809082031249998,
                                33.165145408240285
                            ],
                            [
                                -0.8679199218749999,
                                32.41706632846282
                            ],
                            [
                                7.767333984374999,
                                33.00866349457558
                            ],
                            [
                                7.22900390625,
                                33.96158628979907
                            ],
                            [
                                8.096923828125,
                                34.687427949314845
                            ],
                            [
                                8.63525390625,
                                37.16031654673677
                            ],
                            [
                                2.61474609375,
                                37.17782559332976
                            ],
                            [
                                -2.1752929687499996,
                                35.22767235493586
                            ]
                        ]
                    ]
                }
            }
        }
    }
)
```

Result

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |          0          |      1300010       |               2411               |        no        |  No Index  |

COLLSCAN
nRetuned: 826
Execution Time: 391 ms
Documents Examined: 1300010

![DB one Query 6](Image/Query6-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1249         |        1225        |                24                |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1225
Execution Time: 0 ms

**FETCH**
nRetuned: 826
Execution Time: 9 ms

![DB Two Query 6](Image/Query6-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1249         |        1225        |                8                 |        no        |  2dsphere  |

**IXSAN**
nRetuned: 1225
Execution Time: 0 ms

**FETCH**
nRetuned: 826
Execution Time: 0 ms

![DB Three Query 6](Image/Query6-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        826         |        1252         |        1225        |                11                |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 826
Execution Time: 10 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 826
Execution Time: 0 ms

**IXSAN**
nRetuned: 1225
Execution Time: 1 ms

**FETCH**
nRetuned: 826
Execution Time: 0 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 10 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 0
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

![DB Foure Query 6](Image/Query6-4.png)

### Query 7

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.lands
        .find({
            "coordinate": {
                "$geoWithin": {
                    "$geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    4.88616943359375,
                                    36.357163062654365
                                ],
                                [
                                    5.0042724609375,
                                    35.72421761691415
                                ],
                                [
                                    5.92987060546875,
                                    35.766572101173516
                                ],
                                [
                                    5.943603515625,
                                    36.45000844447082
                                ],
                                [
                                    4.88616943359375,
                                    36.357163062654365
                                ]
                            ]
                        ]
                    }
                }
            }
        }
    )
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |          0          |       200064       |               5164               |        no        |  No Index  |

COLLSCAN
nRetuned: 1
Execution Time: 4950 ms
Documents Examined: 200064

![DB one Query 7](Image/Query7-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       189440        |       189357       |               2507               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 189357
Execution Time: 141 ms

**FETCH**
nRetuned: 1
Execution Time: 1603 ms

![DB Two Query 7](Image/Query7-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       189440        |       189357       |               1807               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 189357
Execution Time: 122 ms

**FETCH**
nRetuned: 1
Execution Time: 880 ms

![DB Three Query 7](Image/Query7-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       189431        |       189356       |               1897               |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 1
Execution Time: 832 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 2
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 10 ms

**IXSAN**
nRetuned: 1
Execution Time: 0 ms

**FETCH**
nRetuned: 0
Execution Time: 0 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 1
Execution Time: 1 ms

**IXSAN**
nRetuned: 189353
Execution Time: 67 ms

**FETCH**
nRetuned: 1
Execution Time: 997 ms

![DB Foure Query 7](Image/Query7-4.png)

### Query 8

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.roads.find(
    {
        "coordinate": {
            "$geoWithin": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [

                            [
                                5.358881950378418,
                                36.19462470395782
                            ],
                            [
                                5.369052886962891,
                                36.192581309214255
                            ],
                            [
                                5.3694820404052725,
                                36.1939666674039
                            ],
                            [
                                5.371112823486328,
                                36.195248101907744
                            ],
                            [
                                5.370726585388184,
                                36.196668045376434
                            ],
                            [
                                5.372915267944336,
                                36.20193200133552
                            ],
                            [
                                5.372185707092285,
                                36.20404441045111
                            ],
                            [
                                5.35858154296875,
                                36.200200475940555
                            ],
                            [
                                5.358881950378418,
                                36.19462470395782
                            ]
                        ]
                    ]
                }
            }
        }
    }
)
```

- Result DB One :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |          0          |       200005       |               5167               |        no        |  No Index  |

COLLSCAN
nRetuned: 1
Execution Time: 5001 ms
Documents Examined: 200005

![DB one Query 8](Image/Query8-1.png)

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       183645        |       183637       |              16659               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183637
Execution Time: 272 ms

**FETCH**
nRetuned: 1
Execution Time: 16378 ms

![DB Two Query 8](Image/Query8-2.png)

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       183645        |       183637       |              11609               |        no        |  2dsphere  |

**IXSAN**
nRetuned: 183637
Execution Time: 146 ms

**FETCH**
nRetuned: 1
Execution Time: 11444 ms

![DB Three Query 8](Image/Query8-3.png)

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         1          |       183650        |       183637       |               4344               |        no        |  2dsphere  |

**SHARED_MEARG**
nRetuned: 1
Execution Time: 15 ms

**SHARDING_ONE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 1
Execution Time: 38 ms

**IXSAN**
nRetuned: 60383
Execution Time: 44 ms

**FETCH**
nRetuned: 1
Execution Time: 4002 ms

SHARDING_TWO_REPLICATION
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 58753
Execution Time: 45 ms

**FETCH**
nRetuned: 0
Execution Time: 3976 ms

**SHARDING_THREE_REPLICATION**
**SHARDING_FILTER**
nRetuned: 0
Execution Time: 0 ms

**IXSAN**
nRetuned: 64501
Execution Time: 84 ms

**FETCH**
nRetuned: 0
Execution Time: 4245 ms

![DB Foure Query 8](Image/Query8-4.png)

### Query 9

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.cities.find({
    "coordinate": {
        "$near":
        {
            "$geometry": {
                "type": "Point",
                "coordinates": [
                    5.358853787183762,
                    36.19515042573396
                ]
            },
            "$minDistance": 1000,
            "$maxDistance": 20000
        }
    }
})
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                9                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 9](Image/Query9-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                4                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 9](Image/Query9-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                5                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Foure Query 9](Image/Query9-4.png) -->

### Query 10

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.lands.find(
    {
        "coordinate": {
            "$near":
            {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [
                        5.410080253975188,
                        36.191711170919284
                    ]
                },
                "$minDistance": 1000,
                "$maxDistance": 20000
            }
        }
    }
)
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               5588               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 10](Image/Query10-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               4130               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 10](Image/Query10-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               4243               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Foure Query 10](Image/Query10-4.png) -->

### Query 11

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.roads.find(
    {
        "coordinate": {
            "$near":
            {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [
                        5.410080253975188,
                        36.191711170919284
                    ]
                },
                "$minDistance": 1000,
                "$maxDistance": 20000
            }
        }
    }
)
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               9743               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 11](Image/Query11-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               7352               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 11](Image/Query11-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               2640               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 11](Image/Query11-4.png) -->

### Query 12

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.cities.find({
    "coordinate": {
        "$nearSphere":
        {
            "$geometry": {
                "type": "Point",
                "coordinates": [
                    5.358853787183762,
                    36.19515042573396
                ]
            },
            "$minDistance": 1000,
            "$maxDistance": 20000
        }
    }
})
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                7                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 12](Image/Query12-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                4                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 12](Image/Query12-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|         3          |         130         |         6          |                5                 |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Foure Query 12](Image/Query12-4.png) -->

### Query 13

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.lands.find(
    {
        "coordinate": {
            "$nearSphere":
            {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [
                        5.410080253975188,
                        36.191711170919284
                    ]
                },
                "$minDistance": 1000,
                "$maxDistance": 20000
            }
        }
    }
)
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               5517               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 13](Image/Query13-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               4216               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 13](Image/Query13-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|        1394        |       378618        |       378601       |               4260               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Foure Query 13](Image/Query13-4.png) -->

### Query 14

Description
<!-- TODO ADD Description -->

Code Of Query

```js
db.roads.find(
    {
        "coordinate": {
            "$nearSphere":
            {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [
                        5.410080253975188,
                        36.191711170919284
                    ]
                },
                "$minDistance": 1000,
                "$maxDistance": 20000
            }
        }
    }
)
```

- Result DB Two :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               9876               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Two Query 14](Image/Query14-2.png) -->

- Result DB Three :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               7368               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Three Query 14](Image/Query14-3.png) -->

- Result DB Foure :

| Documents Returned | Index Keys Examined | Documents Examined | Actual Query Execution Time (ms) | Sorted in Memory | index Uesd |
| :----------------: | :-----------------: | :----------------: | :------------------------------: | :--------------: | :--------: |
|       19187        |       367287        |       367276       |               2630               |        no        |  2dsphere  |

<!-- we cant take screen  shoot properlies -->
<!-- ![DB Foure Query 14](Image/Query14-4.png) -->