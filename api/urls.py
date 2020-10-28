from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register('aboutUs',AboutUsViewSet)
router.register('aboutUsLink',AboutUsLinkViewSet)
router.register('blog',BlogLinkViewSet)
router.register('blogLink',BlogLinkViewSet)
router.register('blogLink',BlogImageViewSet)
router.register('blogLink',BlogVideoViewSet)
router.register('quote',QuoteViewSet)
router.register('fieldWeWorkIn',FieldWeWorkInViewSet)
router.register('slideshow',SlideShowViewSet)
router.register('video',VideoViewSet)
router.register('category',CategoryViewSet)
router.register('ebook',EbookViewSet)
router.register('discount',DiscountViewSet)

urlpatterns = [
]


urlpatterns += router.urls