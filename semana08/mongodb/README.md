# MongoDB

## Instalación

- Instalar MongoDB Server
- Instalar MongoDB Compass
- Instalar MongoDB Shell

## Abrir MongoDB Shell

```bash
mongosh
```

## Listar las bases de datos

```bash
show dbs
```

## Crear o conecta a una base de datos

```bash
db.createCollection("nombre_de_la_coleccion")
# ó
db.nombre_de_la_coleccion.insertOne({key: "value"})
```

## Insertar datos en una colección

```javascript
db.customers.insertOne({ name: "John Doe", age: 30 })

db.customers.insertMany([
    { name: "Bob Smith", age: 35 }
    { name: "Alice Johnson", age: 33 }
])
```

## Consultar datos en una colección

```javascript
db.customers.find()
db.customers.find({
    name: "Alice Johnson"
})
db.customers.find({
    age: 30
})
db.customers.findOne({
    age: 30
})
```

## Actualizar datos en una colección

```javascript
db.customers.updateOne(
    { name: "Alice Johnson" },
    { $set: { age: 31 } }
)
db.customers.updateMany(
    { age: { $lt: 30 } },
    { $set: { age: 31 } }
)
```

## Eliminar datos en una colección

```javascript
db.customers.deleteOne({
    name: "Alice Johnson"
})
db.customers.deleteMany({
    age: { $lt: 30 }
})
```

## Eliminar propiedades de un documento

```javascript
db.customers.updateOne(
    { _id: ObjectId('68a9209253e0509eb5eec4aa') },
    { $unset: { tags: 1 } }
)
```

## Ordenar datos en una colección

```javascript
db.customers.find().sort({ age: -1 })
// 1: Ascendente
// -1: Descendente
```

## Limitar los resultados de una consulta

```javascript
db.customers.find().sort({ age: 1 }).limit(2)
```

## Paginar los resultados de una consulta

```javascript
db.customers.find().sort({ age: 1 }).skip(2).limit(2)
```