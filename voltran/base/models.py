from django.db import models

class Member(models.Model):
    first_name = models.CharField("isim", max_length=100)
    last_name = models.CharField("soy isim", max_length=100)
    description = models.TextField("aciklama", max_length=200)

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"

    def __str__(self):
        return self.first_name
    


class Log(models.Model):
    title = models.CharField("baslik", max_length=60) 
    description = models.TextField("Aciklama")
    date = models.DateTimeField("tarih")

    class Meta:
        verbose_name = "log"
        verbose_name_plural = "logs"

    def __str__(self):
        return self.title
    


class Project(models.Model):
    project_title = models.CharField("proje baslik", max_length=60)    
    project_description = models.TextField("proje aciklama")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.project_title
    