from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


class CustomPageNumberPagination(PageNumberPagination):
    PAGE_SIZE = 9

    def get_paginated_response(self, data):
        return OrderedDict(
            [
                ("count", self.page.paginator.count),
                ("next", self.get_next_link()),
                ("previous", self.get_previous_link()),
                ("results", data),
            ]
        )
