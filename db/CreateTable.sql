CREATE TABLE IF NOT EXISTS room
             (
                          pk         INTEGER NOT NULL AUTO_INCREMENT,
                          room_name VARCHAR(30) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS plant
             (
                          pk         INTEGER NOT NULL AUTO_INCREMENT,
                          plant_name VARCHAR(30) NOT NULL,
                          plant_desc VARCHAR(500) NOT NULL,
                          flowers    VARCHAR(10) NOT NULL,
                          watering_req VARCHAR(20) NOT NULL,
                          fk_room_pk INTEGER NOT NULL,   
                          PRIMARY KEY (id),
                          FOREIGN KEY (fk_room_pk) REFERENCES room(pk)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




