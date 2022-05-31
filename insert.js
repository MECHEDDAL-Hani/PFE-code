use("myDB");

// cities

db.cities.insertOne({
    "name": "P1",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            -5,
            5
        ]
    },
    "description": "Non neque velit modi sit voluptatem est sed. Dolor non quisquam sed neque dolor."
});

db.cities.insertOne({
    "name": "P2",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            6,
            6
        ]
    },
    "description": "Non neque velit modi sit voluptatem est sed. Dolor non quisquam sed neque dolor."
});

db.cities.insertOne({
    "name": "P3",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            3,
            -3
        ]
    },
    "description": "Non neque velit modi sit voluptatem est sed. Dolor non quisquam sed neque dolor."
});

db.cities.insertOne({
    "name": "P4",
    "coordinate": {
        "type": "Point",
        "coordinates": [
            -2,
            -2
        ]
    },
    "description": "Non neque velit modi sit voluptatem est sed. Dolor non quisquam sed neque dolor."
});


// lands

db.lands.insertOne({
    name: "L1",
    coordinate: {
        type: "Polygon",
        coordinates: [
            [
                [-9, 9],
                [-5, 8],
                [-8, 5],
                [-11, 6],
                [-9, 9],
            ],
        ],
    },
    description: "Sit dolore ipsum tempora ipsum.",
});

db.lands.insertOne({
    name: "L2",
    coordinate: {
        type: "Polygon",
        coordinates: [
            [
                [6, 6],
                [6, 5],
                [4, 3],
                [2, 5],
                [6, 6],
            ],
        ],
    },
    description: "Sit dolore ipsum tempora ipsum.",
});

db.lands.insertOne({
    name: "L3",
    coordinate: {
        type: "Polygon",
        coordinates: [
            [
                [2, 2],
                [2, -2],
                [-2, -2],
                [-2, 2],
                [2, 2],
            ],
        ],
    },
    description: "Sit dolore ipsum tempora ipsum.",
});

db.lands.insertOne({
    name: "L4",
    coordinate: {
        type: "Polygon",
        coordinates: [
            [
                [6, 11],
                [10, 2],
                [4, -6],
                [-5, 3],
                [6, 11],
            ],
        ],
    },
    description: "Sit dolore ipsum tempora ipsum.",
});

// roads

db.roads.insertOne({
    name: "R1",
    coordinate: {
        type: "LineString",
        coordinates: [
            [-2, 2],
            [2, 2],
            [2, 5],
            [4, 5],
            [6, 7],
        ],
    },
    description: "Quaerat velit dolorem adipisci sed labore etincidunt.",
});

db.roads.insertOne({
    name: "R2",
    coordinate: {
        type: "LineString",
        coordinates: [
            [-4, 4],
            [1, 4],
            [2, -2],
            [7, -2],
            [9, 2],
        ],
    },
    description: "Quaerat velit dolorem adipisci sed labore etincidunt.",
});

db.roads.insertOne({
    name: "R3",
    coordinate: {
        type: "LineString",
        coordinates: [
            [-4, 9],
            [11, 9],
            [4, -4],
            [-3, -4],
        ],
    },
    description: "Quaerat velit dolorem adipisci sed labore etincidunt.",
});
