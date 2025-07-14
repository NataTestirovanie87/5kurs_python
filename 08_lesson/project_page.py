class ProjectPage:
    def __init__(self, api):
        self.api = api

    def get_projects(self):
        return self.api.get_project_list()

    def create_project(self, title, users):
        return self.api.create_project(title=title, users=users)

    def edit_project(
            self, project_id, new_title=None, new_users=None, deleted=False):
        return self.api.edit_project(
            project_id=project_id, new_title=new_title, new_users=new_users,
            deleted=deleted)

    def search_project_by_id(self, project_id):
        return self.api.search_project_by_id(project_id)
