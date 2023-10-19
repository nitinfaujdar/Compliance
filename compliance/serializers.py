from .models import *
from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'application_name', 'product_name', 'created_at', 'updated_at']
        

class ComplianceSerializer(serializers.ModelSerializer):
    apps_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Compliance
        fields = ['id', 'compliance', 'applications', 'apps_list', 'created_at', 'updated_at']


    @classmethod
    def get_apps_list(self, obj: Compliance):
        if obj.applications is not None:
            app_arr = obj.applications.split(',')
        return Application.objects.filter(pk__in=app_arr).values()