from django.db import models
from django.utils.text import slugify
from pytz import timezone  # 현지 시각 출력을 위하여
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Juicy(models.Model):
    year = models.IntegerField()
    count= models.IntegerField()

    def __str__(self):
        return '쥬씨: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'JUICY'

class Gongcha(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '공차: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'GONGCHA'

class Subway(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '서브웨이: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'SUBWAY'

class Starbucks(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '스타벅스: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'STARBUCKS'

class Momstouch(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '맘스터치: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'MOMSTOUCH'

class Ediya(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '이디야: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'EDIYA'

class Sinjeon(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '신전떡볶이: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'SINJEON'

class Caffebene(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '카페베네: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'CAFFEBENE'

class Mrsd(models.Model):
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return '명랑핫도그: {}'.format(self.year)
    class Meta:
        verbose_name_plural = 'MRSD'