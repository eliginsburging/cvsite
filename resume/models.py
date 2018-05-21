from django.db import models


class Semester(models.Model):
    time_period = models.CharField(max_length=20)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    deans_list = models.BooleanField()

    def __str__(self):
        return f"{self.TimePeriod} - {self.GPA}"


class Course(models.Model):

    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    course_title = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.CourseTitle} - {self.Grade}"


class AcademicAwards(models.Model):

    award_name = models.CharField(max_length=120)
    award_description = models.TextField()

    def __str__(self):
        return self.award_name


class Quotation(models.Model):

    author = models.CharField(max_length=40)
    author_desc = models.TextField()
    quotation_text = models.TextField()

    def __str__(self):
        return self.author


class Position(models.Model):

    title = models.CharField(max_length=40)
    employer = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    prior_title_one = models.CharField(max_length=40, null=True)
    prior_title_two = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f"{self.title} - {self.employer}"


class Duty(models.Model):

    job = models.ForeignKey('Position', on_delete=models.CASCADE)
    job_duty = models.TextField()

    def __str__(self):
        return f"{self.job.title} - {self.job_duty}"


class DutyTag(models.Model):

    duty = models.ManyToManyField(Duty)
    duty_tag = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.duty.job_duty} - {self.duty_tag}"


class Interest(models.Model):

    interest_title = models.CharField(max_length=25)
    interest_description = models.TextField()
    img_file = models.CharField(max_length=40)
    img_text = models.TextField(null=True)

    def __str__(self):
        return self.interest_title


class Ideal(models.Model):

    ideal_title = models.CharField(max_length=40)
    ideal_description = models.TextField()


class Language(models.Model):

    language = models.CharField(max_length=20)
    proficiency = models.CharField(max_length=20)
    current = models.BooleanField()
    description = models.TextField()


class Skill(models.Model):

    skill = models.CharField(max_length=20)
    skill_type = models.CharField(max_length=20)


class SkillDetail(models.Model):

    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    skill_detail = models.TextField()
