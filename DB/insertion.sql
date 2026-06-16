INSERT INTO person
(first_name, last_name, gender, birth_date)
VALUES
('Nicolas', 'Martou', 'M', '2000-12-02'),
('John', 'Doe', 'M', '1988-02-16'),
('Allan', 'Vanem', 'M', '1995-01-01'),
('Tyler', 'Joseph', 'M', '1989-07-03'),
('Josh', 'Dun', 'M', '1991-12-12'),
('Sabrina', 'Carpenter', 'F', '1998-05-24'),
('Dwayne', 'Johnson', 'M', '1973-06-25');

INSERT INTO address
(street, appartment_number, postcode, city, country)
VALUES
('Avenue Emile Zola 44', '201', 1348, 'Louvain-la-Neuve', 'Belgium'),
('Avenue Emile Zola 44', '202', 1300, 'Wavre', 'Belgium'),
('Avenue Emile Zola 44', '203', 1348, 'Louvain-la-Neuve', 'Belgium'),
('Avenue Emile Zola 42', '101', 1348, 'Louvain-la-Neuve', 'Belgium'),
('Avenue Emile Zola 44', '102', 1500, 'Incourt', 'Belgium'),
('Avenue Emile Zola 43', NULL, 1348, 'Louvain-la-Neuve', 'Belgium'),
('Avenue Emile Zola 48', '301', 75002, 'Paris', 'France');

INSERT INTO property
(price, property_type, address_id)
VALUES
(259000, 'APPARTMENT', 1),
(189000, 'APPARTMENT', 2),
(310000, 'APPARTMENT', 3),
(120000, 'APPARTMENT', 4),
(225000, 'APPARTMENT', 5),
(435000, 'HOUSE', 6),
(1500000, 'APPARTMENT', 7);

INSERT INTO property_history
(start_date, end_date, property_id, contract_id)
VALUES
('2026-01-01', NULL, 1, NULL),
('2026-02-01', NULL, 2, NULL),
('2026-03-01', NULL, 3, NULL),
('2026-04-01', NULL, 4, NULL),
('2026-05-01', NULL, 5, NULL),
('2026-06-01', NULL, 6, NULL),
('2026-06-15', NULL, 7, NULL);

INSERT INTO bank_account
(iban, swift_code)
VALUES
('BE10542318759684', NULL),
('BE10542318759684', 'BBRUBEBB'), -- ING belgium
('852964178', 'FDRLINBBIBD'), -- Federal bank of India
('BE10542318759684', NULL),
('BE10542318759684', NULL),
('BE10542318759684', NULL);