from jiraClass import *
import json
import argparse


# Function : Print help/usage and take args
def argParser():
    parser = argparse.ArgumentParser(description='Script for Jira automation from JSON issue template ! \
                                    TO CREATE an JIRA issue : python3 script.py --action CREATE --file myFile.json ; \
                                    TO UPDATE an JIRA issue : python3 script.py --action UPDATE --file myFile.json ; \
                                    TO DELETE a JIRA issue : python3 script.py --action DELETE --name myIssueName ')

    parser.add_argument('--action',action='store',required=True,dest='action',
                        help='JIRA Action : CREATE, UPDATE or DELETE issue')
    parser.add_argument('--file',action='store',dest='json_file',help='Path of JIRA issue in JSON format')
    parser.add_argument('--name',action='store',dest='sum_name',
                        help='Value of the summary fields (The name of your issue)')
    parser.add_argument('--transition',action='store',dest='transition',help='Change status of an issue')
    parser.add_argument('--attachment',action='store',dest='attachment',help='Send an attachment to an issue')

    return parser.parse_args()


# Load the JSON file with new issue values and convert it to Python Dict
def load_json2dict(json_file):
    with open(json_file,"r") as f:
        return json.load(f)


if __name__ == "__main__":
    #### VARIABLES #####
    JIRA_URL = "https://myDomain.atlassian.net/"
    JIRA_MAIL = "toto@mail.com"
    JIRA_API_TOKEN = "JIRA_API_TOKEN"
    JIRA_PROJECT_NAME = "PROJECT_NAME"

    ######### DEMO / COMPLETE BY THE ARGUMENTS #####
    JIRA_JSON_PATH = "demo.json"
    action = "CREATE"
    issue_name = "myNewIssue"
    ##########

    # Connect to Jira with URL, Mail and API Token
    jira_connect = Jira(JIRA_URL,JIRA_MAIL,JIRA_API_TOKEN)

    # Get values from args gave by the user
    arguments = argParser()

    # Save the action CREATE / UPDATE /DELETE and load JSON_file if needed (CREATE / UPDATE )
    # or set the issue name ( DELETE )
    action = arguments.action
    if action == 'CREATE' or action == 'UPDATE':
        JIRA_JSON_PATH = arguments.json_file
        # Load JSON template of the issue with values
        json_to_dict = load_json2dict(JIRA_JSON_PATH)

        # Link JSON Key <-> Jira customfield_id <-> Jira Fields Name
        dict_new_keys = jira_connect.replace_keys(json_to_dict)
        issue_name = dict_new_keys['summary']

    elif action == 'DELETE':
        issue_name = arguments.sum_name

    # Check if the issue already exist, search the "summary" value in Project
    issue_key_if_created = jira_connect.is_created(JIRA_PROJECT_NAME,issue_name)

    # Check if issue exist or not, and use the action gave by the user
    if action == "CREATE" and len(issue_key_if_created) == 0:
        issue_key_if_created = jira_connect.create_issue(dict_new_keys)
        print("ISSUE WAS CREATED")

    elif action == "UPDATE" and len(issue_key_if_created) != 0:
        jira_connect.update_issue(str(issue_key_if_created),dict_new_keys)
        print("ISSUE",issue_key_if_created,"WAS UPDATED")

    elif action == "DELETE" and len(issue_key_if_created) != 0:
        jira_connect.delete_issue(issue_key_if_created)
        print("ISSUE ",issue_key_if_created,"WAS DELETED")

    else:
        print("ERROR : Bad args / Issue already created in JIRA ")

    # Optional : Make transition and change status of issue
    transition_name = arguments.transition
    if transition_name is not None:
        jira_connect.transition_issue(issue_key_if_created,transition_name)

    attachment_name = arguments.attachment
    if attachment_name is not None:
        jira_connect.add_attachment(issue_key_if_created, attachment_name)

