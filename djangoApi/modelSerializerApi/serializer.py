from rest_framework import serializers

from .models import Athlete, Category


class AthleteSerializer(serializers.ModelSerializer):
    earthTime = serializers.IntegerField(source='age')
    athleticsTime = serializers.SerializerMethodField(

        method_name='athlete_span')
    category = serializers.StringRelatedField()

    class Meta:
        model = Athlete
        fields = ['id', 'name', 'discipline',
                  'earthTime', 'athleticsTime', 'category']

    def athlete_span(self, athlete: Athlete):
        return athlete.age-8
