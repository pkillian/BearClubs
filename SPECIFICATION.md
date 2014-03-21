BearClubs  
Requirements and Specification Document  
*03/21/2014, version 2.0*  

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## Changelog *v2.0*
* Bump date and revision
* Add user stories for iteration 2
* Add more future user stories

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


### User Stories For Future Iterations:

* First time user tutorial
* Sign In With CalNet
* View your Calendar
* Edit Profile/Dashboard
* Search For Clubs
* Create New Club
* Join Club
* Subscribe To Club
* View Club Page
* Edit Club Page (Admin)
* Post Club Event (Admin)
* Edit Club Event (Admin)
* Manager Club Membership (Admin)

## User Interface Requirements

![UI Requirements](https://dl.dropboxusercontent.com/u/632568/CS169_proj3.png)
