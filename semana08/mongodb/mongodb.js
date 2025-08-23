db.customers.insertOne({
    name: "Charlie Brown",
    age: 40,
    tags: ["cool", "funny"],
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        coordinates: {
            latitude: 37.4224764,
            longitude: -122.0842499
        }
    }
})