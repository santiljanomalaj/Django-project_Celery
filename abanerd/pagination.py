from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from rest_framework.response import Response
from django.db.models import Min, Max

from abanerd.models import CEUCredit

class ResultsSetPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class ResultsSetPaginationCEUCredit(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_max_min(self):
        return CEUCredit.objects.aggregate(min_price=Min('price'), max_price=Max('price'))

    def get_paginated_response(self, data):
        values = self.get_max_min()
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages, 'min_price': values.get('min_price'),
            'max_price': values.get('max_price'),
            'results': data
        })
