from django.shortcuts import render
from .models import (Quotation,
                     Semester,
                     Course,
                     AcademicAward,
                     APCourse)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (QuotationSerializer,
                          SemesterSerializer,
                          CourseSerializer,
                          AcademicAwardSerializer,
                          APCourseSerializer)

# Create your views here.


def index_page(request):
    welcome_text = ("My name is Eli Ginsburg-Marcy, and I would like to "
                    "welcome you to my personal website. The original idea "
                    "behind this site was to provide an extended version of "
                    "my resume, but during my third rebuild, I decided to "
                    "showcase more than just my work and educational history. "
                    "I hope that in looking over the site, you can get a"
                    " better sense of who I am, professionally and on a more "
                    "human level.")
    quote_list = Quotation.objects.only('author')
    starting_quote = Quotation.objects.get(pk=1)
    pics = ['portrait.jpg', 'ACT.jpg', 'greeksoy2.png', 'me.jpg']
    return render(request, 'home.html', locals())


@api_view(['GET'])
def quote_detail(request, author):
    """
    retrieve quote text and details by author namm
    """
    try:
        quote = Quotation.objects.get(author=author)
    except Quotation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = QuotationSerializer(quote, context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def semester_detail(request, pk):
    """
    retrieve semester by pk
    """
    try:
        sem = Semester.objects.get(pk=pk)
    except Semester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SemesterSerializer(sem, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def semester_list(request):
    """
    retrieve all semseters
    """
    sem_set = Semester.objects.all()
    serializer = SemesterSerializer(sem_set, many=True,
                                    context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def course_detail(request, pk):
    """
    retrieve course by pk
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(course, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def award_detail(request, pk):
    """
    retrieve award by pk
    """
    try:
        award = AcademicAward.objects.get(pk=pk)
    except AcademicAward.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AcademicAwardSerializer(award, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def award_list(request):
    """
    retrieve list of awards
    """
    award_set = AcademicAward.objects.all()
    serializer = AcademicAwardSerializer(award_set,
                                         many=True,
                                         context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def apcourse_detail(request, pk):
    """
    retrieve apcourse by pk
    """
    try:
        apcourse = APCourse.objects.get(pk=pk)
    except APCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = APCourseSerializer(apcourse, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def apcourse_list(request):
    """
    retrieve list of apcourses
    """
    apcourse_set = APCourse.objects.all()
    serializer = APCourseSerializer(apcourse_set,
                                        many=True,
                                        context={'request': request})
    return Response(serializer.data)
