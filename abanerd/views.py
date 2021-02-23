from django.db.models import Count
import django_filters
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
<<<<<<< HEAD
from filters.mixins import (
    FiltersMixin,
)
=======

>>>>>>> initalize
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_flex_fields import FlexFieldsModelSerializer

from .models import Provider, CEUCredit, CEUImageFile, CEUSubmission, CEUMediaType, CEUCreditType, CSVFile
from .pagination import ResultsSetPagination, ResultsSetPaginationCEUCredit
from .serializers import ProviderSerializer, CEUCreditSerializer, ProviderFilterSerializer, CEUImageFileSerializer, \
    CEUMediaTypeSerializer, CEUCreditTypeSerializer, CEUCreditMaxPriceSerializer
from .tasks import upload_items


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

class ProviderCustomerFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr = 'icontains')
    url = django_filters.CharFilter(lookup_expr = 'icontains')
    slug = django_filters.CharFilter(lookup_expr = 'icontains')
    class Meta:
        fields = ('name', 'slug', 'url')
        model = Provider

<<<<<<< HEAD
class ProviderCustomFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    url = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        fields = ('name','slug','url')
        model = Provider

class ProviderViewSet(FiltersMixin,viewsets.ModelViewSet):
    """
        Adding filtermixin for pagination along with django_filter
=======
class ProviderViewSet(viewsets.ModelViewSet):
    """
        
>>>>>>> initalize
    """
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer
<<<<<<< HEAD
    filterset_class = ProviderCustomFilterSet
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
=======
    filterset_class = ProviderCustomerFilterSet
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    paginate_by =12
>>>>>>> initalize
    pagination_class = ResultsSetPagination

class CEUMediaTypeCustomFilterSet(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
<<<<<<< HEAD
        fields = ('id','name','slug')
        model = CEUMediaType
   

class CEUMediaTypeViewSet(FiltersMixin, viewsets.ModelViewSet):
    """
        Adding filtermixin for pagination along with django_filter
=======
        fields = ('id', 'name', 'slug')
        model = CEUMediaType
        
class CEUMediaTypeViewSet(viewsets.ModelViewSet):
    """
        
>>>>>>> initalize
    """
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUMediaType.objects.all().order_by('id')
    serializer_class = CEUMediaTypeSerializer
    filterset_class = CEUMediaTypeCustomFilterSet
<<<<<<< HEAD
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPagination
    
=======
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPagination

