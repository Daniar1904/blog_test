from rest_framework import serializers
from django.contrib.auth.models import User


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')


class PostListSerializer(serializers.ModelSerializer):
    model = Post
    fields = '__all__'
# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')
#
#
# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ('password',)
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=8, write_only=True, required=True)
#     password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirmation')
#
#     def validate(self, attrs):
#         password2 = attrs.pop('password_confirmation')
#         if password2 != attrs['password']:
#             raise serializers.ValidationError('Passwords did not match!')
#
#         if not attrs['first_name'].istitle():
#             raise serializers.ValidationError('Name must start with uppercase letter!')
#         return attrs
#
#     def create(self, validated_data):
#         # user = User.objects.create(
#         #     username=validated_data['username'],
#         #     first_name=validated_data['first_name'],
#         #     last_name=validated_data['last_name'],
#         #     email=validated_data['email'],
#         # ) # вручную
#         user = User.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


