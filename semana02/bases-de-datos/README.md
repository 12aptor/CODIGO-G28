# PostgreSQL

## Crear tablas

```sql
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    director VARCHAR(100),
    year INT,
    length_minutes INT
);

CREATE TABLE boxoffice (
    id SERIAL PRIMARY KEY,
    domestic_sales INT,
    movie_id INT
);
```

## Insertar registros

```sql
INSERT INTO movies (title, director, year, length_minutes)
VALUES ('Toy Story', 'John Lasseter', 1995, 81);

INSERT INTO movies (title, director, year, length_minutes)
VALUES
    ('Finding Nemo', 'Andrew Stanton', 2003, 100),
    ('The Incredibles', 'Brad Bird', 2004, 115),
    ('Ratatouille', 'Brad Bird', 2007, 111),
    ('Up', 'Pete Docter', 2009, 96),
    ('Toy Story 3', 'Lee Unkrich', 2010, 103),
    ('Inside Out', 'Pete Docter', 2015, 95),
    ('Coco', 'Lee Unkrich', 2017, 105),
    ('Toy Story 4', 'Josh Cooley', 2019, 100),
    ('Soul', 'Pete Docter', 2020, 100);

INSERT INTO boxoffice (domestic_sales, movie_id)
VALUES
    (100, 1),
    (115, 2),
    (111, 3),
    (96, 4),
    (103, 5);
```

## Consultar registros

## SELECT

```sql
-- Seleccionar todos los registros
SELECT * FROM movies;

-- Seleccionar campos específicos
SELECT id, title, director FROM movies;

-- Seleccionar registros con condición
SELECT * FROM movies WHERE id = 1;
```

## Busqueda con restricciones

- =, !=, <, >, <=, <=: Operadores de comparación para valores numéricos y de texto.
    ```sql
    SELECT * FROM movies WHERE year = 2003;
    ```

- **BETWEEN**: Filtrar por rango de valores.
    ```sql
    SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
    ```

- **IN**: Filtrar por lista de valores.
    ```sql
    SELECT * FROM movies WHERE year IN (2000, 2005, 2010);
    ```

- **LIKE**: Filtrar por patrón de texto.
    ```sql
    SELECT * FROM movies WHERE title LIKE 'Toy%';
    ```

- **%**: Cualquier cadena de caracteres.

- **_**: Cualquier caracter.

## Ordenar resultados

- **ORDER BY**: Ordenar resultados.
    ```sql
    SELECT * FROM movies ORDER BY id DESC;
    ```

- **ASC**: Ordenar de forma ascendente.
- **DESC**: Ordenar de forma descendente.

## Limitar resultados

- **LIMIT**: Limitar cantidad de resultados.
    ```sql
    SELECT * FROM movies LIMIT 5;
    ```

- **OFFSET**: Desplazar resultados.
    ```sql
    SELECT * FROM movies LIMIT 5 OFFSET 5;
    ```

## Operadores AND, OR y NOT

- **AND**: Operador lógico Y.
    ```sql
    SELECT * FROM movies WHERE year >= 2000 AND year <= 2010;
    ```

- **OR**: Operador lógico O.
    ```sql
    SELECT * FROM movies WHERE year = 2003 OR year = 2010;
    ```

- **NOT**: Operador lógico NOT.
    ```sql
    SELECT * FROM movies WHERE NOT YEAR = 2003;
    ```

## Operador UPDATE

- **UPDATE**: Actualizar registros.
    ```sql
    UPDATE movies SET year = 2020 WHERE id = 1;
    ```

## Operador DELETE

- **DELETE**: Eliminar registros.
    ```sql
    DELETE FROM movies WHERE id = 1;
    ```

## Operador JOIN

- **JOIN**: Unir tablas.
    ```sql
    SELECT title, domestic_sales
    FROM movies
    JOIN boxoffice ON movies.id = boxoffice.movie_id;
    ```