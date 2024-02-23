from rest_framework import routers
from core.auth.viewsets.register import RegisterViewSet
router = routers.SimpleRouter()
# ##################################################################### #
# ################### AUTH ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewSet, basename='auth-register')