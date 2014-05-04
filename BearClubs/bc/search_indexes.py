from haystack import indexes

from BearClubs.bc.models import user, event, organization

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='username')
    email = indexes.CharField(model_attr='email')
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    calNetID = indexes.IntegerField(model_attr='calNetID', null=True)

    # We add this for autocomplete.
    name_auto = indexes.EdgeNgramField(model_attr='username')

    def get_model(self):
        return user.User

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    organization = indexes.CharField(model_attr='organization')

    name_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return event.Event

class OrganizationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    location = indexes.CharField(model_attr='location')

    name_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return organization.Organization