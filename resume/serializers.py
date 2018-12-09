from rest_framework import serializers
from .models import (Quotation,
                     Semester,
                     Course,
                     AcademicAward,
                     APCourse,
                     Language,
                     LanguageDetail,
                     Skill,
                     SkillDetail,
                     Position,
                     PriorTitle,
                     Duty,
                     DutyTag,
                     Project,
                     ProjectTag,)


class QuotationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes quotations; note change to default view name and lookup field
    """
    class Meta:
        model = Quotation
        fields = ('id',
                  'url',
                  'author',
                  'author_desc',
                  'quotation_text')
        extra_kwargs = {
            'url': {'view_name': 'quote_api_author',
                    'lookup_field': 'author'}
        }


class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    course_set = serializers.HyperlinkedRelatedField(many=True,
                                                     read_only=True,
                                                     view_name='course-detail')

    class Meta:
        model = Semester
        fields = ('id',
                  'url',
                  'time_period',
                  'gpa',
                  'deans_list',
                  'course_set')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
                  'url',
                  'semester',
                  'course_title',
                  'grade',
                  'description')


class AcademicAwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcademicAward
        fields = ('id',
                  'url',
                  'award_name',
                  'award_description',
                  'img',)


class APCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APCourse
        fields = ('id',
                  'url',
                  'course',
                  'score')


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id',
                  'url',
                  'language',
                  'proficiency',
                  'current',
                  'languagedetail_set')


class LanguageDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageDetail
        fields = ('id',
                  'url',
                  'language',
                  'detail')


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('id',
                  'url',
                  'skill',
                  'skill_type',
                  'skilldetail_set')


class SkillDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillDetail
        fields = ('id',
                  'url',
                  'skill',
                  'skill_detail')


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('id',
                  'url',
                  'title',
                  'employer',
                  'start_date',
                  'end_date',
                  'priortitle_set',
                  'duty_set',
                  'project_set',)


class PriorTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PriorTitle
        fields = ('id',
                  'url',
                  'current_position',
                  'prior_title',
                  'promotion_date')


class DutySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Duty
        fields = ('id',
                  'url',
                  'job',
                  'job_duty',
                  'prior',
                  'dutytag_set')


class DutyTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DutyTag
        fields = ('id',
                  'url',
                  'duty',
                  'duty_tag')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'url',
                  'job',
                  'project_name',
                  'project_description',
                  'projecttag_set')


class ProjectTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ('id',
                  'url',
                  'project',
                  'project_tag')
