use datarepresentation;
create table staff (
staffID int AUTO_INCREMENT,
name varchar(250),
role varchar(250),
expertise varchar(250),
availability int,
PRIMARY Key (staffID),
FOREIGN KEY (role) REFERENCES costing(role));
alter table staff AUTO_INCREMENT = 101;
