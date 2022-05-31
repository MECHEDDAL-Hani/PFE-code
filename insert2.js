use("myDB");

// cities

db.cities.insertOne({
    "name": "Universite Ferhat Abbas",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            5.358853787183762,
            36.19515042573396
        ]
    },
    "description": "Universite Ferhat Abbas Location."
});

db.cities.insertOne({
    "name": "Park Mall Sétif",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            5.410080253975188, 36.191711170919284
        ]
    },
    "description": "Centre commercial & de loisirs Park Mall Sétif."
});


db.lands.insertOne({
    name: "Universite Ferhat Abbas area",
    coordinate: {
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
    },
    description: "Universite Ferhat Abbas Area.",
});

db.roads.insertOne({
    name: "Universite Ferhat Abbas Path",
    coordinate: {
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
    description: "Universite Ferhat Abbas Path to computer science departement.",
});


db.roads.insertOne({
    name: "Algeria East-West Highway",
    coordinate: {
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
    },
    description: "Algeria East-West Highway",
});
