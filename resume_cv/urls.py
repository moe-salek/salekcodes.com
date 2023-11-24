from django.urls import path

from resume_cv.views import (
    AwardView,
    CertificateView,
    ContactView,
    EducationView,
    ExperienceView,
    ResumeCVView,
    SkillView,
)

urlpatterns = [
    # region skill
    path('skill/<int:id>/', SkillView.as_view({'get': 'retrieve'}), name='skill_detail'),
    path('skill/', SkillView.as_view({'get': 'list'}), name='skill'),
    # endregion
    # region experience
    path('experience/<int:id>/', ExperienceView.as_view({'get': 'retrieve'}), name='experience_detail'),
    path('experience/', ExperienceView.as_view({'get': 'list'}), name='experience'),
    # endregion
    # region education
    path('education/<int:id>/', EducationView.as_view({'get': 'retrieve'}), name='education_detail'),
    path('education/', EducationView.as_view({'get': 'list'}), name='education'),
    # endregion
    # region certificate
    path('certificate/<int:id>/', CertificateView.as_view({'get': 'retrieve'}), name='certificate_detail'),
    path('certificate/', CertificateView.as_view({'get': 'list'}), name='certificate'),
    # endregion
    # region award
    path('award/<int:id>/', AwardView.as_view({'get': 'retrieve'}), name='award_detail'),
    path('award/', AwardView.as_view({'get': 'list'}), name='award'),
    # endregion
    # region contact
    path('contact/<int:id>/', ContactView.as_view({'get': 'retrieve'}), name='contact_detail'),
    path('contact/', ContactView.as_view({'get': 'list'}), name='contact'),
    # endregion
    # region resume_cv
    path('resume_cv/<int:id>/', ResumeCVView.as_view({'get': 'retrieve'}), name='resume_cv_detail'),
    path('resume_cv/', ResumeCVView.as_view({'get': 'list'}), name='resume_cv'),
    # endregion
]
