from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from authentication.views import UserViewSet
from order.views import OrderViewSet
from book.views import BookViewSet
from author.views import AuthorViewSet

# Main router
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')

# Nested router: user -> order
user_router = NestedDefaultRouter(router, r'user', lookup='user')
user_router.register(r'order', OrderViewSet, basename='user-order')

urlpatterns = router.urls + user_router.urls
