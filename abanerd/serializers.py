from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Provider, CEUCredit, CEUMediaType, CEUCreditType, CEUImageFile, CEUSubmission

class ProviderSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'slug', 'url')

class CEUMediaTypeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CEUMediaType
        fields = ('id', 'name', 'slug')

class CEUCreditTypeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CEUCreditType
        fields = ('id', 'name', 'slug')

class CEUImageFileSerializer(FlexFieldsModelSerializer):

    original = serializers.SerializerMethodField()
    preview = serializers.SerializerMethodField()
    grid = serializers.SerializerMethodField()
    modal = serializers.SerializerMethodField()
    large = serializers.SerializerMethodField()

    class Meta:
        model = CEUImageFile
        fields = ('id', 'original', 'grid', 'modal', 'large')

    def get_original(self, obj):
        return obj.image.url

    def get_preview(self, obj):
        return obj.image.preview.url

    def get_grid(self, obj):
        return obj.image.grid.url

    def get_modal(self, obj):
        return obj.image.modal.url

    def get_large(self, obj):
        return obj.image.large.url

class CEUCreditSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = CEUCredit
        fields = (
            'id',
            'published_date',
            'title',
            'description',
            'url',
            'price',
            'credits',
            'slug',
            'url',
            'event_date',
            'is_featured',
            'media',
            'type',
            'image',
            'provider',
        )
        expandable_fields = {
            'media': CEUMediaTypeSerializer,
            'type': CEUCreditTypeSerializer,
            'image': CEUImageFileSerializer,
            'provider': ProviderSerializer,
        }

class CEUSubmissionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CEUSubmission
        fields = ('id', 'title', 'url', 'slug')

class CEUCreditMaxPriceSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CEUCredit
        fields = ('price',)

class CEUCreditProviderSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Provider
        fields = ('name',)

class ProviderFilterSerializer(serializers.Serializer):
    provider = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    def get_provider(self, obj):
        return obj.get('provider__name')

    def get_count(self, obj):
        return obj.get('count')

    def get_id(self, obj):
        return obj.get('provider__id')
