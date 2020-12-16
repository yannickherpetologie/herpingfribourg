from django.db import models
from django.template.defaultfilters import slugify
from djrichtextfield.models import RichTextField

class Herp(models.Model):
    order_choices = (
        ('A', 'Amphibien'),
        ('R', 'Reptile')
    )
    iucn_choices = (
        ('I', 'Données insufissantes'),
        ('N', 'Non concerné'),
        ('L', 'Quasi menacé'),
        ('V', 'Vulnérable'),
        ('E', 'En danger'),
        ('C', 'Danger critique'),
        ('X', 'Eteint')
    )
    order = models.CharField(max_length=1, verbose_name='Ordre', choices=order_choices)
    scientific_name = models.CharField(max_length=64, verbose_name='Nom scientifique')
    common_name = models.CharField(max_length=64, verbose_name='Nom commun')
    author = models.CharField(max_length=64, verbose_name='Auteur')
    description = RichTextField()
    iucn_status = models.CharField(max_length=1, verbose_name='Status', choices=iucn_choices)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.scientific_name} ({self.author})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.scientific_name)
        super(Herp, self).save(*args, **kwargs)

class Site(models.Model):
    object = models.CharField(max_length=5, verbose_name="Object")
    name = models.CharField(max_length=64, verbose_name="Nom de l'objet")
    commune = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    gps = models.CharField(max_length=64)
    altitude = models.IntegerField()
    surface = models.FloatField()
    slug = models.SlugField(unique=True)
    population = models.ManyToManyField(Herp, through='Population')

    def __str__(self):
        return f"{self.object} {self.name} ({self.commune}, {self.district}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.object}-{self.district}-{self.commune}")
        super(Site, self).save(*args, **kwargs)

class Population(models.Model):
    size = (
        ('P', 'Petite'),
        ('M', 'Moyenne'),
        ('G', 'Grande'),
        ('T', 'Très grande')
    )
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='+')
    herp = models.ForeignKey(Herp, on_delete=models.CASCADE, related_name='+')
    population_size = models.CharField(max_length=1, choices=size)

def user_directory_path(self):
    pass
def herp_directory_path(self):
    pass

class HerpImage(models.Model):
    categories = (
        ('I', 'Image'),
        ('M', 'MP3'),
        ('V', 'Video')
    )
    category = models.CharField(max_length=1, choices=categories)
    herp = models.ForeignKey(Herp, on_delete=models.PROTECT)
    media = models.FileField(upload_to="uploads/species")
    description = models.TextField()

    def __str__(self):
        return f"{self.media}"

class Observation(models.Model):
    herp = models.ForeignKey(Herp, on_delete=models.PROTECT)
    observer = models.ForeignKey(to='users.User', on_delete=models.PROTECT, related_name='observer')
    date = models.DateField()
    quantity = models.CharField(max_length=12)
    area = models.CharField(max_length=64)
    image = models.ImageField(upload_to="uploads/species/observations/", blank=True)

    def __str__(self):
        return self.pk

