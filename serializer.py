from rest_framework import serializers
from contest.models import Contest,Colleges,Challenges,View_Stats,Submission_Stats


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'



class CollegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleges
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = '__all__'


class ViewsStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = View_Stats
        fields = '__all__'


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission_Stats
        fields = '__all__'

