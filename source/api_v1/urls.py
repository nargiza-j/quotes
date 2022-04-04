from django.urls import path

from api_v1.views import QuoteCreateApi, QuoteListView, QuoteSingleObjectView

app_name = "api_v1"

urlpatterns = [
    # path('get-csrf-token/', get_csrf_token),
    path('quotes/', QuoteListView.as_view(), name="quotes"),
    path('quotes/create/', QuoteCreateApi.as_view(), name="create"),
    path('quotes/<int:pk>/', QuoteSingleObjectView.as_view(), name="quote-single-object"),
]