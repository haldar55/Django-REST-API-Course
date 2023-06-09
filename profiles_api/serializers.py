from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIviews"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the user profile object"""
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        """Create and return a new user profile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Update a user profile, given the id"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    

class ProfileFeedItemSerialzer(serializers.ModelSerializer):
    """Profile feed item serializer"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ['id','user_profile','status_text','created_on']
        extra_kwargs = {'user_profile':{'read_only':True}}