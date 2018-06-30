# Generated by Django 2.0.2 on 2018-06-30 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=120)),
                ('award_description', models.TextField()),
                ('img', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='APCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_duty', models.TextField()),
                ('prior', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DutyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_tag', models.CharField(choices=[('Critical Thinking', 'Critical Thinking'), ('Writing', 'Writing'), ('Time and Project Management', 'Time and Project Management'), ('Client Service', 'Client Service'), ('Teaching', 'Teaching'), ('Administrative', 'Administrative'), ('Supervisory', 'Supervisory')], max_length=30)),
                ('duty', models.ManyToManyField(to='resume.Duty')),
            ],
        ),
        migrations.CreateModel(
            name='Ideal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideal_title', models.CharField(max_length=40)),
                ('ideal_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_title', models.CharField(max_length=25)),
                ('interest_description', models.TextField()),
                ('img_file', models.CharField(max_length=40)),
                ('img_text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('proficiency', models.CharField(max_length=20, null=True)),
                ('current', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LanguageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('employer', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriorTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prior_title', models.CharField(max_length=50)),
                ('promotion_date', models.DateField()),
                ('current_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Position')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_tag', models.CharField(choices=[('Critical Thinking', 'Critical Thinking'), ('Writing', 'Writing'), ('Time and Project Management', 'Time and Project Management'), ('Client Service', 'Client Service'), ('Teaching', 'Teaching'), ('Administrative', 'Administrative'), ('Supervisory', 'Supervisory')], max_length=30)),
                ('project', models.ManyToManyField(to='resume.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('author_desc', models.TextField()),
                ('quotation_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(max_length=20)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('deans_list', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
                ('skill_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SkillDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_detail', models.TextField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='duty',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Position'),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Semester'),
        ),
    ]
