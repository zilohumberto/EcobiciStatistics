from core.database.data import data


class Controller(object):

    model = None
    entity = None
    model_pk = 'id'

    def __init__(self):
        """Constructor.
        Sets the attribute's values using the abstract methods. These abstract
        methods are implemented by the children classes, or return default
        values.
        """
        self._model = self.model if self.model else None
        self.query = data.get(data.get(self.entity)) if self.model else None

    def get(self, **kwargs):
        return self._get_entity(**kwargs)

    def _get_entity(self, **kwargs):
        instance = self.search(**kwargs)
        if len(instance) > 0:
            raise NameError('Cannot find {entity} by {model_pk}'.format(
                entity=self.entity,
                model_pk=self.model_pk))
        return instance[0]

    def get_collection(self, **kwargs):
        return self.search(**kwargs)

    def search(self, **kwargs):
        elements = data.get(self.entity, [])
        print(len(elements))
        results = list(filter(
            lambda x:
            getattr(x, self.model_pk) ==
            kwargs.get(
                self.model_pk,
                getattr(x, self.model_pk)), elements))
        return results

