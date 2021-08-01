from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsCharityOwner, IsBenefactor
from charities.models import Task
from charities.serializers import (
    TaskSerializer, CharitySerializer, BenefactorSerializer
)


class BenefactorRegistration(APIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request):
        data = request.data
        benefactor_serializer = BenefactorSerializer(
            data= {'experience': data['experience'],
                   'free_time_per_week':data['free_time_per_week']})
        if benefactor_serializer.is_valid():
            benefactor_serializer.save(user= request.user)
            return Response(
                data={
                    'message': f'Congratulations <<{request.user.username}>>You have been successfully registered as a benefactor!'
                    },
                status= status.HTTP_200_OK)
        return Response(data= {'errors':benefactor_serializer.errors})


class CharityRegistration(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data 
        charity_serializer = CharitySerializer(
            data= {'name': data['name'],
                   'reg_number':data['reg_number']})
        if charity_serializer.is_valid():
            charity_serializer.save(user= request.user)
            return Response(
                data={
                    'message': f'Congratulations <<{request.user.username}>>You have been successfully registered as a charity!'
                    },
                status= status.HTTP_200_OK)
        return Response(data= {'errors':charity_serializer.errors})

class Tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all_related_tasks_to_user(self.request.user)

    def post(self, request, *args, **kwargs):
        data = {
            **request.data,
            "charity_id": request.user.charity.id
        }
        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsCharityOwner, ]

        return [permission() for permission in self.permission_classes]

    def filter_queryset(self, queryset):
        filter_lookups = {}
        for name, value in Task.filtering_lookups:
            param = self.request.GET.get(value)
            if param:
                filter_lookups[name] = param
        exclude_lookups = {}
        for name, value in Task.excluding_lookups:
            param = self.request.GET.get(value)
            if param:
                exclude_lookups[name] = param

        return queryset.filter(**filter_lookups).exclude(**exclude_lookups)


class TaskRequest(APIView):
    pass


class TaskResponse(APIView):
    pass


class DoneTask(APIView):
    pass