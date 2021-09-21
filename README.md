# Python Jira API : From JSON to Issue
> I've made this project to manipulate Jira issues with JSON templates.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)
* [License](#license)


## General Information
### What problem this project intend to solve  ? 
The problem with Jira usage is that is to static. Configure issues with the web interface is boring.
Especially when you have a lot a of issues to treat with.

A lack of project about Jira automatization and they didn't corresponds to my usage (too simple, overkill,...).
Also, I haven't seen any project about Jira automatisation which used JSON to manipulate issue.

### What is the purpose of this project ? 
My project intends to automatize Jira issues manipulation with JSON templates.
I wanted to implement the most useful features and made it simplest as possible.

### Why did I undertake it ? 
For my IT school project, I had to do a CMDB for a DRP (Disastery Recovery Protocol) and I choose to use Jira.
So, I had to automatize the creation/modification/deletion of issues. 

## Technologies Used
- Python - Version 3.8
- Library : Jira

## Features
- Create / Modify / Delete Issue
- Transition an issue
- Send an attachment to an issue

## Setup
You need to install Jira library : 

`pip install jira`

You need to setup script variables to allow it to connect to your JIRA Project.
Edit these line in `script.py with JIRA Project Information/Credentials: 

    JIRA_URL = "https://myDomain.atlassian.net/"
    JIRA_MAIL = "toto@mail.com"
    JIRA_API_TOKEN = "JIRA_API_TOKEN"
    JIRA_PROJECT_NAME = "PROJECT_NAME"

You can also edit these others variable but it's not necessary : 

    JIRA_JSON_PATH = "demo.json"
    action = "CREATE"
    issue_name = "myNewIssue"

Also, my script depends on the 'summary' field in JIRA, so your issues need to have this field.
   
## Usage
Create an issue : 
`python3 script.py --action CREATE --file myDemo.json`

Edit an issue : 
`python3 script.py --action UPDATE --file myDemo.json`

Delete an issue : 
`python3 script.py --action CREATE --name myIssueName`

Do a transition for my issue : 
`python3 script.py --action UPDATE --file myDemo.json --transition myTransition`

Send an attachment to an issue: 
`python3 script.py --action UPDATE --file myDemo.json --attachment myAttachment`


## Project Status
Project is: _complete_.

## Contact
Created by [@vlaujacky](https://github.com/vlaujacky) - feel free to contact me!

## License
This project is open source and available under the [Apache License, Version 2.0](./LICENSE).
