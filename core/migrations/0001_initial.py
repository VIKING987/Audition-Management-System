# Generated by Django 2.1.5 on 2019-01-20 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinalPi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_taken_by', models.CharField(max_length=255)),
                ('pi_review', models.CharField(max_length=255)),
                ('promote', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupDiscussionRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gd_review', models.CharField(max_length=255)),
                ('gd_taken_by', models.CharField(max_length=255)),
                ('promote', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PenPaperRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_taken_by', models.CharField(max_length=255)),
                ('pi_review', models.CharField(max_length=255)),
                ('pi_task', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('dept', models.CharField(max_length=20)),
                ('final_pi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.FinalPi')),
                ('gd_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.GroupDiscussionRound')),
                ('pen_paper_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PenPaperRound')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRoundOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=255)),
                ('task_given_by', models.CharField(max_length=255)),
                ('task_submission_date', models.CharField(max_length=255)),
                ('task_review', models.CharField(max_length=255)),
                ('task_done', models.BooleanField()),
                ('promote', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskRoundTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=255)),
                ('task_given_by', models.CharField(max_length=255)),
                ('task_submission_date', models.CharField(max_length=255)),
                ('task_review', models.CharField(max_length=255)),
                ('task_done', models.BooleanField()),
                ('promote', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='task_round_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaskRoundOne'),
        ),
        migrations.AddField(
            model_name='student',
            name='task_round_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaskRoundTwo'),
        ),
    ]
