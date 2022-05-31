"""_summary_"""
import pymongo

MY_CONNECTION_URL = "mongodb://root:root@127.0.0.1:27001/?authSource=admin"


class Mongodb:
    """_summary_"""

    def __init__(self, connection_url=MY_CONNECTION_URL, database_name="myDB"):
        self.connection_url = connection_url
        self.client = pymongo.MongoClient(self.connection_url)
        self.database_name = database_name
        self.database = self.client[self.database_name]

    def query_one(self):
        """ Docstring """

        collection = self.database["cities"]
        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoIntersects": {
                    "$geometry": polygon
                }
            }
        }
        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_two(self):
        """ Docstring """
        collection = self.database["cities"]

        line_string = {
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

        my_filter = {
            "coordinate": {
                "$geoIntersects": {
                    "$geometry": line_string
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_three(self):
        """ Docstring """

        collection = self.database["lands"]

        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoIntersects": {
                    "$geometry": polygon
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_four(self):
        """ Docstring """
        collection = self.database["roads"]

        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoIntersects": {
                    "$geometry": polygon
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_five(self):
        """ Docstring """
        collection = self.database["roads"]

        line_string = {
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

        my_filter = {
            "coordinate": {
                "$geoIntersects": {
                    "$geometry": line_string
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_six(self):
        """ Docstring """
        collection = self.database["cities"]

        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoWithin": {
                    "$geometry": polygon
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_seven(self):
        """ Docstring """
        collection = self.database["lands"]

        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoWithin": {
                    "$geometry": polygon
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def query_eight(self):
        """ Docstring """
        collection = self.database["roads"]

        polygon = {
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

        my_filter = {
            "coordinate": {
                "$geoWithin": {
                    "$geometry": polygon
                }
            }
        }

        return collection.find(
            filter=my_filter
        ).explain()["executionStats"]["executionTimeMillis"]

    def run(self):
        n = self.query_one()
        print(f"Query 1 :{n}")

        n = self.query_two()
        print(f"Query 2 :{n}")

        n = self.query_three()
        print(f"Query 3 :{n}")

        n = self.query_four()
        print(f"Query 4 :{n}")

        n = self.query_five()
        print(f"Query 5 :{n}")

        n = self.query_six()
        print(f"Query 6 :{n}")

        n = self.query_seven()
        print(f"Query 7 :{n}")

        n = self.query_eight()
        print(f"Query 8 :{n}")


if __name__ == "__main__":

    # mongodb = Mongodb()
    Mongodb().run()
