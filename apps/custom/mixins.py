from django.conf import settings

class TitleMixin(object):

    page_title = "Title Not Set"

    def title(self):
        return self.page_title

    def project_name(self):
        return settings.PROJECT_NAME
