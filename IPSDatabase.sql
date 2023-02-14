drop database IPS;
create database IPS;
use IPS;

CREATE TABLE employee
(employee_id VARCHAR(10) NOT NULL,
 employee_fname VARCHAR(255) NOT NULL,
 employee_mname VARCHAR(255),
 employee_lname VARCHAR(255) NOT NULL,
 employee_sex CHAR(1) NOT NULL,
 employee_bday DATE NOT NULL,
 employee_email VARCHAR(255) NOT NULL,
 employee_num CHAR(10),
 employee_emergnum CHAR(10),
CONSTRAINT employee_pk PRIMARY KEY (employee_id));

CREATE TABLE joborder
(joborder_no VARCHAR(10) NOT NULL,
 report_no VARCHAR(10) NOT NULL,
 process VARCHAR(255) NOT NULL,
 status VARCHAR(255) NOT NULL,
CONSTRAINT joborder_pk PRIMARY KEY (joborder_no, report_no));

CREATE TABLE productivity
(report_no VARCHAR(10) NOT NULL,
 employee_id VARCHAR(10) NOT NULL,
 prod_date DATE NOT NULL,
 workinghours TIME,
 remarks TEXT(2000),
 prod_score FLOAT,
CONSTRAINT productivty_pk PRIMARY KEY (report_no),
CONSTRAINT productivity_fk FOREIGN KEY (employee_id) REFERENCES employee(employee_id));

CREATE TABLE history
(history_no VARCHAR(10) NOT NULL,
 employee_id VARCHAR(10) NOT NULL,
 position_id VARCHAR(10) NOT NULL,
 employee_fname VARCHAR(255) NOT NULL,
 employee_mname VARCHAR(255),
 employee_lname VARCHAR(255) NOT NULL,
 position_name VARCHAR(255) NOT NULL,
 position_startdate DATE NOT NULL,
 position_enddate DATE,
CONSTRAINT history_pk PRIMARY KEY (history_no),
CONSTRAINT history_fk1 FOREIGN KEY (employee_id) REFERENCES employee(employee_id));

CREATE TABLE position
(position_id VARCHAR(10) NOT NULL,
 history_no VARCHAR(10) NOT NULL,
 position_name VARCHAR(255) NOT NULL,
 CONSTRAINT position_pk PRIMARY KEY (position_id),
 CONSTRAINT position_fk FOREIGN KEY (history_no) REFERENCES history(history_no));

CREATE TABLE dashboard
(dashboard_id VARCHAR(10) NOT NULL,
 employee_id VARCHAR(10) NOT NULL,
 report_no VARCHAR(255) NOT NULL,
 timespan TIME NOT NULL,
 displaytype VARCHAR(255) NOT NULL,
 total_workinghours TIME NOT NULL,
 contribution VARCHAR(10) NOT NULL,
 avgprodscore FLOAT(5,2) NOT NULL,
CONSTRAINT dashboard_pk PRIMARY KEY (dashboard_id),
CONSTRAINT dashboard_fk1 FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
CONSTRAINT dashboard_fk2 FOREIGN KEY (report_no) REFERENCES productivity(report_no));


/* sample working hours 
INSERT INTO my_table (id, duration) VALUES (1, INTERVAL '2:30' HOUR TO MINUTE);

   sample date
INSERT INTO my_table (id, my_date) VALUES (1, '2023-02-13');

   sample productivity_score
INSERT INTO my_table (id, productivity_score) VALUES (1, 7.5);

*/

