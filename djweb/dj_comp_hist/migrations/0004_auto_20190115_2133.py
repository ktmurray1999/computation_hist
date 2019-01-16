# Generated by Django 2.1.5 on 2019-01-15 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0003_auto_20190114_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.OneToOneField(on_delete=models.SET(None), to='dj_comp_hist.Page')),
            ],
        ),
        migrations.RenameField(
            model_name='folder',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='filename',
        ),
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.CharField(default=None, max_length=191),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='recipient',
            field=models.ManyToManyField(related_name='recipient', to='dj_comp_hist.Person'),
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(default=None, max_length=191),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.ManyToManyField(related_name='author', to='dj_comp_hist.Person'),
        ),
        migrations.AddField(
            model_name='page',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_comp_hist.Document'),
        ),
        migrations.AddField(
            model_name='image',
            name='page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dj_comp_hist.Page'),
        ),
        migrations.AddField(
            model_name='folder',
            name='box',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dj_comp_hist.Box'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='organization',
            field=models.ManyToManyField(to='dj_comp_hist.Organization'),
        ),
    ]