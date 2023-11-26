from .models import StickyNote
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets

class StickyNoteSerializer(serializers.Serializer):
    content = serializers.CharField()
    created_time = serializers.DateTimeField()
    created_user = serializers.EmailField()

class StickyNoteViewSet(viewsets.ModelViewSet):
    queryset = StickyNote.objects.all()
    serializer_class = StickyNoteSerializer

    @swagger_auto_schema(request_body=StickyNoteSerializer)
    def create(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).create(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: None, 302: 'Redirect somewhere'})
    def retrieve(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=StickyNoteSerializer)
    def update(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=StickyNoteSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).destroy(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: StickyNoteSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super(StickyNoteViewSet, self).list(request, *args, **kwargs)
