from django.db import models
from django.template.defaultfilters import slugify
from djrichtextfield.models import RichTextField

class Herp(models.Model):
    """ Espèces"""
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

    class Meta:
        verbose_name = "Espèce"
        verbose_name_plural = "Espèces"

    def __str__(self):
        return f"{self.scientific_name} ({self.author})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.scientific_name)
        super(Herp, self).save(*args, **kwargs)

"""
 Amphibiens
"""
class ReproductionSite(models.Model):
    site_type = (
        ('P', 'Plan d\'eau'),
        ('H', 'Zone humide'),
        ('I', 'Objet itinérant'),
    )
    object = models.CharField(max_length=5, verbose_name="Object")
    type_object = models.CharField(max_length=1, choices=site_type, default='P')
    name = models.CharField(max_length=64, verbose_name="Nom de l'objet")
    commune = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    gps = models.CharField(max_length=64)
    altitude = models.IntegerField()
    surface = models.FloatField()
    surface_b = models.FloatField(blank=True, default=0)
    slug = models.SlugField(unique=True)
    population = models.ManyToManyField(Herp, through='Population')

    class Meta:
        verbose_name = "Site de reproduction des amphibiens"
        verbose_name_plural = "Sites de reproduction des amphibiens"

    def __str__(self):
        return f"{self.object} {self.name} ({self.commune}, {self.district})"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.object}-{self.district}-{self.commune}")
        super(ReproductionSite, self).save(*args, **kwargs)

class Population(models.Model):
    """ Site de reproduction """
    size = (
        ('I', 'Inconnu'),
        ('P', 'Petite'),
        ('M', 'Moyenne'),
        ('G', 'Grande'),
        ('T', 'Très grande')
    )
    site = models.ForeignKey(ReproductionSite, on_delete=models.CASCADE, related_name='+')
    herp = models.ForeignKey(Herp, on_delete=models.CASCADE, related_name='+')
    population_size = models.CharField(max_length=1, choices=size, default='I')

    class Meta:
        verbose_name = "Population par site de reproduction"
        verbose_name_plural = "Populations par site de reproduction"

class Barrier(models.Model):
    """ Barrière """
    location = models.CharField(max_length=64)
    rte = models.CharField(max_length=64)
    t_length = models.FloatField(verbose_name="Longueur")
    nb_trap = models.IntegerField(verbose_name="Nombre de sceaux")
    date_begin = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    population = models.ManyToManyField(Herp, through='PopulationBarrier')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Barrière à amphibien"
        verbose_name_plural = "Barrières à amphibiens"

    def __str__(self):
        return f"{self.location}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.location}")
        super(Barrier, self).save(*args, **kwargs)

class PopulationBarrier(models.Model):
    """ Espèces présentes sur les barrières """
    barrier = models.ForeignKey(Barrier, on_delete=models.CASCADE, related_name='+')
    herp = models.ForeignKey(Herp, on_delete=models.CASCADE, related_name='+')

class HerpMedia(models.Model):
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

class Stream(models.Model):
    size = (
        ('I', 'Inconnu'),
        ('P', 'Petite'),
        ('M', 'Moyenne'),
        ('G', 'Grande'),
        ('T', 'Très grande')
    )
    probabilities =(
        ('C', 'Certaine'),
        ('M', 'Probable'),
        ('I', 'Impossible')
    )
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    probabilities = models.CharField(max_length=1, choices=probabilities, default='I', blank=True, null=True)
    population_size = models.CharField(max_length=1, choices=size, default='I', blank=True, null=True)

    def __str__(self):
        return f"{self.name} à {self.location} ({self.district})"

    class Meta:
        verbose_name = 'Ruisseau à salamandre tâchetée'
        verbose_name_plural = 'Ruisseaux à salamandre tâchetée'