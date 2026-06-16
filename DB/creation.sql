-- Drop tables

DROP TABLE IF EXISTS property;
DROP TABLE IF EXISTS property_type;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS subcontractor;
DROP TABLE IF EXISTS subcontractor_type;
DROP TABLE IF EXISTS role_person;
DROP TABLE IF EXISTS address;

-- Create table

CREATE TABLE address
(
    id_address SERIAL,
    street VARCHAR(100) NOT NULL,
    postcode INTEGER NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(30) NOT NULL,
    
    CONSTRAINT pk_id_address PRIMARY KEY(id_address)
)

CREATE TABLE role_type
(
    id_role_type SERIAL,
    name VARCHAR(50) NOT NULL,

    CONSTRAINT pk_id_role_type PRIMARY KEY(id_role_type)
)

CREATE TABLE role_person
(
    id_role SERIAL,
    role_type_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,

    CONSTRAINT pk_id_role PRIMARY KEY(id_role)
)

CREATE TABLE subcontractor_type
(
    id_subcontractor_type SERIAL,
    name VARCHAR(30) NOT NULL,

    CONSTRAINT pk_id_subcontractor_type PRIMARY KEY
)

CREATE TABLE subcontractor
(
    id_subcontractor SERIAL,
    vat_number INTEGER(10) NOT NULL,
    legal_name VARCHAR(100) NOT NULL,
    bank_accont VARCHAR(50) NULL,
    swift_code VARCHAR(11) NULL, -- 8 -> 11 chars
    subcontractor_type_id INTEGER NOT NULL,

    CONSTRAINT pk_id_subcontractor PRIMARY KEY,
    CONSTRAINT fk_subcontractor_type_id FOREIGN KEY(subcontractor_type_id) REFERENCES subcontractor_type(id_subcontractor_type)
)

CREATE TABLE person
(
    id_person SERIAL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role_id INTEGER NOT NULL,
    
    CONSTRAINT pk_id_person PRIMARY KEY(id_person),
    CONSTRAINT fk_role_id FOREIGN KEY(role_id) REFERENCES role_person(id_role)
)

CREATE TABLE property_type
(
    id_property_type SERIAL,
    name VARCHAR(50) NOT NULL,

    CONSTRAINT pk_id_property_type PRIMARY KEY(id_property_type)
)

CREATE TABLE property
(
    id_property SERIAL,
    price MONEY NOT NULL,
    location_price MONEY,
    address_id INTEGER NOT NULL,

    CONSTRAINT pk_id_property PRIMARY KEY(id_property),
    CONSTRAINT fK_address_id FOREIGN KEY(address_id) REFERENCES address(id_address)
)

CREATE TABLE project_type
(
    id_project_type SERIAL,
    name VARCHAR(50)
)

CREATE TABLE project_type
(
    id_project_type SERIAL,
    name VARCHAR(100) NOT NULL,

    CONSTRAINT pk_id_project PRIMARY KEY(id_project)
)

CREATE TABLE project
(
    id_project SERIAL,
    owner_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    project_type_id INTEGER NOT NULL,

    CONSTRAINT pk_id_project PRIMARY KEY(id_project),
    CONSTRAINT fk_owner_id FOREIGN KEY(owner_id) REFERENCES person(id_person),
    CONSTRAINT fk_property_id FOREIGN KEY(property_id) REFERENCES property(id_property),
    CONSTRAINT fk_project_type_id FOREIGN KEY(project_type_id) REFERENCES project_type(id_project_type)
)

CREATE TABLE project_subcontractor
(
    id_project_subcontractor SERIAL,
    project_id INTEGER NOT NULL,
    subcontractor_id INTEGER NOT NULL,

    CONSTRAINT pk_id_project_subcontractor PRIMARY KEY(id_project_subcontractor),
    CONSTRAINT fk_project_id FOREIGN KEY(project_id) REFERENCES project(id_project),
    CONSTRAINT fk_subcontractor_id FOREIGN KEY(subcontractor_id) REFERENCES subcontractor(id_subcontractor)
)