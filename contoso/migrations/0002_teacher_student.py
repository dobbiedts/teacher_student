# Generated by Django 3.0.3 on 2021-02-05 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contoso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_student',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contoso.teacher')),
                ('assigned_student', models.ManyToManyField(default=None, help_text='who is/are the students assigned to this teacher', to='contoso.student')),
            ],
            bases=('contoso.teacher',),
        ),
    ]
