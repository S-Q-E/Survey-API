from .apiviews import *
from django.urls import path


app_name = 'polls'
urlpatterns = [
    path('login/', login, name='login'),
    path('polls/create/', survey_create, name='survey_create'),
    path('polls/update/<int:survey_id>/', survey_update, name='survey_update'),
    path('polls/view/', survey_view, name='survey_view'),
    path('polls/update/active/', activate_survey_view, name='active_survey_view'),

    path('question/create/', question_create, name='question_create'),
    path('question/update/<int:question_id>', question_update, name='question_update'),

    path('choice/create/', choice_create, name='choice_create'),
    path('choice/update/', choice_update, name='choice_update'),
    
    path('answer/create/', answer_create, name='answer_create'),
    path('question/update/<int:asnwer_id>', answer_update, name='answer_update'),
    path('question/view', answer_view, name='answer_view')
]
