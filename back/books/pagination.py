from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class MyPagination(PageNumberPagination):
    page_size = 8
    def get_paginated_response(self, data):
        return Response({

                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
                'current_page_num': self.page.number,
                'all_pages': self.page.paginator.num_pages,
                'results': data
        })