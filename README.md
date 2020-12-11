# Data Representation Project

This github repository contains my project submission for the Data Representation module.

For any queries relating to this repository please reach out to G00283361@gmit.ie.

***

## Overview

For this assessment I have chosen to develop a web application which functions as a resource management tool.

The application relies on two database tables; a staff table and a costing table.

The functionality of the web application is as follows:

 - View the pool of available resources, including their areas of expertise and their weekly hours of availability;
 
 - View the charge rates assigned to each role within the organisation hierarchy;
 
 - Book a resource by reducing their hoours of availability;
 
 - Delete a resource who no longer works for the organisation;
 
 - Promote a resource to a new role within the organisation;
 
 - Calculate the cost of booking a certain role for a defined number of hours.
 
The redirects and on-page links should allow for full navigation of the site from the root page, without having to manually manipulate the web address.

Details of the interface developed underlying the functionality of the web application can be found in the .pptx file found within this repository.

***

## Pythonanywhere

This web application can also be accessed at the following web address:

http://dervlacandon.pythonanywhere.com/

Testing of the hosted webpage has highlighted that a 500 internal server error is not an uncommon occurence, due to the free account used and the number of consoles available for use.

If 500 internal server errors arise when visiting the webpage, please reach out to the e-mail address listed above in order to refresh the consoles and resolve the issues.

***

## Initiation

Please use the ```dbconfigtemplate.py``` file to create your own version of dbconfig.py with the appropriate username and password.

I have supplied two sql files which can be used to create the database tables needed to execute the code, and ```tesOfficeDao.py``` contains sample json variables to allow you to create the initial values in the database. The 4 entries in the costing table are mandatory, but staff entries are customisable by the user, provided the roles are found in the costing table.

Then, to initiate a local instance of this web application, just run the file ```server.py``` and visit the root page.

Enjoy!

***
