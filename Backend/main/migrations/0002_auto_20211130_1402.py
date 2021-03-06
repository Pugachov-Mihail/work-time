# Generated by Django 3.2.6 on 2021-11-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plansmonth',
            options={'verbose_name_plural': 'Планы на месяц'},
        ),
        migrations.AlterModelOptions(
            name='shopname',
            options={'verbose_name_plural': 'Название торговой точки'},
        ),
        migrations.CreateModel(
            name='PlansDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal', models.IntegerField(verbose_name='Железо')),
                ('accs', models.IntegerField(verbose_name='Аксы')),
                ('dop', models.IntegerField(verbose_name='Доп оборот')),
                ('oss', models.IntegerField(verbose_name='ОСС')),
                ('setting', models.IntegerField(verbose_name='Настройки')),
                ('bil', models.IntegerField(verbose_name='Билайн')),
                ('mega', models.IntegerField(verbose_name='Мегафон')),
                ('yota', models.IntegerField(verbose_name='Yota')),
                ('tele', models.IntegerField(verbose_name='Теле 2')),
                ('persone', models.IntegerField(verbose_name='Сотрудников')),
                ('date', models.DateTimeField(auto_now=True)),
                ('shopname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shopname', verbose_name='Название ТТ')),
            ],
            options={
                'verbose_name_plural': 'Планы на день',
            },
        ),
    ]
