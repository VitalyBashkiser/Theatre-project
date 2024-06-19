from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    GenreViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    ReservationViewSet,
    TicketViewSet,
    ActorRetrieveUpdateDestroyView,
    PerformanceListCreateView,
    PerformanceRetrieveUpdateDestroyView,
    ActorViewSet,
)

app_name = "api"

router = DefaultRouter()
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"plays", PlayViewSet)
router.register(r"theatre-halls", TheatreHallViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-retrieve-update-destroy",
    ),
    path(
        "performances/",
        PerformanceListCreateView.as_view(),
        name="performance-list-create",
    ),
    path(
        "performances/<int:pk>/",
        PerformanceRetrieveUpdateDestroyView.as_view(),
        name="performance-retrieve-update-destroy",
    ),
]
