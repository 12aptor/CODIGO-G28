const express = require("express");
const morgan = require("morgan");

const app = express();

app.use(express.json());
app.use(morgan("dev"));

app.get("/", (req, res) => {
  res.send("Hola mundo");
});

app.get("/hola/:nombre", (req, res) => {
  const nombre = req.params.nombre;
  res.send(`Hola ${nombre}`);
});

app.get("/usuario", (req, res) => {
  res.status(200).json({
    id: 1,
    nombre: "Eduardo",
    email: "eduardo@gmail.com",
  });
});

app.post("/usuario", (req, res) => {
  const usuario = req.body;

  res.status(200).json(usuario);
});

app.listen(3000, () => {
  console.log("Servidor corriendo en http://localhost:3000");
});
