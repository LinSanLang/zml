from rest_framework import serializers
from .models import *

class DepartmentSerizlizer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少3个字"
    })

    def create(self, validated_data):
        instance = Department.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance

class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })
    department = DepartmentSerizlizer(label="部门")

    def validate_category(self, department):

        try:
            Department.objects.get(name = department["name"])
        except:
            raise serializers.ValidationError("输入的部门名不存在")

        return department

    def validate(self, attrs):
        try:
            c = Department.objects.get(name=attrs["department"]["name"])
        except:
            c = Department.objects.create(name = attrs["department"]["name"])
        attrs["department"] = c
        return attrs

    def create(self, validated_data):
        instance = People.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.department = validated_data.get("department",instance.department)
        instance.save()
        return instance