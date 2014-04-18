from haystack import indexes

from BearClubs.bc.models import user, event, organization

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    email = indexes.CharField(model_attr='email')
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')

    # We add this for autocomplete.
    first_name_auto = indexes.EdgeNgramField(model_attr='first_name')
    last_name_auto = indexes.EdgeNgramField(model_attr='last_name')
    username_auto = indexes.EdgeNgramField(model_attr='username')
    email_auto = indexes.EdgeNgramField(model_attr='email')

    def get_model(self):
        return user.User

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    organization = indexes.CharField(model_attr='organization')

    name_auto = indexes.EdgeNgramField(model_attr='name')
    description_auto = indexes.EdgeNgramField(model_attr='description')
    organization_auto = indexes.EdgeNgramField(model_attr='organization')

    def get_model(self):
        return event.Event

class OrganizationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    location = indexes.CharField(model_attr='location')

    name_auto = indexes.EdgeNgramField(model_attr='name')
    description_auto = indexes.EdgeNgramField(model_attr='description')
    location_auto = indexes.EdgeNgramField(model_attr='location')

    def get_model(self):
        return organization.Organization