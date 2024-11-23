# Generated by Django 5.1.1 on 2024-11-22 02:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lab', '0005_alter_tiposanguineo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analise',
            name='data_solicitacao',
        ),
        migrations.RemoveField(
            model_name='analise',
            name='preco',
        ),
        migrations.AlterField(
            model_name='analise',
            name='data_realizacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analise',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_lab.exame'),
        ),
    ]