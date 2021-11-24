from flask_admin.contrib.sqla import ModelView


class BaseModelView(ModelView):
    create_modal = True
    edit_modal = True
    details_modal = True
    column_display_pk = True
