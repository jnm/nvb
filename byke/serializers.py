from rest_framework import serializers

from models import (
    Bike, Youth, Adult, Stand, SkillCategory, Skill, Part, ShopSession,
    Activity, ActivitySkill, ActivityPart)


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'


class YouthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youth
        fields = '__all__'


class AdultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adult
        fields = '__all__'


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = '__all__'


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class ShopSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopSession
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
