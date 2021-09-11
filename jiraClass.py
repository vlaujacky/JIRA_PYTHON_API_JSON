from jira import JIRA


class Jira(JIRA):

    def __init__(self,server_url,username,api_token):
        jira_options = {'server': server_url}
        super(Jira,self).__init__(options=jira_options,basic_auth=(username, api_token))

    def create_issue(self, issue_dict):
        super(Jira,self).create_issue(issue_dict)

    def delete_issue(self, issue_key):
        issue = super(Jira, self).issue(issue_key)
        issue.delete()

    def update_issue(self, issue_key, issue_dict):
        issue = super(Jira, self).issue(issue_key)
        issue.update(issue_dict)

    def search_issue_summary(self, project_name, summary_name):
        list_machine = []
        for singleIssue in super(Jira,self).search_issues(
                jql_str='project = ' + project_name + ' AND summary ~ ' + summary_name):
            list_machine.append(singleIssue.key)
        return list_machine

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
