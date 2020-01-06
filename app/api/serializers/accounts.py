from rest_framework import serializers

from app.accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance):
        year = instance.birth_date.year
        data = super(ProfileSerializer, self).to_representation(instance)
        generation = ""

        if year <= 1964:
            generation =  'BABY BOOMER'
        elif 1965 <= year <= 1979:
            generation =  'GEN X'
        elif 1980 <= year <= 1994:
            generation = 'GEN Y'
        elif year >= 1995:
            generation = 'GEN Z'

        data['generation'] = generation
        return data