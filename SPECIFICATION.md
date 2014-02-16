BearClubs
Requirements and Specification Document
*02/14/2014, version 0.1*

# BearClubs

A tool for connecting students and organizations at UC Berkeley.

## Project Abstract

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
| Acceptance Tests: | Assure that only proper credentials (username, password) allow for sign in |
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
| Name/Requirement: | Tutorial                                                                       |
| Actors:           | General User                                                                   |
| Triggers:         | Sign In // Complete Sign Up                                                    |
| Precondition:     | User is Signed In for the first time                                           |
| Actions:          | Present Tutorial (Image Overlay(?), Video(?)                                   |
| Postconditions:   | Tutorial is dismissed // Revert back to normal logged-in general user behavior |
| Acceptance Tests: | Assure that "Tutorial" only occurs on user's first login                       |
| Iteration:        | 1                                                                              |

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


### User Stories For Future Iterations:

* Sign In With CalNet
* Edit Profile
* Join Club
* Subscribe To Club
* Edit Club Page (Admin)
* Post Club Event (Admin)

## User Interface Requirements

