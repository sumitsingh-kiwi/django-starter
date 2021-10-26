"""
views
"""
# django imports
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# local imports
from apps.notifications.messages import SUCCESS_CODE
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationListSerializer, RegisterDevice
from apps.utility.pagination import LimitOffsetPagination


class NotificationViewSet(viewsets.GenericViewSet):
    """ used to do the notification actions """
    serializer_class = NotificationListSerializer

    def list(self, request, *args, **kwargs):
        """ list the notifications """
        queryset = Notification.objects.filter(notification_to=request.user).order_by('-id')
        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(queryset, request=request)
        serializer = NotificationListSerializer(page, many=True)
        paginated_data = paginator.get_paginated_response(serializer.data)
        query = Q(is_read=False) & Q(notification_to=request.user)
        if queryset.exists():
            query &= Q(id__lte=queryset.first().id)

        Notification.objects.filter(query).update(is_read=True)
        return Response({'detail': SUCCESS_CODE['2001'], 'data': paginated_data},
                        status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='count', url_name='count')
    def get_notification_count(self, request):
        """ used to get the unread notification count """
        data = {
            'notification_count': Notification.objects.filter(is_read=False, notification_to=request.user).count()
        }
        return Response({'message': SUCCESS_CODE['2001'], 'data': data},
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='device', url_name='device', serializer_class=RegisterDevice,
            permission_classes=[IsAuthenticated, ])
    def fcm_registration(self, request):
        """ used to save the fcm token """
        serializer = self.get_serializer_class()(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': SUCCESS_CODE["2001"], 'data': None},
                        status=status.HTTP_200_OK)
