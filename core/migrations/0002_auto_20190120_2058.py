# Generated by Django 2.1.5 on 2019-01-20 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='final_pi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.FinalPi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gd_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.GroupDiscussionRound'),
        ),
        migrations.AlterField(
            model_name='student',
            name='pen_paper_round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PenPaperRound'),
        ),
        migrations.AlterField(
            model_name='student',
            name='task_round_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TaskRoundOne'),
        ),
        migrations.AlterField(
            model_name='student',
            name='task_round_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TaskRoundTwo'),
        ),
    ]
