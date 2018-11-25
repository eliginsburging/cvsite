from rest_framework import serializers
from .models import (Quotation,
                     Semester,
                     Course,
                     AcademicAward,
                     APCourse)


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
