from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

app_name = "api"

router = DefaultRouter()
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"plays", PlayViewSet)
router.register(r"theatre-halls", TheatreHallViewSet)
router.register(r"performances", PerformanceViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"tickets", TicketViewSet)

urlpatterns = [path("", include(router.urls))]