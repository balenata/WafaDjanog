from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('admin',AdminViewSet)
router.register('aboutUs',AboutUsViewSet)
router.register('aboutUsLink',AboutUsLinkViewSet)
router.register('blog',BlogViewSet)
router.register('blogLink',BlogLinkViewSet)
router.register('blogImage',BlogImageViewSet)
router.register('blogVideo',BlogVideoViewSet)
router.register('quote',QuoteViewSet)
router.register('fieldWeWorkIn',FieldWeWorkInViewSet)
router.register('slideshow',SlideShowViewSet)
router.register('video',VideoViewSet)
router.register('category',CategoryViewSet)
router.register('ebook',EbookViewSet)
router.register('discount',DiscountViewSet)

urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
]


urlpatterns += router.urls