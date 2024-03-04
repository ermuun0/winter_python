from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.post.viewsets import PostViewSet
from rest_framework_nested import routers
from comment.viewsets import CommentViewSet
router = routers.SimpleRouter()
# ##################################################################### #
# ################### AUTH ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'post', PostViewSet, basename='post')
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet,
basename='post-comment')
urlpatterns = [
*router.urls,
*posts_router.urls
]