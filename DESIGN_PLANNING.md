BearClubs  
Design and Planning Document  
*03/21/2014, version 2.0*  

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## Changelog *v2.0*
* Bump date and revision
* Removed iteration 1 user stories from implementation plan; left summary for browsing purposes
* Add iteration 2 user stories and tasks to implementation plan
* Assign new teams for iteration 2
* Fixed various typos

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

The following sections in Design Details are under active development; they will be subject to change during the first two iterations while we dial in our datastructures, etc.

### Frontend App Details

On the frontend, BearClubs will primarily be a web-based application. We decided to forgo mobile platforms for now since we foresee the majority of our users to access the application from a desktop/laptop. Our app is for users to discover and connect with new clubs and administrators to manage their club presence on our platform, and a "mobile" aspect does not seem to add much value. The experience seems to be best served on traditional browser interfaces for now. Perhaps once our platform is fully built out with a healthy user base, then we may consider adding on a mobile interface.

Our frontend code will primarily be HTML5/CSS/JavaScript, and we plan to test and support the latest stable versions of major browsers, including Chrome, Firefox, Safari, and Internet Explorer. Our Javascript will make extensive use of jQuery libraries and plugins, and will be concatenated and minified together for the fastest server response times possible. Our CSS will be written in LESS, compiled by `grunt-less`, and minified. The LESS source directory structure supports multiple themes, which we will implement if requested by users. We will follow the traditional Django design pattern of templating, implemented in fragments of HTML5 and passing Python objects/variables from views to templates for rendering.

### Backend Server Details

Our backend will be written in Django. The server will process incoming requests and manage access to the global database, as well as build and serve pages and manage password encryption and authentication. There are many Django packages that can help us manage these tasks. Since our application is targeted for UC Berkeley students, we are also considering running our user registration and authentication system through CalNet in a later iteration.

### Database Details

We will be using SQLite for local development, and PostgreSQL on production. We chose local SQLite for speed of development and ease of use, and production PostgreSQL for scale and performance. Our database will store users and their related profile information, organizations and their related profile information, events and their relevant information, as well as provide mappings between these three main models:  

Users: username, email, first name, last name  
Organization: name, description, location, contact info, type  
Event: name, description, start time, end time, location  

We will also have mapping / relational tables to link our users to organizations and events to organizations; a rudimentary diagram is shown below, and will be updated with future iterations.

##### Data Tables

*All tables have a `UNIQUE PRIMARY KEY` field of type integer with name `id`*

###### USER

| Field             | Description                            |
| ----------------- |:---------------------------------------|
| username          | required unique char(128)              |
| email             | required unique char(128)              |
| first\_name       | required char(128)                     |
| last\_name        | required char(128)                     |

###### ORGANIZATION

| Field             | Description                       |
| ----------------- |:----------------------------------|
| name              | required char(128)                |
| description       | required textblob                 |
| location          | char(128)                         |
| location_lat      | double                            |
| location_long     | double                            |
| contact\_info     | char(128)                         |
| type              | required foreign key org_type(id) |

###### ORGANIZATION_TYPE

| Field             | Description                       |
| ----------------- |:----------------------------------|
| name              | required char(128)                |
| description       | required textblob                 |

###### EVENT

| Field             | Description                           |
| ----------------- |:--------------------------------------|
| name              | required char(128)                    |
| description       | required blob                         |
| start\_time       | required datetime                     |
| end\_time         | required datetime                     |
| location          | char(128)                             |
| location_lat      | double                                |
| location_long     | double                                |
| org\_id           | required foreign key organization(id) |

##### Mappings / Relations

###### User to Organization

| Field                | Description                            |
| -------------------- |:---------------------------------------|
| fk\_user\_id         | required foreign key user(id)          |
| fk\_organization\_id | required foreign key organization(id)  |
| admin                | required bool                          |
| position             | char(128)                              |


#### Invariants

* User
    * Must have valid username.
    * Must have valid email.
    * Must have valid first name and last name.
    * Must be associated with zero or more organizations (user to organization mapping).
* Organization
    * Must be associated with at least one admin member.
    * Must be associated with at least one member.
    * Must have valid name.
    * Must have valid contact info.
* Event
    * Must have valid name.
    * Must have start time and end time (start time must be before end time).
    * Must be associated with exactly one club.

#### Algorithms

For iteration 1, our algorithms are trivial. In future iterations, algorithms that will be of significance are not limited to the following:

* Calendar to User mapping algorithm
* Algorithms that concern live-updating members of club updates
* Authentication and permissions algorithms concerning admins/officers of clubs
* Complex search algorithms
    * Distinguishing between users, clubs, events, etc.
    * Live-updating results on keypresses
    * Caching of data (Redis, SOLR, etc.)

#### Protocols

Since we're implementing our backend and frontend through a single Django/HTML5 application, our protocols are trivial. We have no plans of exposing a REST API to distribute our data unless persued later on (for mobile app purposes, programmatic administration of organizations, etc.). Our backend and frontend will communicate via standard HTTP methods (`GET`, `POST`, `PUT`, etc.) through Django's framework of HTTP communication.

