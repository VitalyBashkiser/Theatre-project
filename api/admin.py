from django.contrib import admin
from api.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ["name", "rows", "seats_in_row"]
    search_fields = ["name"]


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ["play", "theatre_hall", "show_time"]
    search_fields = ["play__title", "theatre_hall__name"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]
    search_fields = ["user__username"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["performance", "seat", "reservation"]
    search_fields = [
        "performance__play__title",
        "seat",
        "reservation__user__username",
    ]
