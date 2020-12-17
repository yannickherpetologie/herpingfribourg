# Generated by Django 3.1.4 on 2020-12-16 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64)),
                ('t_length', models.FloatField(verbose_name='Longueur')),
                ('nb_trap', models.IntegerField(verbose_name='Nombre de sceaux')),
                ('date_begin', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Herp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(choices=[('A', 'Amphibien'), ('R', 'Reptile')], max_length=1, verbose_name='Ordre')),
                ('scientific_name', models.CharField(max_length=64, verbose_name='Nom scientifique')),
                ('common_name', models.CharField(max_length=64, verbose_name='Nom commun')),
                ('author', models.CharField(max_length=64, verbose_name='Auteur')),
                ('description', djrichtextfield.models.RichTextField()),
                ('iucn_status', models.CharField(choices=[('I', 'Données insufissantes'), ('N', 'Non concerné'), ('L', 'Quasi menacé'), ('V', 'Vulnérable'), ('E', 'En danger'), ('C', 'Danger critique'), ('X', 'Eteint')], max_length=1, verbose_name='Status')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population_size', models.CharField(choices=[('P', 'Petite'), ('M', 'Moyenne'), ('G', 'Grande'), ('T', 'Très grande')], max_length=1)),
                ('herp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='herp.herp')),
            ],
        ),
        migrations.CreateModel(
            name='SiteReproduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=5, verbose_name='Object')),
                ('type_object', models.CharField(choices=[('P', "Plan d'eau"), ('H', 'Zone humide'), ('I', 'Objet itinérant')], default='P', max_length=1)),
                ('name', models.CharField(max_length=64, verbose_name="Nom de l'objet")),
                ('commune', models.CharField(max_length=64)),
                ('district', models.CharField(max_length=64)),
                ('gps', models.CharField(max_length=64)),
                ('altitude', models.IntegerField()),
                ('surface', models.FloatField()),
                ('surface_b', models.FloatField(blank=True, default=0)),
                ('slug', models.SlugField(unique=True)),
                ('population', models.ManyToManyField(through='herp.Population', to='herp.Herp')),
            ],
        ),
        migrations.CreateModel(
            name='PopulationBarrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='herp.barrier')),
                ('herp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='herp.herp')),
            ],
        ),
        migrations.AddField(
            model_name='population',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='herp.sitereproduction'),
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.CharField(max_length=12)),
                ('area', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='uploads/species/observations/')),
                ('herp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='herp.herp')),
                ('observer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='observer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HerpImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('I', 'Image'), ('M', 'MP3'), ('V', 'Video')], max_length=1)),
                ('media', models.FileField(upload_to='uploads/species')),
                ('description', models.TextField()),
                ('herp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='herp.herp')),
            ],
        ),
        migrations.AddField(
            model_name='barrier',
            name='population',
            field=models.ManyToManyField(through='herp.PopulationBarrier', to='herp.Herp'),
        ),
    ]
