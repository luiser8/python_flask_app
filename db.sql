create database course_flask

CREATE TABLE users
(
    id              serial PRIMARY KEY,
    firstname       varchar NOT NULL,
    lastname        varchar NOT NULL,
    email           varchar NOT NULL,
    password        varchar NOT NULL,
    status          boolean NULL DEFAULT true,
    createdat       TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updatedat       TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publicaciones
(
    id              	serial PRIMARY KEY,
    titulo		    	varchar NOT NULL,
    descripcion     	varchar NOT NULL,
    descripcion_full    text NOT NULL,
    status          	boolean NULL DEFAULT true,
    createdat       	TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updatedat       	TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);
