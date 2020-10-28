from rest_framework import serializers
from .models import * 


class AboutUslinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUslink
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    about_us_links = AboutUslinkSerializer(many=True,read_only=True)
    
    class Meta:
        model = AboutUs
        fields = '__all__'

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

class BlogVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogVideo
        fields = '__all__'

class BlogLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLink
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    blog_links = BlogLinkSerializer(many=True,read_only=True)
    blog_images = BlogImageSerializer(many=True,read_only=True)
    blog_videos = BlogVideoSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class FieldWeWorkInSerializer(serializers.ModelSerializer):
      class Meta:
        model = FieldWeWorkIn
        fields = '__all__'

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideShow
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EbookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Ebook
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'