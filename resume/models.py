from django.db import models

tag_choices = (
    ("Critical Thinking", "Critical Thinking"),
    ("Writing", "Writing"),
    ("Time and Project Management", "Time and Project Management"),
    ("Client Service", "Client Service"),
    ("Teaching", "Teaching"),
    ("Administrative", "Administrative"),
    ("Supervisory", "Supervisory")
)


class Quotation(models.Model):

    author = models.CharField(max_length=40)
    author_desc = models.TextField()
    quotation_text = models.TextField()

    def __str__(self):
        return self.author


class Semester(models.Model):
    time_period = models.CharField(max_length=20)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    deans_list = models.BooleanField()

    def __str__(self):
        return f"{self.TimePeriod} - {self.GPA}"


class Course(models.Model):

    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    course_title = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.CourseTitle} - {self.Grade}"


class AcademicAward(models.Model):

    award_name = models.CharField(max_length=120)
    award_description = models.TextField()
    img = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.award_name


class APCourse(models.Model):

    course = models.CharField(max_length=50)
    score = models.CharField(max_length=20)


class Language(models.Model):

    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, null=True)
    current = models.BooleanField()


class LanguageDetail(models.Model):

    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    detail = models.TextField()


class Skill(models.Model):

    skill = models.CharField(max_length=20)
    skill_type = models.CharField(max_length=20)


class SkillDetail(models.Model):

    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    skill_detail = models.TextField()


class Position(models.Model):

    title = models.CharField(max_length=150)
    employer = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} - {self.employer}"


class PriorTitle(models.Model):

    current_position = models.ForeignKey('Position', on_delete=models.CASCADE)
    prior_title = models.CharField(max_length=50)
    promotion_date = models.DateField()


class Duty(models.Model):

    job = models.ForeignKey('Position', on_delete=models.CASCADE)
    job_duty = models.TextField()
    prior = models.BooleanField()

    def __str__(self):
        return f"{self.job.title} - {self.job_duty}"


class DutyTag(models.Model):

    duty = models.ManyToManyField(Duty)
    duty_tag = models.CharField(max_length=30, choices=tag_choices)

    def __str__(self):
        return f"{self.duty.job_duty} - {self.duty_tag}"


class Project(models.Model):

    job = models.ForeignKey("Position", on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()


class ProjectTag(models.Model):

    project = models.ManyToManyField("Project")
    project_tag = models.CharField(max_length=30, choices=tag_choices)


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


class BlogPost(models.Model):

    post_title = models.CharField(max_length=500)
    post_date = models.DateField(auto_now_add=True)
    post_content = models.TextField()  # insert photo slots by adding && between text
    post_pictures = models.TextField()  # this will be a comma separated list of
    # references to files on the server
