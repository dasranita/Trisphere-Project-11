CREATE TABLE rooms(id serial PRIMARY KEY, property text NOT NULL, city text NOT NULL, price integer NOT NULL CHECK(price>0));
CREATE TABLE bookings(id uuid PRIMARY KEY, room_id int REFERENCES rooms, owner text NOT NULL, arrival date NOT NULL, departure date NOT NULL CHECK(departure>arrival), status text NOT NULL CHECK(status IN ('held','confirmed','cancelled','expired','failed')), expires timestamptz NOT NULL, total integer NOT NULL, payment_ref text UNIQUE);
CREATE INDEX booking_room ON bookings(room_id,arrival,departure);
INSERT INTO rooms(property,city,price) VALUES ('Sunrise Hotel','Kolkata',250000),('Ocean View','Goa',350000),('Mountain Retreat','Darjeeling',280000);
