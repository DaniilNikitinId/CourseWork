from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class PublishedManager(models.Manager):  # новый менеджер
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Store.Status.PUBLISHED)


class Store(models.Model):
    class Status(models.IntegerChoices):  # описание для виджета
        DRAFT = 0, 'черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=400,validators=[MinLengthValidator(5)] ,verbose_name='Заголовок')
    price = models.IntegerField(verbose_name='Цена', validators=[MinValueValidator(1), MaxValueValidator(100000)],default=0)
    #age = models.ForeignKey('Age', on_delete=models.PROTECT, related_name='age', verbose_name='возраст', null=True,blank=True, help_text="Заполняется, если есть явное указание на упаковке")
    age = models.ManyToManyField('Age', blank=True, related_name='size', verbose_name='Возраст')
    typeFeed = models.ForeignKey('TypeFeed', on_delete=models.PROTECT, related_name='typeFeed',verbose_name='вид корма', null=True, blank=True)
    size = models.ManyToManyField('Size', blank=True, related_name='size', verbose_name='Размер животного')
    weight = models.CharField(max_length=5, verbose_name='Вес', blank=True, null=True)
    taste = models.CharField(max_length=400, verbose_name='Вкус', blank=True, null=True)
    article = models.CharField(max_length=255, verbose_name='Артикул', blank=True, null=True)
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name='Слаг')
    photo = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='текст статьи')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='время обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),default=Status.DRAFT, verbose_name='статус')
    cat2 = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='cats', verbose_name='Категории', null=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='brands', verbose_name='Бренд', null=True,blank=True)
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='тег')

    main_product = models.ForeignKey('Store', verbose_name="Основной продукт", on_delete=models.PROTECT, help_text="Заполняется если текущий продукт является подпродуктом основного, отличаются по весу и т.п", null=True, blank=True, related_name="sub_products")

    objects = models.Manager()  # старый менеджер
    published = PublishedManager()  # определение нового менеджера

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})  # формирование адреса

    def __str__(self):
        return self.title


class Category(models.Model):  # m2o
    name = models.CharField(max_length=400, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=400, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Brand(models.Model):  # m2o
    name = models.CharField(max_length=255, db_index=True, verbose_name='Бренд')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_slug': self.slug})


class Age(models.Model):  # m2o
    name = models.CharField(max_length=255, db_index=True, verbose_name='Возраст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('age', kwargs={'age_slug': self.slug})


class Size(models.Model):  # m2o
    name = models.CharField(max_length=255, db_index=True, verbose_name='Возраст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Размер животного'
        verbose_name_plural = 'Размер животного'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('size', kwargs={'size_slug': self.slug})


class TypeFeed(models.Model):  # m2o
    name = models.CharField(max_length=255, db_index=True, verbose_name='Возраст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Вид корма'
        verbose_name_plural = 'Вид корма'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('typeFeed', kwargs={'typeFeed_slug': self.slug})


class TagPost(models.Model):
    objects = None
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Тег'  # что написано в админке
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.tag
