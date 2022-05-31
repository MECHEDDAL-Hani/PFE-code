use("myDB");

print(1);
print(db.cities.find(
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
).explain("executionStats").executionStats.executionTimeMillis);


print(2);
print(db.cities.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(3);


print(
    db.lands
        .find({
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
                    },
                },
            },
        })
        .explain("executionStats").executionStats.executionTimeMillis);

print(4);


print(db.roads.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(5);


print(db.roads.find({
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
            },
        },
    },
}).explain("executionStats").executionStats.executionTimeMillis);

print(6);
print(db.cities.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(7);
print(
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
                    },
                },
            },
        })
        .explain("executionStats").executionStats.executionTimeMillis);

print(8);
print(db.roads.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(9);

print(db.cities.find({
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
}).explain("executionStats").executionStats.executionTimeMillis);

print(10);

print(db.lands.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(11);
print(db.roads.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(12);

print(db.cities.find({
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
}).explain("executionStats").executionStats.executionTimeMillis);

print(13);
print(db.lands.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

print(14);
print(db.roads.find(
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
).explain("executionStats").executionStats.executionTimeMillis);

exit();
