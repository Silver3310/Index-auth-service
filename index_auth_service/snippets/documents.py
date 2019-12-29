from django.conf import settings

from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl.indices import Index

from django_elasticsearch_dsl.fields import TextField
from django_elasticsearch_dsl.fields import Completion
from django_elasticsearch_dsl.fields import IntegerField
from django_elasticsearch_dsl.fields import ObjectField

from .models import Snippet

snippets = Index('snippets')


@snippets.doc_type
class SnippetDocument(DocType):
    """
    Document for the Snippet model for elasticsearch with fields to index
    """
    desc = TextField(
        attr='desc',
        fields={
            'suggest': Completion(),
        }
    )
    user = ObjectField(
        properties={
            'username': TextField(),
            'id': IntegerField(),
        }
    )

    class Django:
        model = Snippet
        fields = [
            'id',
            'is_visible'
        ]

        related_models = [settings.AUTH_USER_MODEL]

    def get_queryset(self):
        return super().get_queryset().select_related(
            'user'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, settings.AUTH_USER_MODEL):
            return related_instance.snippet_set.all()
