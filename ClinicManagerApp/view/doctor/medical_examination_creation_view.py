from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp.view.base_view import BaseView


class MedicalExaminationCreationView(BaseView):
    @expose('/')
    def index(self):
        return self.render('doctor/medical_examination_creation.html')
    
    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('bác sĩ')
