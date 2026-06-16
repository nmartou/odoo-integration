-- Create table

CREATE TABLE address
(
    id_address SERIAL,
    street VARCHAR(100) NOT NULL,
    appartment_number VARCHAR(10),
    postcode INTEGER NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(30) NOT NULL,
    
    CONSTRAINT pk_id_address PRIMARY KEY(id_address)
);

CREATE TABLE bank_account
(
    id_bank_account SERIAL,
    iban VARCHAR(50) NOT NULL,
    swift_code VARCHAR(11), -- 8 -> 11

    CONSTRAINT pk_id_bank_account PRIMARY KEY(id_bank_account)
);

CREATE TABLE person
(
    id_person SERIAL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    bank_account_id INTEGER,
    
    CONSTRAINT pk_id_person PRIMARY KEY(id_person),
    CONSTRAINT fk_bank_account_id FOREIGN KEY(bank_account_id) REFERENCES bank_account(id_bank_account)
);

CREATE TABLE subcontractor
(
    id_subcontractor SERIAL,
    vat_number INTEGER NOT NULL,
    legal_name VARCHAR(100) NOT NULL,
    bank_account_id INTEGER,
    subcontractor_type VARCHAR(30) NOT NULL,

    CONSTRAINT pk_id_subcontractor PRIMARY KEY(id_subcontractor),
    CONSTRAINT fk_bank_account_id FOREIGN KEY(bank_account_id) REFERENCES bank_account(id_bank_account)
);

CREATE TABLE property
(
    id_property SERIAL,
    price MONEY NOT NULL,
    property_type VARCHAR(30) NOT NULL,
    address_id INTEGER NOT NULL,

    CONSTRAINT pk_id_property PRIMARY KEY(id_property),
    CONSTRAINT fK_address_id FOREIGN KEY(address_id) REFERENCES address(id_address)
);

CREATE TABLE role_person
(
    id_role SERIAL,
    role_name VARCHAR(30) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    person_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,

    CONSTRAINT pk_id_role PRIMARY KEY(id_role),
    CONSTRAINT fk_person_id FOREIGN KEY(person_id) REFERENCES person(id_person),
    CONSTRAINT fk_property_id FOREIGN KEY(property_id) REFERENCES property(id_property)
);

CREATE TABLE project
(
    id_project SERIAL,
    owner_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    project_type VARCHAR(30) NOT NULL,
    status VARCHAR(30) NOT NULL,
    property_id INTEGER NOT NULL,

    CONSTRAINT pk_id_project PRIMARY KEY(id_project),
    CONSTRAINT fk_owner_id FOREIGN KEY(owner_id) REFERENCES person(id_person),
    CONSTRAINT fk_property_id FOREIGN KEY(property_id) REFERENCES property(id_property)
);

CREATE TABLE project_subcontractor
(
    id_project_subcontractor SERIAL,
    project_id INTEGER NOT NULL,
    subcontractor_id INTEGER NOT NULL,

    CONSTRAINT pk_id_project_subcontractor PRIMARY KEY(id_project_subcontractor),
    CONSTRAINT fk_project_id FOREIGN KEY(project_id) REFERENCES project(id_project),
    CONSTRAINT fk_subcontractor_id FOREIGN KEY(subcontractor_id) REFERENCES subcontractor(id_subcontractor)
);

CREATE TABLE contract
(
    id_contract SERIAL,
    name_type VARCHAR(30),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    amount MONEY NOT NULL,
    payment_interval VARCHAR(10) NOT NULL,
    is_owner BOOLEAN NOT NULL DEFAULT FALSE,
    rent_collection BOOLEAN NOT NULL DEFAULT FALSE,
    rent_indexation BOOLEAN NOT NULL DEFAULT FALSE,
    payment_reminders BOOLEAN NOT NULL DEFAULT FALSE,
    rental_guarantees BOOLEAN NOT NULL DEFAULT FALSE,
    service_charges BOOLEAN NOT NULL DEFAULT FALSE,
    repairs BOOLEAN NOT NULL DEFAULT FALSE,
    insurance_unpaid_rent BOOLEAN NOT NULL DEFAULT FALSE,
    legal_cover BOOLEAN NOT NULL DEFAULT FALSE,

    CONSTRAINT pk_id_contract PRIMARY KEY(id_contract)
);

CREATE TABLE property_history
(
    id_property_history SERIAL,
    start_date DATE NOT NULL,
    end_date DATE,
    property_id INTEGER NOT NULL,
    contract_id INTEGER NOT NULL,

    CONSTRAINT pk_id_property_history PRIMARY KEY(id_property_history),
    CONSTRAINT fk_property_id FOREIGN KEY(property_id) REFERENCES property(id_property),
    CONSTRAINT fk_contract_id FOREIGN KEY(contract_id) REFERENCES contract(id_contract)
);

CREATE TABLE contract_party
(
    id_contract_party SERIAL,
    contract_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    guarantor_id INTEGER,

    CONSTRAINT pk_id_contract_party PRIMARY KEY(id_contract_party),
    CONSTRAINT fk_contract_id FOREIGN KEY(contract_id) REFERENCES contract(id_contract),
    CONSTRAINT fk_owner_id FOREIGN KEY(owner_id) REFERENCES person(id_person),
    CONSTRAINT fk_tenant_id FOREIGN KEY(tenant_id) REFERENCES person(id_person),
    CONSTRAINT fk_guarantor_id FOREIGN KEY(guarantor_id) REFERENCES person(id_person)
);

CREATE TABLE payment
(
    id_payment BIGSERIAL,
    due_date DATE NOT NULL,
    paid_date DATE,
    status VARCHAR(30) NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    invoice_id INTEGER, --NOT NULL but require invoicing
    project_id INTEGER,
    contract_party_id INTEGER,

    CONSTRAINT pk_id_payment PRIMARY KEY(id_payment),
    -- CONSTRAINT fk_invoice_id FOREIGN KEY(invoice_id) REFERENCES invoice(id_invoice),
    CONSTRAINT fk_project_id FOREIGN KEY(project_id) REFERENCES project(id_project),
    CONSTRAINT fk_contract_party_id FOREIGN KEY(contract_party_id) REFERENCES contract_party(id_contract_party)
);