>>>>>>> initalize
class CEUCreditTypeCustomFilterSet(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
<<<<<<< HEAD
        fields = ('id','name','slug')
=======
        fields = ('id', 'name', 'slug')
>>>>>>> initalize
        model = CEUCreditType

class CEUCreditTypeViewSet(viewsets.ModelViewSet):
    """
<<<<<<< HEAD
        Adding filtermixin for pagination along with django_filter
=======
        
>>>>>>> initalize
    """
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUCreditType.objects.all().order_by('id')
    serializer_class = CEUCreditTypeSerializer
    filterset_class = CEUCreditTypeCustomFilterSet
<<<<<<< HEAD
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
=======
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
>>>>>>> initalize
    paginate_by = 12
    pagination_class = ResultsSetPagination

class CEUSubmissionCustomFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    url = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
<<<<<<< HEAD
        fields = ('title','url','slug')
=======
        fields = ('title', 'url', 'slug')
>>>>>>> initalize
        model = CEUSubmission

class CEUSubmissionViewSet(viewsets.ModelViewSet):
    """
<<<<<<< HEAD
        Adding filtermixin for pagination along with django_filter
=======
        
>>>>>>> initalize
    """
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUSubmission.objects.all().order_by('title')
    serializer_class = ProviderSerializer
    filterset_class = CEUSubmissionCustomFilterSet
<<<<<<< HEAD
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPagination
    # search_fields = ['title', 'url']
    # ordering = ['title']
    # ordering_fields = ['created']

    # filter_mappings = {
    #     'id': 'id',
    #     'title': 'title__exact',
    #     'title_contains': 'title__icontains',
    #     'url': 'url__icontains',
    #     'slug': 'slug__exact',
    #     'slug_contains': 'slug__icontains',
    # }

=======
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPagination
>>>>>>> initalize

class CEUCreditCustomFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    provider = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
<<<<<<< HEAD
        fields = ('title','description','provider')
=======
        fields = ('title', 'description', 'provider')
>>>>>>> initalize
        model = CEUCredit

class CEUCreditViewSet(viewsets.ModelViewSet):
    """

    """
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUCredit.objects.all().order_by('title')
    serializer_class = CEUCreditSerializer
    filterset_class = CEUCreditCustomFilterSet
<<<<<<< HEAD
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPagination
    # search_fields = ['title', 'description', 'provider__name']
    # ordering_fields = ['title', 'price', 'credit', 'media', 'type', 'provider__name', 'slug']
    # ordering = ['-created', 'title']

    # filter_mappings = {
    #     'id': 'id',
    #     'title': 'title__icontains',
    #     'url': 'url__icontains',
    #     'media': 'media_id__exact',
    #     'type': 'type_id__exact',
    #     'price': 'price__exact',
    #     'price_lte': 'price__lte',
    #     'price_gte': 'price__gte',
    #     'price_lt': 'price__lt',
    #     'price_gt': 'price__gt',
    #     'credits': 'credits__exact',
    #     'credits_lte': 'credits__lte',
    #     'credits_gte': 'credits__gte',
    #     'credits_lt': 'credits__lt',
    #     'credits_gt': 'credits__gt',
    #     'provider_id': 'provider_id__exact',
    #     'provider_name': 'provider_name__icontains',
    #     'provider_name_exact': 'provider_name__exact',
    # }
=======
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    paginate_by = 12
    pagination_class = ResultsSetPaginationCEUCredit
>>>>>>> initalize

    def common_data(self, query_data, object_data):
        if (set(query_data) & set(object_data)):
            return True
        else:
            return False

    def apply_filters(self, queryset):
        filter_id = []
        media_types = [item.strip().upper() for item in self.request.GET.get('media_types', '').split(',')]
        ceu_types = [item.strip().upper() for item in self.request.GET.get('ceu_types', '').split(',')]
        if self.request.GET.get('media_types', '') or self.request.GET.get('ceu_types', ''):
            for item in queryset:
                if self.common_data(media_types, item.media) or self.common_data(ceu_types, item.type):
                    filter_id.append(item.id)
            queryset = CEUCredit.objects.filter(id__in=filter_id).order_by('title')
        return queryset

    def get_queryset(self):
        is_featured = self.request.GET.get('is_featured')
        if is_featured:
            self.queryset = self.queryset.filter(is_featured=True)
        return self.apply_filters(self.queryset)

class CEUImageFileCustomFilterSet(django_filters.FilterSet):
    filename = django_filters.CharFilter(lookup_expr='icontains')
    image_url = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        fields = ('filename','image_url')
        model = CEUImageFile

class CEUImageFileViewSet(viewsets.ModelViewSet):

<<<<<<< HEAD
class CEUImageFileCustomFilterSet(django_filters.FilterSet):
    filename = django_filters.CharFilter(lookup_expr='icontains')
    image_url = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        fields = ('filename','image_url')
        model = CEUImageFile

class CEUImageFileViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUImageFile.objects.all().order_by('filename')
    serializer_class = CEUImageFileSerializer
    filterset_class = CEUImageFileCustomFilterSet
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
=======
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = CEUImageFile.objects.all().order_by('filename')
    serializer_class = CEUImageFileSerializer
    filterset_class =CEUImageFileCustomFilterSet
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
>>>>>>> initalize
    paginate_by = 12
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return CEUImageFile.objects.all()

    def create(self, request, *args, **kwargs):
        request_copy = self.request.data.copy()
        request_copy['user'] = self.request.user.id
        serializer = self.get_serializer(data=request_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProvidersFilterView(APIView):
    serializer_class = ProviderFilterSerializer
    permission_classes = ()

    def get_object(self):
        return CEUCredit.objects.all().values('provider', 'provider__name', 'provider__id').annotate(
            count=Count('provider')).order_by(
            'count')

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(self.get_object(), many=True)
        return Response(serialized_data.data)


class InjectDataView(APIView):

    def post(self, request, *args, **kwargs):
        if request.data.get('file'):
            csv_file_queryset_object = CSVFile.objects.create(file=request.data.get('file'))
            celery_task = upload_items.delay(csv_file_queryset_object.id)
            response = {
                'Success': f'File {csv_file_queryset_object.id} upload successful and task assigned to Celery.',
                'tasks': {celery_task.id}
            }
            return Response(response)
        return Response({'error': 'No file attached'})

class MaxPriceView(APIView):
    serializer_class = CEUCreditMaxPriceSerializer
    permission_classes = ()

    def get_object(self):
        return CEUCredit.objects.all().order_by('-price').first()

    def get(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(self.get_object(), many=False)
        return Response(serialized_data.data)

class CEUCreditMaxPriceSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CEUCredit
        fields = ('price',)
