

# from django.urls import path
# from .views import BookViewSet

# # urlpatterns = [
# #     path('list/', books_list),
# #     path('', create_book),
# #     path('<str:title>', book),
# # ]
# urlpatterns = [
#     path('list/',BookViewSet.as_view()),
#     # path('', create_book),
#     # path('<str:title>', book),
# ]


from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('list', views.BookViewSet)
urlpatterns = router.urls

