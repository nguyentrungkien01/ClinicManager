from flask_admin.contrib.sqla import ModelView


class BaseModelView(ModelView):
    column_hide_backrefs = False
    can_create = True
    can_edit = True
    can_delete = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_display_pk = True
    page_size = 10
    column_display_all_relations = True
    can_view_details = True
    can_export = True

    list_template = 'admin/test.html'
    # edit_template =
    # create_template =
    # details_template =