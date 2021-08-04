from inspect import currentframe
from django.http.response import HttpResponse
from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom, GetRoomById, CreateRoomView2, CurrentSession, HttpRequest, DeleteRoom, CurrentSessionRoom

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view()),
    path('get-room-by-id/<int:pk>/', GetRoomById.as_view()),
    path('create-room-2', CreateRoomView2.as_view()),
    path('session', CurrentSession.as_view()),
    path('sessionroom', CurrentSessionRoom.as_view()),
    path('http-request', HttpRequest.as_view()),
    path('room/<str:code>', DeleteRoom.as_view()),
]
