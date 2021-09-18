from jira import JIRA


class Jira(JIRA):

    def __init__(self,server_url,username,api_token):
        jira_options = {'server': server_url}
        super(Jira,self).__init__(options=jira_options,basic_auth=(username, api_token))

    def search_issue_summary(self, project_name, summary_name):
        list_issue = []
        for singleIssue in super(Jira,self).search_issues(jql_str='project = ' + project_name + ' AND summary ~ ' + summary_name):
            list_issue.append(singleIssue.key)
        return list_issue

    # Check if the issue is created (search with the 'summary' value)
    def is_created(self, project_name, issue_name):
        list_issue = self.search_issue_summary(project_name, issue_name)
        if len(list_issue) == 1:
            print('Issue is existing, possible command : UPDATE, DELETE for issue ', list_issue)
            return list_issue[0]
        elif not list_issue:
            print('No issue existing, possible command : CREATE')
            return list_issue
        else:
            print('[ WARNING ] : SIMILAR ISSUE SUMMARY')
            print(list_issue)
            return exit(1)

    def create_issue(self, issue_dict):
        issue_key = super(Jira,self).create_issue(issue_dict)
        return issue_key

    def delete_issue(self, issue_key):
        issue = super(Jira, self).issue(issue_key)
        issue.delete()

    def update_issue(self, issue_key, issue_dict):
        issue = super(Jira, self).issue(issue_key)
        issue.update(issue_dict)

    def get_fields(self):
        allfields = super(Jira, self).fields()
        nameMap = {field['name']: field['id'] for field in allfields}
        return nameMap

    def replace_keys(self, json_to_dict):
        new_key = []
        for i in json_to_dict:
            new_key.append(self.get_fields()[i])
        new_dict = dict(zip(new_key, json_to_dict.values()))
        return new_dict

