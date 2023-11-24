from django.contrib.auth import get_user_model
from django.db import models

from salekcodes.models import Base


class Skill(Base):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')


class Experience(Base):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField('resume_cv.Skill', blank=True)
    url = models.URLField(blank=True, default='')


class Education(Base):
    organization_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    start_at = models.DateField()
    end_at = models.DateField(blank=True, null=True)


class Certificate(Base):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    issuer = models.CharField(max_length=255, blank=True, default='')
    issued_at = models.DateField(blank=True, null=True)
    expire_at = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, default='')
    related_experience = models.ForeignKey('resume_cv.Experience', on_delete=models.CASCADE, blank=True, null=True)


class Award(Base):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    issued_at = models.DateField(blank=True, null=True)
    related_experience = models.ForeignKey('resume_cv.Experience', on_delete=models.CASCADE, blank=True, null=True)


class Contact(Base):
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, default='')
    website = models.URLField(blank=True, default='')
    github = models.URLField(blank=True, default='')
    linkedin = models.URLField(blank=True, default='')


class ResumeCV(Base):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True, default='')
    contact = models.ForeignKey('resume_cv.Contact', on_delete=models.SET_NULL, blank=True, null=True)
    experiences = models.ManyToManyField('resume_cv.Experience', blank=True)
    educations = models.ManyToManyField('resume_cv.Education', blank=True)
    certificates = models.ManyToManyField('resume_cv.Certificate', blank=True)
    awards = models.ManyToManyField('resume_cv.Award', blank=True)
    version = models.PositiveIntegerField(default=1)
    is_public = models.BooleanField(default=False)

    @property
    def first_name(self) -> str:
        return self.user.first_name

    @property
    def last_name(self) -> str:
        return self.user.last_name

    @property
    def full_name(self) -> str:
        return self.user.full_name
