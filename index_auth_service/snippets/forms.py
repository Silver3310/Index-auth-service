from django.forms import Form

from django.forms import CharField


class SnippetSearchForm(Form):
    """
    Form for searching snippets
    """
    desc = CharField(
        label='Description',
        required=False
    )
    username = CharField(
        label='Username',
        required=False
    )

    def __init__(
        self,
        desc: str,
        username: str
    ):
        super().__init__()
        self.fields['desc'].initial = desc
        self.fields['username'].initial = username
