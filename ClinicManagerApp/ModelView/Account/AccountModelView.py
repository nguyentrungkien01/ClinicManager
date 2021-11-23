from flask_admin.contrib.sqla import ModelView


class AccountModelView(ModelView):
    column_hide_backrefs = False


