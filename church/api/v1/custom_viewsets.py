from rest_framework import mixins, viewsets

class ListRetrieveUpdateViewSets(mixins.ListModelMixin, mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet): pass