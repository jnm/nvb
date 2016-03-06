from rest_framework import viewsets

from models import (
    Bike, Youth, Adult, Stand, SkillCategory, Skill, Part, ShopSession,
    Activity, ActivitySkill, ActivityPart)

from serializers import (
    BikeSerializer, YouthSerializer, AdultSerializer, StandSerializer,
    SkillCategorySerializer, SkillSerializer, PartSerializer,
    ShopSessionSerializer, ActivitySerializer)

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class YouthViewSet(viewsets.ModelViewSet):
    queryset = Youth.objects.all()
    serializer_class = YouthSerializer


class AdultViewSet(viewsets.ModelViewSet):
    queryset = Adult.objects.all()
    serializer_class = AdultSerializer


class StandViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class ShopSessionViewSet(viewsets.ModelViewSet):
    queryset = ShopSession.objects.all()
    serializer_class = ShopSessionSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
