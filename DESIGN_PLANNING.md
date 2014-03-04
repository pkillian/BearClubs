BearClubs  
Design and Planning Document  
*03/02/2014, version 1.0*  

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## System Architecture

### Client-Server Overview

We will be creating a client-server web application. We will follow a Model-View-Controller (MVC) pattern, using HTML5/JavaScript for the client and Django for the server side. The key components in this system will be:

* Database: We will store relevant raw data/information about our users, organizations, and events in a PostgreSQL database.

* Backend Server: The server will be implemented in Django. It will access the database for raw data and communicate with the client for sending and receiving data requests/responses.

* Frontend Web Client: We will implement the client using HTML5/CSS to display information and JavaScript to transfer and parse data to and from the server as needed.

### MVC/MTV Overview

Django follows the MVC pattern, but instead calls it MTV for Model-Template-View. In this case, MTV's "template" is like the "view" in MVC and MTV's "view" is similar to the "controller" in MVC. We describe the MTV components in more detail below:

* Model: This describes the database tables, allowing us to create, retrieve, update, and delete records about our users, organizations, and events. The model will also provide the business logic, manipulation of data to carry out functionalities needed for the application.

* View: This deals with data requests from the client side and returns appropriate responses. It renders data for the templates that will be displayed in the web client.

* Template: This is the part that creates what the user actually sees when using the application. We use HTML5/CSS to create templates and determine what data to display and how to display it. We use JavaScript to request data that needs to be displayed.

## Design Details

## Implementation Plan

## Testing Plan


