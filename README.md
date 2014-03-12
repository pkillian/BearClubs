BearClubs :: CS 169 Project Proposal
====================================
[![Gitter chat](https://badges.gitter.im/pkillian/BearClubs.png)](https://gitter.im/pkillian/BearClubs)
[![Build Status](https://travis-ci.org/pkillian/BearClubs.png?branch=master)](https://travis-ci.org/pkillian/BearClubs)

## Problem statement: 

Campus clubs / organizations are hard to browse, keep track of and discover. Different sources of information don't agree (Facebook, CalLink, etc.), and are misleading. There exists no central place for all organization updates / browsing / information, other than [CalLink](http://callink.berkeley.edu) which is clunky and outdated.


## Customers:

 - Club officers
 - Current members of organizations
 - Students curious about joining clubs


## Application functionality: 

The application should have three different focuses; one for the officers of an organization, one for current members of organizations to stay up to date with their organizations, and one for students to browse and find new organizations.

Each user of the application will have their own personal dashboard and calendar. If they're the officer of an organization, they'll have administrative options for them; if they're a member of an organization, their dashboard will have upcoming events and updates; each user can also choose to 'follow' or subscribe to certain organizations and stay up to date with their events, even if they're not a member yet (potentially finding a new organization).

The officer customer focus will allow for rapid editing of the organization's pages and information; allow for multiple tabs including but not limited to: Welcome, About, Events / Calendar, Contact, Apply, etc. The officer focus should also give officers the ability to manage membership, promote members to officer status, create new events, and a variety of other administrative tasks.

The current member customer focus will allow current members of organizations to see all events, communicate with other members, add blog / forum posts, etc.

The new member customer focus will allow students who aren't current members to search for clubs, apply for clubs, and keep up-to-date with infosessions / events. New member focus should also allow for students to select favorite potential clubs, allowing for their events / updates to populate their dashboard feed.


## Testing:

Unit tests will be implemented liberally throughout development, as will E2E (end-to-end) tests.

Three environments will be necessary: development, staging, and production. Development and staging should be identical, while production should only be different from staging in scale (3 front ends compared to 1, etc.)

After importing any information we possibly can salvage from CalLink and other various sources into a dev environment, a user-switching behavior will be implemented that allows superusers (developers) to see the application through the eyes of specific users. This will allow us to simulate data importing and practice rollouts from development to staging before possibly introducing issues into production.


## Demo:

We'd need our customers, members of an organization (TBG, CSUA, etc.), to demo our application. We can walk through the various workflows an officer can use to edit pages, etc. After the officer demo, we can have them walk a new member through the application process, and highlight how easy searching / browsing organizations is. Then, we can shift to the member's perspective, and highlight the dashboard and calendar aspects of the personal profile. 


## Justification:

There's a multitude of reasons why this application is justifiable for a team of 5-7. Given a team of 6, the work can be split in equitable ways; 2 members can tackle the personal dashboard and calendar, another 2 members can implement the officer admin pages / editable organization pages, and 1 member each can handle the databasing (tables / view organization, indexing of frequently queried columns, etc.), and the overall style / UX of the application.

Ideally, given the right amount of time, all features will be implemented. Realistically, all features won't get implemented in time, so here's a potential order of features based on priority:

### High priority:

 - Easy to browse list of all organizations
 - Easy search / filtering
 - Officer administration of pages with multiple tabs (About, Contact, Events, Apply, etc.)
 - Interactive user dashboard / calendar where favorite clubs can be "followed" or subscribed to

### Medium priority:

 - Powerful officer tools (email blasts to all members, new member chat / email lists, member administration, bookkeeping, etc.)
 - Common / Web application handled application processes (user goes to apply tab, fills out form specified by officers, submit to officer's queue for approval / processing)
 - Voting / Polls that officers can initiate and members can vote on

### Low priority:

 - Organization forum / blog posts
 - Exporting of information for calendar consumption, address books, etc.
 - Customizable HTML and templates for officers to implement custom pages


## Conclusion:

For all the prestige that Berkeley encapsulates, the task of finding organizations and joining them should be easier than it currently is. Instead of having potential new members storm Sproul Plaza during lunch hours and grab every flyer they can, there should be an up-to-date University affiliated outlet for students to utilize. That's where BearClubs sets in, and hopes to satisfy. Thanks for your consideration, and GO BEARS!
