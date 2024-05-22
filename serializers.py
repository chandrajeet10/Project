from rest_framework import serializers
from .models import WorkExperience, Address, Qualification, Project, Employee


class WorkExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):   
    class Meta:     
        model = Address
        fields = '__all__'

class QualificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializers(serializers.ModelSerializer):
    address = AddressSerializers()
    work_experience = WorkExperienceSerializers(many=True)
    qualifications = QualificationSerializers(many=True)
    projects = ProjectSerializers(many=True)

    class Meta:
        model = Employee
        fields = '__all__'



