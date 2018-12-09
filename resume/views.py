from django.shortcuts import render
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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (QuotationSerializer,
                          SemesterSerializer,
                          CourseSerializer,
                          AcademicAwardSerializer,
                          APCourseSerializer,
                          LanguageSerializer,
                          LanguageDetailSerializer,
                          SkillSerializer,
                          SkillDetailSerializer,
                          PositionSerializer,
                          PriorTitleSerializer,
                          DutySerializer,
                          DutyTagSerializer,
                          ProjectSerializer,
                          ProjectTagSerializer,)

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


@api_view(['GET'])
def language_detail(request, pk):
    """
    retrieve a language by pk
    """
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LanguageSerializer(language, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def language_list(request, iscurrent="all"):
    """
    retrieve list of languages
    """
    if iscurrent == "all":
        language_set = Language.objects.all()
    elif iscurrent == "current":
        language_set = Language.objects.filter(current='True')
    elif iscurrent == "past":
        language_set = Language.objects.filter(current='False')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LanguageSerializer(language_set,
                                    many=True,
                                    context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def languagedetail_detail(request, pk):
    """
    retrieve language detail by pk
    """
    try:
        language_det = LanguageDetail.objects.get(pk=pk)
    except LanguageDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LanguageDetailSerializer(language_det,
                                          context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def skill_detail(request, pk):
    """
    retrieve skill by pk
    """
    try:
        skill = Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SkillSerializer(skill,
                                 context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def skill_list(request):
    """
    retrieve list of all skills
    """
    skill_set = Skill.objects.all()
    serializer = SkillSerializer(skill_set,
                                 many=True,
                                 context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def skilldetail_detail(request, pk):
    """
    retrieve skill detail by pk
    """
    try:
        skill_det = SkillDetail.objects.get(pk=pk)
    except SkillDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SkillDetailSerializer(skill_det,
                                       context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def position_detail(request, pk):
    """
    retrieve position by pk
    """
    try:
        position_det = Position.objects.get(pk=pk)
    except Position.DoesNotExist:
        return
    serializer = PositionSerializer(position_det,
                                    context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def position_list(request):
    """
    retrieve list of all positions
    """
    position_set = Position.objects.all()
    serializzer = PositionSerializer(position_set,
                                     many=True,
                                     context={'request': request})
    return Response(serializzer.data)


@api_view(['GET'])
def priortitle_detail(request, pk):
    """
    retrieve prior title by pk
    """
    try:
        priortitle_det = PriorTitle.objects.get(pk=pk)
    except PriorTitle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PriorTitleSerializer(priortitle_det,
                                      context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def duty_detail(request, pk):
    """
    retrieve duty by pk
    """
    try:
        duty_det = Duty.objects.get(pk=pk)
    except Duty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DutySerializer(duty_det,
                                context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def dutytag_detail(request, pk):
    """
    retrieve duty tag by pk
    """
    try:
        dutytag_det = DutyTag.objects.get(pk=pk)
    except DutyTag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DutyTagSerializer(dutytag_det,
                                   context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, pk):
    """
    retrieve project by pk
    """
    try:
        project_det = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProjectSerializer(project_det,
                                   context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def projecttag_detail(request, pk):
    """
    retrieve project tag by pk
    """
    try:
        projecttag_det = ProjectTag.objects.get(pk=pk)
    except ProjectTag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProjectTagSerializer(projecttag_det,
                                      context={'request': request})
    return Response(serializer.data)
