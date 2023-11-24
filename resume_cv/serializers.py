from rest_framework import serializers

from resume_cv.models import (
    Award,
    Certificate,
    Contact,
    Education,
    Experience,
    ResumeCV,
    Skill,
)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']
        read_only_fields = fields


class ExperienceSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.get_fields()]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.get_fields()]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.get_fields()]


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.get_fields()]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.get_fields()]


class ResumeCVSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    experiences = ExperienceSerializer(read_only=True, many=True)
    educations = EducationSerializer(read_only=True, many=True)
    certificates = CertificateSerializer(read_only=True, many=True)
    awards = AwardSerializer(read_only=True, many=True)

    class Meta:
        model = ResumeCV
        fields = [
            'id',
            'title',
            'summary',
            'contact',
            'experiences',
            'educations',
            'certificates',
            'awards',
            'first_name',
            'last_name',
            'full_name',
        ]
        read_only_fields = [f.name for f in model._meta.get_fields()]
