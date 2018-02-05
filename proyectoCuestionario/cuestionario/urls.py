from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import (
    AnswerList,
    AnswerUpdate,
    QuestionaryList,
    QuestionaryCreate,
    QuestionaryUpdate,
    QuestionaryListFilter,
    QuestionsCopy
)

urlpatterns = [
    url(
        r'^cuestionario/$',
        view=QuestionaryList.as_view(),
        name='cuestionario-list'
    ),
    url(
        r'^cuestionario_filter/$',
        view=QuestionaryListFilter.as_view(),
        name='cuestionario-list-filter'
    ),
    url(
        r'^cuestionario/create/$',
        view=QuestionaryCreate.as_view(),
        name='cuestionario-create'
    ),
    url(
        r'^cuestionario/(?P<pk>[^\/]+)/$',
        view=QuestionaryUpdate.as_view(),
        name='cuestionario'
    ),
    url(
        r'^question/(?P<pk>[^\/]+)/$',
        view=QuestionsCopy.as_view(),
        name='question'
    ),
    url(
        r'^answer/$',
        view=AnswerList.as_view(),
        name='answer-list'
    ),
    url(
        r'^answer/(?P<pk>[^\/]+)/$',
        view=AnswerUpdate.as_view(),
        name='answer'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
