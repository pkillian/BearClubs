BearClubs  
Design and Planning Document  
*03/02/2014, version 1.0*  

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## System Architecture

### Client-Server Overview

We will be creating a client-server web application. We will follow a Model-View-Controller (MVC) pattern, using HTML5/JavaScript for the client and Django for the server side. The key components in this system will be:

* Database: We will store relevant raw data/information about our users, organizations, and events in a database.

* Backend Server: The server will be implemented in Django. It will access the database for raw data and communicate with the client for sending and receiving data requests/responses.

* Frontend Web Client: We will implement the client using HTML5/CSS to display information and JavaScript to transfer and parse data to and from the server as needed.

### MVC/MTV Overview

Django follows the MVC pattern, but instead calls it MTV for Model-Template-View. In this case, MTV's "template" is like the "view" in MVC and MTV's "view" is similar to the "controller" in MVC. We describe the MTV components in more detail below:

* Model: This describes the database tables, allowing us to create, retrieve, update, and delete records about our users, organizations, and events. The model will also provide the business logic, manipulation of data to carry out functionalities needed for the application.

* Template: This is the part that creates what the user actually sees when using the application. We use HTML5/CSS to create templates and determine what data to display and how to display it. We use JavaScript to request data that needs to be displayed.

* View: This deals with data requests from the client side and returns appropriate responses. It renders data for the templates that will be displayed in the web client.

## Design Details

### Frontend App Details

On the frontend, BearClubs will intially be primarily a web-based application. We decided to forgo mobile platforms for now since we foresee the majority of our users to access from a web browser. Our app is for users to discover and connect with new clubs and administrators to manage their club presence on our platform, and a "mobile" aspect does not seem to add much value. The experience seems to be best served on traditional browser interfaces for now. Perhaps once our platform is fully built out with a healthy user base, then we may consider adding on a mobile interface.

Our fontend code will primarily be HTML5/CSS/JavaScript, and we plan to test and support the latest stable versions of major browsers, including Chrome, Firefox, Safari, and Internet Explorer. 

### Backend Server Details

Our backend will be written in Django. The server will process incoming requests and manage access to the global database, as well as build and serve pages and manage password encryption and authentication. There are many Django packages that can help us manage these tasks. Since our application is targeted for UC Berkeley students, we are also considering running our user registration and authentication system through CalNet at a later stage.

### Database Details

We will be using SQLite for locally for speed of development and ease of use, but our production model will implement PostgreSQL for scale and performance. Our database will store users and their related profile information, organizations and their related profile information, events and their relevant information, as well as provide mappings between these three main models:

Users: username, email, first name, last name
Organization: name, description, office, contact info, type
Event: name, description, start time, end time, location

We will also have mapping / relational tables to link our users to organizations and events to organizations. See TABLES.md for diagram.

### Invariants

Users:
* Must have valid username.
* Must have valid email.
* Must have valid first name and last name.

Organization:
* Must have at least one admin user associated.
* Must have valid name.
* Must have valid contact info.

Events:
* Must be associated with exactly one club (must have clubid field).
* Must have valid name.
* Must have start time and end time (start time must be before end time).

## Implementation Plan

### Iteration 1

For Iteration 1, we want to implement the basic core features that will define BearClubs. These core features will be the user stories that we listed in our specification. There are 6 user stories that we want to implement specifically:
* Initial Launch: Presenting Sign In/Sign Up page so that users can sign up or sign in
* Signed In User Launch: Allowing previously logged in users navigation of BearClubs with "signed in" privileges
* Sign In: Allowing users to sign in via a sign in button
* Sign Up: Present the sign up process via sign up button
* Add Club: User can create a club that he or she is apart of
* View Directory of Clubs: Allow users to see a directory of the clubs at the club URL

In order to accomplish these 6 stores in an efficient manner, we want to break it down into separate development tasks. Given the 6 members in our group, we would like to break down our group of 6 into teams of 2. From here, we will divide the 6 stories across our teams 3 so that every team is responsible for 2 stories.

In terms of dependencies, we believe that we've already mitigated most of the possible dependencies. Our group has created mockups for each model, and we have hashed out and finalized how the backend will work. After doing this, we believe that implementing our first iteration through our proposed implementation plan will be straightforward since there will be minimal conflict. We do acknowledge that a potential risk would be that the front-end views will conflict across the 3 teams. To mitigate this, we believe that unifying the front-ends at the end of implementaiton will be easiest. Coupling this with a common naming convention across the team will help unify our front-ends to be one them.

##### Entire BearClubs Team Tasks (These will happen first)

* 1) Create models for each class: User, Club, user\_to\_clubs, club\_to\_events (1 Day)
* 2) Create naming convention for front-end design (1 Day)

##### Sign Up Team - [Insert Member Here], [Insert Member Here]

* Number of Days to Develop: 3
* Number of Days to Test: 2 

###### Sub-tasks


* 1) Build out routes to handle sign up (2 Days)
* 2) Create front-end form for the sign up process (2 Days)
* 3) Test sign up process (1 Day)


##### Sign In Team - [Insert Member Here], [Insert Member Here]

* Number of Days to Develop: 7
* Number of Days to Test: 2

###### Sub-tasks

* 1) Create list of privileges that signed in user will have (1 Day)
* 2) Build out basic home screen for a signed in user to see (3 Days)
* 3) Build out routes to handle sign in process (1 Day)
* 4) Create front-end form for the sign in process (1 Day)
* 5) Test sign up process (1 Day)
* 6) Add checks for home screen that a user is authenticated (2 Days)

Note: Tasks 4, 5, and 6 are dependent on the sign up team finishing their tasks. Since that will be how we can create a user to test the sign in process. We have prioritized them last in the list so that we can wait on this dependency to clear by having this team work on something else. When that team is done, the Sign Up Team will come help the Sign In Team finish up the sign in process.

##### Club Team - [Insert Member Here], [Insert Member Here]

* Number of Days to Develop: 5
* Number of Days to Test: 2

###### Sub-tasks

* 1) Build out routes to handle adding a club (2 Days)
* 2) Create front-end form for user to add club (2 Days)
* 3) Create front-end view that will act as a directory for the club (3 Days)

## Testing Plan