#### View/Template Details

Views in Django are similar to how controllers function in a traditional MVC design pattern. Our views will act as the glue between our models and templates; passing data objects to our templates for rendering, accepting `POST` data for processing, and so on.

In iteration 1, we'll be solidifying our overall UI style guide, but common themes will persist through the application:

* Main layout
    * Header across the top of all pages of the application
        * Navigation links (left floating)
            * BearClubs (home)
            * Clubs (clubs directory)
            * Discover (directory search page)
        * User links (right floating)
            * My Profile (user memberships, settings, etc.)
            * My Calendar (upcoming events, subscribed events)
            * My Clubs (list of user's clubs)
    * User Sidebar (floating left, entire height of content area)
        * Profile picture
        * Username
        * Full name
        * Small version of calendar (upcoming week of events)
    * Content area
        * Main content will be rendered here (yield to other views)
* Sign up / Sign in layout
    * Header (same as main layout)
    * No Sidebar (user isn't signed in / registered yet)
    * Content area
        * Centered form / modal dialog
            * Register (left half of div)
                * Username field
                * Email field
                * Confirm email field
                * Password field
                * Confirm password field
                * Register button
            * Sign in (right half of div)
                * Username or Email field
                * Password field
                * Sign In button
                * Forgot username / password button
* Club Directory
    * Header (same as main layout)
    * Sidebar (same as main layout)
    * Content area
        * Sub-header (across top of content area)
            * Live updating search bar
            * Filter options (items per page, A-Z search, etc.)
        * Directory view
            * Live updating list of organizations
            * Table view
                * Each row clickable; directs to club's profile
* Club Profile
    * Header (same as main layout)
    * Sidebar (same as main layout)
    * Content area
        * Sub-header (across top of content area)
            * Cover photo
            * Name of organization
            * Next meeting
        * Profile information
            * Sidebar (right floating)
                * Subscribe button (get notified of updates / add events to calendar)
                * Officer information
                * Contact information
                * Location (offices)
                * Upcoming events
            * Main content
                * News feed of updates, events, etc.

#### Class Descriptions

Iteration 1 only describes two major class implementations initially; `User` and `Organization`

* User :: User model for interacting with user objects
    * Accessor methods; `getUserID()`, `getUsername()`, `getClubs()`, etc.
    * Authentication methods; `loginUser(id, pass\_hash)`, `getAdminRights()`, etc.
    * More complex methods like getClubs() will interact with mappings (user-club-mapping, etc.)
* Organization :: Model implementation for organization objects
    * Accessor methods; `getUsers(admin_level)`, `getAdmins()`, `getOfficers()`, `getOrgName()`, etc.
    * Authentication methods; `getUserAuthLevel(user_id)`, `grantUserAdmin(user_id`, etc.
    * Authentication methods will be limited to entities with admin rights for each organization to prevent members from promoting themselves, demoting others, and other sensitive operations (future iterations)

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

In terms of dependencies, we believe that we've already mitigated most of the possible dependencies. Our group has created mockups for each model, and we have hashed out and finalized how the backend will work. After doing this, we believe that implementing our first iteration through our proposed implementation plan will be straightforward since there will be minimal conflict. We do acknowledge that a potential risk would be that the front-end views will conflict across the 3 teams. To mitigate this, we believe that unifying the front-ends at the end of implementaiton will be easiest. Coupling this with a common naming convention across the team will help unify our front-ends to be one theme.

### Iteration 2

For Iteration 2, we want to implement basic functionality concerning User Profile pages, User Dashboard, Club and Event Profiles as well as interacting with these entities and searching.
* View Club Page
* Join Club
* View User Dashboard
* View User Profile
* Add Club Event
* Edit Club Event
* Search

The four user stories involving clubs (View Club Page, Join Club, Add Club Event, Edit Club Event) all have dependencies on each other because we want to keep an unified front-end and make sure that they are implemented under the assumptions of a standard organization and event model. The two user stories involving users (View User Dashboard, View User Profile) also have dependencies on each other because want to keep an unified front-end. Search will have dependencies on the finalized models. If a team feels as if a model must change for implemenation sake, the search team must be notified.

##### Entire BearClubs Team Tasks (These will happen before the start of tasks by any team)

##### Club Team - Tiffany, Shubham

* Number of Days to Develop: 8
* Number of Days to Test: 2

###### Sub-tasks

* 1) Build out routes to handle viewing and joining a club (1 Day)
* 2) Create front-end for viewing club profiles; coherant layout and display of information (2 Days)
* 3) Create front-end functionality for joining a club (1 Day)
* 4) Implement back-end interactions for interacting with club models (joining, etc.) (3 Days)
* 5) Build out routes to handle viewing existing members and promoting them to admins (1 Day)

##### User Team - Patrick

* Number of Days to Develop: 8
* Number of Days to Test: 2

###### Sub-tasks

