# Generated by Django 2.0.1 on 2021-01-29 08:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import upload.models
import upload.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('Office_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Mobile_no1', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('Mobile_no2', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('landline_no', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Create_folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=upload.models.UploadedFile)),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(max_length=256, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='images/', validators=[upload.validators.validate_file_extension])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_multiple', models.NullBooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('other', 'other')], max_length=10, null=True)),
                ('Role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(blank=True, upload_to='images/')),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(max_length=255, null=True)),
                ('grandfather_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=255, null=True)),
                ('citizenship_no', models.CharField(max_length=255, null=True)),
                ('issued_district', models.CharField(max_length=255, null=True)),
                ('issue_date', models.CharField(max_length=64, null=True)),
                ('temporary_address', models.CharField(max_length=255, null=True)),
                ('permanent_address', models.CharField(max_length=255, null=True)),
                ('Mobile_no', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('landline', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{7,15}$')])),
                ('secondary_school', models.CharField(max_length=255, null=True)),
                ('passed_year1', models.CharField(max_length=64, null=True)),
                ('division_percentage1', models.CharField(max_length=64, null=True)),
                ('intermediate_school', models.CharField(max_length=255, null=True)),
                ('passed_year2', models.CharField(max_length=64, null=True)),
                ('division_percentage2', models.CharField(max_length=64, null=True)),
                ('Bachelor', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_year3', models.CharField(blank=True, max_length=64, null=True)),
                ('division_percentage3', models.CharField(blank=True, max_length=64, null=True)),
                ('Masters', models.CharField(blank=True, max_length=255, null=True)),
                ('passed_year4', models.CharField(blank=True, max_length=64, null=True)),
                ('division_percentage4', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='create_folder',
            name='dir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.Directory'),
        ),
    ]
