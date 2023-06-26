from import_export import resources

from question.models import Choice, Fill, Judge, Subjective


class ChoiceResource(resources.ModelResource):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D', 'right_answer', 'analysis', 'score', 'level')


class FillResource(resources.ModelResource):
    class Meta:
        model = Fill
        fields = ('id', 'question', 'right_answer', 'analysis', 'score', 'level')


class JudgeResource(resources.ModelResource):
    class Meta:
        model = Judge
        fields = ('id', 'question', 'right_answer', 'analysis', 'score', 'level')


class SubjectiveResource(resources.ModelResource):
    class Meta:
        model = Subjective
        fields = ('id', 'question', 'answer_template', 'test_case', 'analysis', 'score', 'level')