* 1) Build out routes to handle user dashboard and profile endpoints (1 Day)
* 2) Create front-end for viewing subscribed entities (club updates, events, etc.) (2 Days)
* 3) Create back-end for pub/sub model of following subscribed entities (3 Days)
* 4) Implement in-links on other views that allow for access to the dashboard and profile pages (1 Day)
* 5) Create back-end for user-admin-club relationship table (1 Day)

##### Event Team - Alex, Kevin

* Number of Days to Develop: 7
* Number of Days to Test: 2

###### Sub-tasks

* 1) Build out routes to handle adding and editing an event (1 Day)
* 2) Create front-end for viewing club profiles; coherant layout and display of information (2 Days)
* 3) Create front-end functionality for joining a club (1 Day)
* 4) Implement back-end processes for interacting with club models (joining, etc.) (3 Days)

##### Search Team - Peter

* Number of Days to Develop: 5
* Number of Days to Test: 2

##### Sub-tasks

* 1) Create search front-end (nav-bar, results page, etc.) (2 Days)
* 2) Implement search back-end with caching technologies (SOLR, Redis, etc.) (3 Days)

### Iteration 3

For Iteration 3, we want to further expand on what we accomplished in Iteration 2. We want to elaborate on the basic functionality provided in the User Profile, Club, and Event pages. In addition, we want to begin revamping the BearClubs' UI and begin consolidating and unifying the views to a uniform design and feel.

#### Entire Bear Clubs Team Tasks (These will happen before the start of tasks by any team)

#### Club Team - [Insert name], [Insert name]

* Number of Days to Develop: 4
* Number of Days to Test: 2

###### Sub-tasks

* 1) Allow club creator to register as club admin through front end functionality (2 days)
* 2) Add front end UI functionality to allow admins to promote existing club members to admin (2 days)



#### User Team - [Insert name], [Insert name]

* Number of Days to Develop:
* Number of Days to Test:

###### Sub-tasks

* 1)  Implement frontend functionality to allow signed in Users to subscribe to a club. ()
* 2)  Implement back-end functionality to allow subscribed users to see club events. ()

#### Event Team - [Insert name], [Insert name]

* Number of Days to Develop:
* Number of Days to Test:

###### Sub-tasks

* 1) Implement view for User to view details on a specific Event listed on the event directory page. ()
* 2) Provide front-end functionality to allow the club admin to add an event. ()

#### UI Team - [Insert name], [Insert Name]

## Testing Plan

### Unit and End-to-End Testing Strategies

BearClubs will utilize two testing paradigms; unit testing and end-to-end (E2E) testing. Since we're only implementing a single backend and frontend (Django and HTML5 respectively) with no need for a REST API, our functional and UI testing will be encompassed in the same paradigm of E2E.

#### Unit Testing

Our unit testing will focus on the Model and View (Django equivalent of a Controller) aspects of the Model-Template-View design pattern. We plan on making our models have much 'heavier' implementations than our views, so unit testing both of these aspects separately will be crucial. Our unit tests will be contained hierarchically in the `BearClubs/tests` directory, and will implement the standard Django unit testing that is provided with the framework.

#### End-to-End Testing

End-to-end tests will highlight the functionality of the web application as a whole, focusing heavily on the HTML5/Javascript front-end we're implementing. These E2E tests will be implemented with the `django-webtest` package. Using this package, we're able to run our E2E tests much like our unit tests. The `django-webtest` package subclasses Django's test case (`django.test.TestCase`), allowing us to write unit and functional tests that are similarly coherent and consistent.

### Automated testing

Automated testing is a critical aspect of our testing approach. We're using two tools to automate our tests; [GruntJS](http://gruntjs.com/) and [Travis CI](https://travis-ci.org/pkillian/BearClubs). 

#### GruntJS

GruntJS allows us to "watch" files in our working directory, and launch the appropriate tests without any hesitation. For example, if a change is made to a model, GruntJS can be configured to launch the proper unit tests that exist in `tests/unit/models`. Likewise for a change made to a template file; GruntJS can automatically launch a series of E2E tests on the fly, continuously.

GruntJS is also being used to minify and deploy JS/LESS/CSS files, but its focus in our testing strategy is that of the "watch" functionality.

#### Travis CI

Travis CI is a free continuous integration environment, similar to that of Jenkins, but without any of the overhead involved. Travis CI is being used to monitor certain branches (`master` and `testing`), and run our entire suite of unit tests on these branches whenever commits are pushed to our GitHub repository. When a new commit is pushed onto `origin/master` or `origin/testing`, Travis CI checks out that revision, and launches the commands we specify in our `/.travis.yml` configuration file. This is extremely useful from a continuous integration standpoint, because this ensures that every single state of the `master` and `testing` branches gets tested before being deployed to production. Our contributing pattern incorporates this; all versions of BearClubs will be pushed to `origin/testing` and have its test output analyzed extensively before ever being deployed on production.

Due to Travis CI's headless nature, it makes running our E2E tests a bit of a headache, so we've decided to only use Travis CI to run our unit tests.

