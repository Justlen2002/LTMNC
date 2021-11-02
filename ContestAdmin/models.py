from django.db import models

# Create your models here.
# class Account(models.Model):
#     UserName = models.CharField(unique=True, max_length=100, default='')
#     Password = models.CharField(max_length=100)
#     Type = models.CharField(max_length=100)
#     Permission = models.CharField(max_length=100)
#
# class Contest(models.Model):
#     IDUser = models.CharField(max_length=100)
#     Title = models.TextField()
#     Description = models.TextField()
#     LinkContest = models.CharField(max_length=100)
#     LinkDataTrain = models.CharField(max_length=100)
#     LinkDataTest = models.CharField(max_length=100)
#     LinkTester = models.CharField(max_length=100)
#     TimeRegister = models.DateTimeField()
#     TimeStart = models.DateTimeField()
#     TimeEnd = models.DateTimeField()
#     TimeOut = models.IntegerField()
#     IDLanguage = models.CharField(max_length=100)
#
# class Status(models.Model):
#     IDcontest = models.CharField(max_length=100)
#     IDUser = models.CharField(max_length=100)
#     Status = models.CharField(max_length=100)
#     TimeSubmit = models.DateTimeField()
#     LinkSubmit = models.CharField(max_length=100)
#     def __str__(self):
#         return self.IDcontest
#
#
# class RegisterContest(models.Model):
#     IDContest = models.CharField(max_length=100)
#     IDUser = models.CharField(max_length=100)
#
# class Language(models.Model):
#     Language = models.CharField(max_length=100)
#

###################################################
class creator(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)

class adm(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)

class Contest(models.Model):
    creator_id = models.IntegerField()
    Title = models.CharField(max_length=45)
    Description = models.CharField(max_length=45)
    LinkContest = models.CharField(max_length=45)
    LinkDataTrain = models.CharField(max_length=45)
    LinkDataTest = models.CharField(max_length=45)
    LinkTester = models.CharField(max_length=45)
    TimeRegister = models.DateTimeField()
    TimeStart = models.DateTimeField()
    TimeEnd = models.DateTimeField()
    TimeOut = models.IntegerField()

# class problem(models.Model):
#     contest_id = models.IntegerField()

class submission(models.Model):
    status = models.CharField(max_length=45)
    TimeSubmit = models.DateTimeField()
    LinkSubmit = models.CharField(max_length=100)
    contest_id = models.IntegerField()
    candidate_id = models.IntegerField()

class candidate(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

class language(models.Model):
    Language = models.CharField(max_length=45)

class RegisterContest(models.Model):
    IDContest = models.IntegerField()
    IDUser = models.IntegerField()

class ChooseLanguage(models.Model):
    contest_id = models.IntegerField()
    language_id = models.IntegerField()