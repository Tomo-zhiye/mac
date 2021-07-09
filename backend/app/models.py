from django.db import models


class Property(models.Model):
    buildingName = models.CharField('物件名', max_length=100)
    title = models.CharField('タイトル', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True, blank=True)
    buildingType = models.CharField('建物の種類（戸建て、集合住宅など）', max_length=100, blank=True)
    price = models.IntegerField()
    buildingAge = models.IntegerField()
    floor = models.CharField('階建', max_length=100, blank=True)
    transportation  = models.CharField('交通', max_length=100, blank=True)
    address = models.CharField('所在地', max_length=100, blank=True)
    showerRoomAndBathRoom = models.CharField('バス、トイレ', max_length=100, blank=True)
    kitchen = models.CharField('キッチン', max_length=100, blank=True)
    Feature = models.CharField('設備・サービス', max_length=100, blank=True)
    other = models.CharField('その他', max_length=100, blank=True)
    renovation = models.CharField('リフォーム', max_length=100, blank=True)
    size = models.IntegerField(blank=True, default=0)
    typeOfBuildingConstruction = models.CharField('建物構造', max_length=100, blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', blank=True)
    entranceImage = models.ImageField(upload_to='images', verbose_name='エントランス写真', blank=True)
    exteriorImage = models.ImageField(upload_to='images', verbose_name='外観写真', blank=True)
    floorPlan = models.ImageField(upload_to='images', verbose_name='間取り図', blank=True)
    buildingDescription = models.TextField('物件詳細', blank=True)


    def __str__(self):
        return self.title

class Favorite(models.Model):
    properties = models.models.ManyToManyField(Property, verbose_name=_(""))


    def __str__(self):
        return self.title