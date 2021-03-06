BearClubs  
Requirements and Specification Document  
*04/25/2014, version 4.0*  

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## Changelog *v4.0*
* Bump date and revision
* Add user stories for iteration 4
* Added screenshots and subheaders to UI section

## Project Abstract

BearClubs strives to be the one-stop shop for all things related to on-campus clubs, organizations, and societies. As a student looking to get involved in Berkeley's many prestigious organizations, one notices very quickly that there's a severe problem with how things are currently done. Clubs and organizations rely on email lists, spamming the chalkboards in massive lecture halls, flyers on Sproul Plaza, and a variety of other methods to distribute information and notify members of events. Those of us affiliated with BearClubs think this is unreasonable and can be done in a much more efficient manner.

CalLink is the existing solution to this problem, but it's severely lacking in functionality (as detailed below). With an approach more focused on the end-user's needs and concerns, BearClubs seeks to take the weight off the shoulders of club officers, members and those seeking new organizations to be apart of. While CalLink functions mostly as a directory with outdated information, BearClubs will keep usability as its top priority.

## Customer

Customers for this application will be all those who are interested or are involved in student organizations and clubs on campus. Specifically, there will be three types of customers: club officers, current members, and students who are interested in joining clubs.

Officers will be able to use this application as a tool to advertise their club and keep members up-to-date on all events and information. Current members will be able to keep track of multiple events across different clubs and communicate with other members. Students interested in joining clubs will be able to browse a listing of all organizations and clubs on campus, learn more about each club and their events, and apply for clubs.

We intend to contact a few clubs on campus as our specific customers who will provide feedback and suggestions as we build the application. We will also be customers involved in this process, acting as current members and those interested in joining clubs.

## Competitive Landscape

