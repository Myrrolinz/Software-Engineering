import xadmin

from question.models import Choice, Fill, Judge, Subjective
from question.resource import ChoiceResource, FillResource, JudgeResource, SubjectiveResource


class ChoiceAdmin(object):
    list_display = ['id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
                    'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_fields = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-question-circle-o'
    import_export_args = {'import_resource_class': ChoiceResource}


class FillAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-edit '
    import_export_args = {'import_resource_class': FillResource}


class JudgeAdmin(object):
    list_display = ['id', 'question', 'right_answer', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-check-square-o'
    import_export_args = {'import_resource_class': JudgeResource}


class SubjectiveAdmin(object):
    list_display = ['id', 'question', 'analysis', 'score', 'level']
    list_filter = ['level']
    search_field = ['id', 'question']
    list_display_links = ['question']
    list_per_page = 10
    # list_editable = ['question']
    model_icon = 'fa fa-laptop'
    import_export_args = {'import_resource_class': SubjectiveResource}


xadmin.site.register(Choice, ChoiceAdmin)
xadmin.site.register(Fill, FillAdmin)
xadmin.site.register(Judge, JudgeAdmin)
xadmin.site.register(Subjective, SubjectiveAdmin)
