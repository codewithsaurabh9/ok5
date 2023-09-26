# Generated by Django 4.2.4 on 2023-09-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutphoto', models.ImageField(blank=True, upload_to='about/profile')),
                ('aboutdetail', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=150)),
                ('work', models.CharField(max_length=150)),
                ('freelance', models.CharField(max_length=150)),
                ('freelance_project', models.CharField(blank=True, max_length=150)),
                ('freelance_num', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='aboutproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Freelance_project', models.CharField(blank=True, max_length=150)),
                ('Freelance_num', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Services_name', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_date', models.CharField(blank=True, max_length=150)),
                ('education_name', models.CharField(blank=True, max_length=150)),
                ('education_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_date', models.CharField(blank=True, max_length=150)),
                ('experience_name', models.CharField(blank=True, max_length=150)),
                ('experience_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='first_display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstimage', models.ImageField(blank=True, upload_to='profile')),
                ('displayname', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='My_Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MySkills', models.CharField(blank=True, max_length=150)),
                ('percent', models.CharField(blank=True, max_length=150)),
                ('width_percent', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='My_Skills2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MySkills', models.CharField(blank=True, max_length=150)),
                ('percent', models.CharField(blank=True, max_length=150)),
                ('width_percent', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MyServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Servicespng', models.CharField(blank=True, max_length=150)),
                ('Services_name', models.CharField(blank=True, max_length=150)),
                ('Services_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MyPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Portfolio', models.ImageField(upload_to='Services/png')),
                ('Services_name', models.CharField(blank=True, max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.category')),
            ],
        ),
    ]