Our main competitor in the UC Berkeley market will be the existing Berkeley solution: [CalLink](http://callink.berkeley.edu). CalLink, in recent years, is and has been the only way for Berkeley students to find clubs and events to attend. However, CalLink is highly inefficient. The site is cluttered and outdated in terms of information. For instance, to join and find organizations to join, one needs to sort through 1,452 organizations with many of these being inactive. Furthermore, some of the currently active organizations don't even work with CalLink to keep their events updated. Currently, rather than use CalLink as a way to publicize events, organizations on campus are primarily focusing on Facebook, a platform that doesn't specifically focus on clubs. As students of Berkeley, we want to better engage with the Cal community, but CalLink doesn't effectively allow us to do that.

For the most part, BearClubs will keep the core idea of CalLink but make major improvements and enhancements to it. We want to provide a clean, simple UI that not only allows students to find organizations and events easily, but also allows current members to stay updated with their clubs. Some features that we are implementing to differentiate from CalLink are: individual user profiles which provide the ability for users to follow organizations they're interested in, administrative privileges for officer club members so they can better manage their club, and a club search system that incorporates the use of tags to better facilitate and simplify the discovery process for new users. In essence, BearClubs will strive to be the go-to place for students and organizations.

## User Stories

### Actors:

A single user can be any combination of the following actors:

1. General User - UC Berkeley Student; Access to basic functionality
2. Club Member - N/A for this iteration (UC Berkeley Student that is a member of an organization/club; Access to elevated privileges within scope of club by discretion of club administrator)
3. Club Officer (Administrator) - N/A for this iteration

### User Stories:

#### Iteration 1 User Stories:

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Initial Launch                                                                        |
| Actors:           | General User                                                                          |
| Triggers:         | Access BearClubs URL                                                                  |
| Precondition:     | None                                                                                  |
| Actions:          | Present Sign In//Sign Up Page                                                         |
| Postconditions:   | User now has ability to either sign in or sign up                                     |
| Acceptance Tests: | Assure that "Initial Launch" story only occurs when no user session is stored locally |
| Iteration:        | 1                                                                                     |

| Field             | Description                                                                      |
| ----------------- |:---------------------------------------------------------------------------------|
| Name/Requirement: | Signed In User Launch                                                            |
| Actors:           | General User                                                                     |
| Triggers:         | Access BearClubs URL                                                             |
| Precondition:     | User session stored locally                                                      |
| Actions:          | Present Initial Signed In Page (Profile(?), Directory of Clubs (?), Feed(?))     |
| Postconditions:   | User now has ability to navigate BearClubs with signed in privileges             |
| Acceptance Tests: | Assure that "Signed In User Launch" only occurs when user session stored locally |
| Iteration:        | 1                                                                                |

| Field             | Description                                                                  |
| ----------------- |:-----------------------------------------------------------------------------|
| Name/Requirement: | Sign In                                                                      |
| Actors:           | General User                                                                 |
| Triggers:         | Click Sign In Button                                                         |
| Precondition:     | None                                                                         |
| Actions:          | Present Initial Signed In Page (Profile(?), Directory of Clubs (?), Feed(?)) |
| Postconditions:   | User now has ability to navigate BearClubs with signed in privileges         |
| Acceptance Tests: | Assure that only proper credentials (username, password) allow for sign in   |
| Iteration:        | 1                                                                            |

| Field             | Description                                                                                     |
| ----------------- |:------------------------------------------------------------------------------------------------|
| Name/Requirement: | Sign Up                                                                                         |
| Actors:           | General User                                                                                    |
| Triggers:         | Click Sign Up Button                                                                            |
| Precondition:     | None                                                                                            |
| Actions:          | Present Sign Up Process (Add Clubs (?), Profile Information (?))                                |
| Postconditions:   | User now has an account // User now has ability to navigate BearClubs with signed in privileges |
| Acceptance Tests: | Assure that proper credentials (username, password) allow for sign up                           |
| Iteration:        | 1                                                                                               |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View Directory of Clubs                                                        |
| Actors:           | General User                                                                   |
| Triggers:         | Access Bear Clubs Club Directory URL                                           |
| Precondition:     | None                                                                           |
| Actions:          | Present Club Directory UI                                                      |
| Postconditions:   | User can now view directory of all clubs                                       |
| Acceptance Tests: | Assure that user can navigate to all clubs                                     |
| Iteration:        | 1                                                                              |

| Field             | Description                                                                             |
| ----------------- |:----------------------------------------------------------------------------------------|
| Name/Requirement: | Add Club                                                                                |
| Actors:           | General User                                                                            |
| Triggers:         | Click on Add Club from Directory of Clubs                                               |
| Precondition:     | None                                                                                    |
| Actions:          | Present Add Club dialog                                                                 |
| Postconditions:   | User can now view Club in Club Directory                                                |
| Acceptance Tests: | User can only add a club with proper input // Assure user sees new club on directory    |
| Iteration:        | 1                                                                                       |

#### Iteration 2 User Stories:

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View Club Page                                                                 |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Club in Directory View                                                |
| Precondition:     | User is looking at club directory                                              |
| Actions:          | User views specific club page with prepopulated information                    |
| Postconditions:   | User now learns more about specific club and can navigate back to directory    |
| Acceptance Tests: | Assure that club page is populated with info added when "Adding a Club"        |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                                   |
| ----------------- |:----------------------------------------------------------------------------------------------|
| Name/Requirement: | View User Dashboard                                                                           |
| Actors:           | Logged In User                                                                                |
| Triggers:         | Navigating "home" or various actions that affect user's interactions with clubs, events, etc. |
| Precondition:     | User is signed in and navigates to their subscribed feed of updates                           |
| Actions:          | Redirect user to dashboard and display user subscribed information (updates, calendar, etc.)  |
| Postconditions:   | User can interact directly with subscribed entities (read more about them, view events, etc.) |
| Acceptance Tests: | User dashboard is rendered properly no matter what is subscribed to // User can interact with subscriptions (view events, view clubs, etc.) // Subscriptions can redirect to other entities like club pages       |
| Iteration:        | 2                                                                                             |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View User Profile                                                              |
| Actors:           | Logged In User                                                                 |
| Triggers:         | Click on username from any view                                                |
| Precondition:     | User is signed in and navigates to a certain user's information                |
| Actions:          | Redirect user to profile and display user generated information                |
| Postconditions:   | User can interact directly with other user (invite, email, etc.)               |
| Acceptance Tests: | User profile is rendered properly no matter what informaton provided // User is redirected seamlessly to profile from intial view                                                               |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Add Club Event                                                                 |
| Actors:           | Creator of Club                                                                |
| Triggers:         | None                                                                           |
| Precondition:     | User clicks on add event buton                                                 |
| Actions:          | Present add event dialog                                                       |
| Postconditions:   | User can now see events under events tab                                       |
| Acceptance Tests: | User can only add a event with proper input // Assure user sees new event under events tab |
| Iteration:        | 2                                                                              | 

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Search                                                                         |
| Actors:           | General User                                                                   |
| Triggers:         | Type in search bar                                                             |
| Precondition:     | User clicks on search bar                                                      |
| Actions:          | Present drop down menu with search results                                     |
| Postconditions:   | User can see results for a search query                                        |
| Acceptance Tests: | User will see results related to search query // Assure user can't see search results they don't have pemissions for  |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Join Club                                                                      |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Join Club button on Club Page                                         |
| Precondition:     | User is signed in and not already a member of the club                         |
| Actions:          | Present form for user to fill out (?)                                          |
| Postconditions:   | User can see the club listed in their profile // User is now a member of the club and has certain member privileges/permissions                                 |
| Acceptance Tests: | User can only join if the form is filled out correctly and is approved         |
| Iteration:        | 2                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Promote Member to Admin                                                                     |
| Actors:           | Existing organization admin (default organization creator)                                                                  |
| Triggers:         | Button on club profile page                                         |
| Precondition:     | User is signed in and is an admin of the organization                         |
| Actions:          | Select members to promote; confirm button                                          |
| Postconditions:   | Member promoted is now admin                             |
| Acceptance Tests: | Members promoted has full admin priviledges (create events for now)       |
| Iteration:        | 2                                                                              |

#### Iteration 3 User Stories:

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Search Autocomplete                                                                     |
| Actors:           | General User                                                                  |
| Triggers:         | Click search button on header                                         |
| Precondition:     | N/A                         |
| Actions:          | Start typing in search field                                          |
| Postconditions:   | Relevant search results are presented to the user                             |
| Acceptance Tests: | Search results are relevant to search query       |
| Iteration:        | 3                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Add Club Creator as Admin                                                      |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Submit button of the create club page                                 |
| Precondition:     | User is signed in                                                              |
| Actions:          | Redirect to club directory(?)                                                  |
| Postconditions:   | User is now a member of the club with admin privileges // User is listed under the members section on the club page                                |
| Acceptance Tests: | The club creator has full admin priviledges                                    |
| Iteration:        | 3                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Add Event as Admin                                                    |
| Actors:           | Existing Organization Admin                                                                  |
| Triggers:         | Click on Add event button                                |
| Precondition:     | User is signed in, and is admin of club                                                            |
| Actions:          | Present add event dialog                                                  |
| Postconditions:   | User can now see events under events tab                                 |
| Acceptance Tests: | User can only add a event with proper input // Assure user sees new event under events tab                                 |
| Iteration:        | 3                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Subscribe to Club                                                 |
| Actors:           | General User                                                                 |
| Triggers:         | Click on Subscribe button                               |
| Precondition:     | User is signed in                                                           |
| Actions:          | Present subscribe club dialog                                                 |
| Postconditions:   | User is now a member of club, user can now see events of club on profile                               |
| Acceptance Tests: | User logged as member in database                         |
| Iteration:        | 3                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Manage Club Membership                                               |
| Actors:           | Existing Organization Admin                                                                |
| Triggers:         | Click on Manage button                               |
| Precondition:     | User is signed in, and is admin of club                                                           |
| Actions:          | Present manage club dialog                                                 |
| Postconditions:   | User can now promote members to admin                               |
| Acceptance Tests: | Club member has full admin privieleges                       |
| Iteration:        | 3                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | View Event Page                                                                 |
| Actors:           | General User                                                                   |
| Triggers:         | Click on Event in Event Directory View                                                |
| Precondition:     | User is looking at event directory                                              |
| Actions:          | User views specific event page with prepopulated information                    |
| Postconditions:   | User now learns more about specific event and can navigate back to directory    |
| Acceptance Tests: | Assure that Event page is populated with info added when "Adding a Event"        |
| Iteration:        | 3                                                                             |

#### Iteration 4 User Stories:

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | First Time User Tutorial                                                       |
| Actors:           | General User                                                                   |
| Triggers:         | Sign Up                                                                        |
| Precondition:     | User clicks on sign up button after filling in information                     |
| Actions:          | User exposed to new UI that explains how various components of the site works  |
| Postconditions:   | User now is educated on the UI and core concept of the site                    |
| Acceptance Tests: | Assure that the tutorial only shows up for newly signed up users               |
| Iteration:        | 4                                                                              |

| Field             | Description                                                                    |
| ----------------- |:-------------------------------------------------------------------------------|
| Name/Requirement: | Sign In / Sign Up With CalNet                                                  |
| Actors:           | General User                                                                   |
| Triggers:         | N/A                                                                            |
| Precondition:     | User clicks on sign up with CalNet button                                      |
| Actions:          | CalNet integration dialog shows                                                |
| Postconditions:   | User is now signed up to BearClubs through their CalNet ID and Password        |
| Acceptance Tests: | Assure that user is able to signup with their CalNet ID and Password           |
| Iteration:        | 4                                                                              |

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Polish User Profile Style/Format                                                      |
| Actors:           | General User                                                                          |
| Triggers:         | N/A                                                                                   |
| Precondition:     | User navigates to a user's profile page                                               |
| Actions:          | User is displayed the proper profile and relevent info in a more attractive manner    |
| Postconditions:   | N/A                                                                                   |
| Acceptance Tests: | All profile pages (User, Club, Event) have similar, coherant and attractive style     |
| Iteration:        | 4                                                                                     |

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Polish Club Profile Style/Format                                                      |
| Actors:           | General User                                                                          |
| Triggers:         | N/A                                                                                   |
| Precondition:     | User navigates to a club's profile page                                               |
| Actions:          | User is displayed the proper profile and relevent info in a more attractive manner    |
| Postconditions:   | N/A                                                                                   |
| Acceptance Tests: | All profile pages (User, Club, Event) have similar, coherant and attractive style     |
| Iteration:        | 4                                                                                     |

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Polish Event Profile Style/Format                                                     |
| Actors:           | General User                                                                          |
| Triggers:         | N/A                                                                                   |
| Precondition:     | User navigates to an event's profile page                                             |
| Actions:          | User is displayed the proper profile and relevent info in a more attractive manner    |
| Postconditions:   | N/A                                                                                   |
| Acceptance Tests: | All profile pages (User, Club, Event) have similar, coherant and attractive style     |
| Iteration:        | 4                                                                                     |

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Leave Club                                                                            |
| Actors:           | Club Member                                                                           |
| Triggers:         | Click Leave Club button                                                               |
| Precondition:     | User is a member of the club                                                          |
| Actions:          | User is removed from club member list                                                 |
| Postconditions:   | User is no longer a member of the club                                                |
| Acceptance Tests: | User is not listed as a member on the manage club page; user does not see the club listed under their profile's club membership list.     |
| Iteration:        | 4                                                                                     |

| Field             | Description                                                                           |
| ----------------- |:--------------------------------------------------------------------------------------|
| Name/Requirement: | Restrict demotions                                                                    |
| Actors:           | Admin                                                                                 |
| Triggers:         | Click demote button for the user him/herself (or show no demote button for the user)  |
| Precondition:     | User is the only admin of a club                                                      |
| Actions:          | An error message is displayed telling the user that you can't demote the last admin   |
| Postconditions:   | User is still an admin                                                                |
| Acceptance Tests: | User still has admin privileges, being able to create events, and can see the club management page |
| Iteration:        | 4                                                                                     |

### User Stories For Future Iterations:

* View your Calendar
* Edit Club Page (Admin)

## User Interface Requirements

### Screenshots after Iteration 3

#### Home Page
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.00.32%20PM.png)

#### Club and Event Directories
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.00.41%20PM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.00.51%20PM.png)

#### Search and Autocomplete
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.00.59%20PM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.01.02%20PM.png)

#### Dashboard and User Profile
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.01.22%20PM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-25%20at%201.01.26%20PM.png)

### Screenshots after Iteration 2

#### Club and Event Directories
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.47.45%20AM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.48.52%20AM.png)

#### Add Element Form Example
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.48.40%20AM.png)

#### Search Functionality
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.48.57%20AM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.50.43%20AM.png)

#### User Login Form Functionality
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.50.50%20AM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.51.07%20AM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.51.17%20AM.png)

#### User Profile and Dashboard Views
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.51.46%20AM.png)
![](https://dl.dropboxusercontent.com/u/632568/Screen%20Shot%202014-04-11%20at%2010.51.49%20AM.png)


### Initial Sketches
![UI Requirements](https://dl.dropboxusercontent.com/u/632568/CS169_proj3.png)
