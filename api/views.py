from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

# Update & Delete image not working in all sections
# that have ImageField

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsLinkViewSet(ModelViewSet):
    queryset = AboutUslink.objects.all()
    serializer_class = AboutUslinkSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogLinkViewSet(ModelViewSet):
    queryset = BlogLink.objects.all()
    serializer_class = BlogLinkSerializer

class BlogImageViewSet(ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer

class BlogVideoViewSet(ModelViewSet):
    queryset = BlogVideo.objects.all()
    serializer_class = BlogVideoSerializer

class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.order_by('-id')
    serializer_class = QuoteSerializer

class FieldWeWorkInViewSet(ModelViewSet):
    queryset = FieldWeWorkIn.objects.all()
    serializer_class = FieldWeWorkInSerializer

class SlideShowViewSet(ModelViewSet):
    queryset = SlideShow.objects.order_by('-id')
    serializer_class = SlideShowSerializer

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EbookViewSet(ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    
