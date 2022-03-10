# Qa March Project

## Introduction
This repository contains my QA Dev Fundamentals Project. The purpose of this ReadMe is to outline how I met the key deliverables of the assigned project with supporting documentation. 

## Contents

1. [Project Brief](#Project-Brief)
2. [App Design](#App-Design)
3. [CI Pipeline](#CI-Pipeline)
4. [Risk Assessment](#Risk-Assessment)
5. [Testing](#Testing)
6. [The App - House of Plants](#The-App-House-of-Plants)
7. [Known Issues](#Known-Issues)
8. [Future Work](#Future-Work)


## Project Brief

The purpose of this project was to demonstrate my abilities in the following areas: 

* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

The overall objective was to create an application which could create, read, update and delete data (CRUD) using the knowledge that had been learnt over the past 4 weeks. The application was to be written in Python using the Flask micro-framework and had to contain a relational database with at least 2 tables of data related to each other. 

The design element of the project describing the architecture had to be documented alongside a detailed risk assessment. The project had to be tracked using a Trello board or equivalent, recording any issues that arose and it was advised that the MVP concept be considered. Test suites for all the functionality had to be created with the requirement for a high test coverage, automated testing and documentation of tests.  

The code had to be integrated via a Version Control System using the Feature Branch model then built via a CI server and deployed to a cloud-based virtual machine.

## App Design

As a recent collector of plants, I chose to design a plant database for my house with two key data tables - a table to record the different rooms in my house, and a table to record the plants that I have and their characteristics, watering requirements and whether they flower or not. The relationship between the plant and room table was one to many - a room may have many plants, but a plant can only have one room. 

This relationship would allow me to ensure that I could keep an accurate record of what plants were kept in each room of my house. The relationship is demonstrated in the below table.

![ERD diagram](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Current%20ERD.png)

The functionality of the MVP was as follows: 

**CREATE**: 
- create a new plant
- create a new room

**READ**:
- view all the plants in ID order

**UPDATE**:
- update a plant's description, features or room

**DELETE**: 
- delete a plant from the database

Building upon the MVP, additional functionality was added to allow me to search for a keyword and view all the plants in room order (READ).

Moving forwards, the goal would be to improve the application as below: 

- add user profiles and a login page so that the application can be used by other users
- add additional features to the room table to record the light in the room and the direction it faces
- add an additional table to record propagated plants (plants grown from cuttings of plants) which would have a one to many relationship with both the plant and room tables i.e. one plant can produce many propagated plants and one room can have many propagated plants, but a propagated plant can only have one room and one plant

This is illustrated by the ERD diagram below: 

![Future ERD Diagram](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Future%20ERD.png)

## CI Pipeline

The key requirements of a CI pipeline are:

- Clear and tracked project requirements - usually using software specifically designed for this
- A version control system that maintains a single source code repository for the project
- Automated building of the application
- Automated testing with error reports generated
- Successful builds stored in an artefacts repository
- Automated deployment of the code

**Tracking**

I chose to use Jira software to plan and track this project because I was familiar with it and it allowed me to work in a KanBan style within sprints. 
To plan my project, I divided it into three sections:

- user stories i.e. what I wanted my users to be able to do and why
- website design i.e. how could these user stories be best faciliated
- what testing was required to ensure that the user stories worked

For each section, I wrote down the tasks that were required to fulfil each requirement. I also categorised my user stories into MVP and enhancements so that I could be clear about what needed to be done to ensure that the MVP was created first (basic MoSCow prioritisation). Usually at this stage in order to ensure work is divided evenly, story points would be assigned to each task. In this case however, as it was only myself doing all the tasks, I decided story points were not necessary. 

All the tasks were then put in a backlog to be assigned into sprints. I created 4 sprints with clear timelines and goals and within each sprint, the tasks were set out on a kanban board. The progress and status of the tasks were updated as the tasks were completed and any issues were recorded as comments.

My project can be found [here.](https://numphries.atlassian.net/jira/software/projects/BP/boards/5)

![Project Roadmap](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Project%20Roadmap.png)

![Example Sprint Layout](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Example%20Sprint.png)

**Version Control System**

I used git as my VCS and stored my source code in a repository on GitHub. I built specific features on feature branches which were deleted after they were pushed to the dev branch, which was set as the default branch so that nothing was pushed to main accidentally. The main branch was updated periodically during the project and also when the application was finalised and finished. Below is a snapshot of the network graph of the repository. A webhook was also set up to Jenkins (the build/test server) so that tests were automatically run after each commit to the repository. 

![Network Graph](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Network%20Graph.png)

**Building Environment**

The application was built using Flask and written in Python. A venv environment was created which meant that any programs installed were kept separate from other applications and the application environment was contained. The application was built on a virtual machine from Google Cloud Platform running Ubunto Pro 20.04. 

**Automated Build and Testing**

Jenkins was used for the automation of the build and testing. A freestyle project was set up, with test scripts saved into an sh file on the repository which were ran every time a commit was pushed to the repository. Artefact reports were generated after each build and if the build was successful, Jenkins automatically deployed the application using Gunicorn.

Below shows the commands that Jenkins executed and the confirmation of a successful build and deployment.

![Jenkins](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/502e41ce211ff7fe9598b4ad85e312e27b23aa85/Jenkins%20Execute%20Shell.png)

![Jenkins success](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/502e41ce211ff7fe9598b4ad85e312e27b23aa85/Successful%20deployment.png)


## Risk Assessment

Before the project was started, a risk assessment was undertaken to identify any risks or blockers to the project and how they could be mitigated. The risk assessment was split into four key sections: security risks, data risks, code risks and reliability risks. Any potential risks were then categorised and given a score based on their likelihood and what impact they would have on the project if they occurred. Measures to then control or mitigate these risks were recorded and the likelihood and impact were rescored. These measures and controls were then integrated into the planning of the project. The risk assessment and scoring matrix are below.

![Risk Assessment](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Risk%20Assessment.png)

## Testing

Thorough testing is integral to the success of the application. For this project, unit testing was used. Unit testing is where a test for each part of the app's functionality is created, to ensure that the application is working as expected.

Integration testing via Selenium was not used in this instance as there was not enough time to properly learn the process and the code required, however it is a goal for future projects. Security testing at this stage was not required as there is no log-in page or confidential user data used in the application.  

Tests were created for each area of functionality, testing both the GET and POST methods if required, which were automatically run through Jenkins. This provided 100% testing coverage as can be seen below.

![Test Screenshot](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/53dfabf74e90bad773ed7e2d772200e8ff571307/Tests%202.png)

![Test Coverage Report](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/53dfabf74e90bad773ed7e2d772200e8ff571307/Test%20Coverage%20Report.png)

## The App - The House of Plants

The homepage presents a number of options to the user.

![Homepage](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/HomePage.png)

The user can:
* Add a plant
* Add a room
* View all plants
* View all rooms
* Update/delete plants
* Search

When adding a plant, the user completes the information about the plant and can view a dropdown list of the rooms that have already been set up. Once the plant has been added successfully, the user is invited to add another plant or return to the homepage. When adding a room, the user is invited to add another room or return to the homepage. A validation error will show if the user tries to add a room that already exists in the database. 

![Add plant screenshot](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Add%20a%20new%20plant.png)

View all plants allows the user to see all the plants that have been input into the database ordered by their plant id number, along with the associated information and their room location.

![view all plants](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/View%20All%20Plants.png)

View all rooms shows the rooms and the plants that are within them.

![view all rooms](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/View%20Rooms.png)

Update/delete plants shows a list of all the plants currently in the database with links beside them to either update or delete them.

![update plants](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Update%20plants.png)

Search allows the user to input a keyword and the results will then show.

![search screenshot](https://github.com/NatalieHumphriesGitHub/qa-march-project/blob/3ec97a59743bcd67b7f8d75a5f98936dbf4195bd/Search%20results.png)

## Known Issues:

The search functionality does not have a message that shows if the keyword is not found in the database, the results field is just blank. The results also show as tuples in brackets which doesn't look very professional. 

The rooms cannot be updated or deleted. This was based on the idea that the rooms most likely will not disappear from a house, but there is a use case where rooms are repurposed or created with a spelling mistake and so this functionality would be useful in the future. 

The sentence structure for showing the plant's location says - "located in the {room}" This works for rooms such as kitchen, or living room, but the grammar is poor for rooms named as bedroom 1 or bathroom 2.

## Future Work:

As discussed above, future work would be to fix all known issues, add additional information about the rooms and add a propagated plants table. The html could also be improved as I would like to add pictures of the plants and have a more user-friendly and modern interface. 

