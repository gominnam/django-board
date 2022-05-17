from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from board.models import Post, PostCategory


def validate_title(value):
    if len(value) < 10:
        raise ValidationError('title 열글자 이상 쓰세요 성의가없네 ㅋ')
    return value


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(validators=[validate_title])
    category = serializers.PrimaryKeyRelatedField(queryset=PostCategory.objects.all(), required=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'category')
