from flask_admin.contrib.sqla import ModelView


class BaseModelView(ModelView):
    column_hide_backrefs = False
    create_modal = True
    edit_modal = True
    details_modal = True
    column_display_pk = True
    page_size = 10
    column_display_all_relations = True
