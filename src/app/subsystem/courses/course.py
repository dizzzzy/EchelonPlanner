from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    department = models.CharField(max_length=120, null=False, blank=False, default="SOEN", primary_key=False)
    number = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    deptnum = models.CharField (max_length=120, primary_key=True, default="SOEN101") # concat of dept and num
    type = models.CharField(max_length=120, null=True, blank=True, primary_key=False) # scrapper doesn't know type yet
    credits = models.FloatField(default=0, primary_key=False)
    prerequisites = models.ManyToManyField("self", null=True, blank=True, symmetrical=False)
    #equivalence = models.ForeignKey(null = True, blank= True) #scrapper doesn't know equivalence
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False, default="14-15") #scrapper has this info, but not sure how to incorp

    def __str__(self):
        return self.deptnum

    def allLectures(self, semester=None):

        if semester is None:
            return list(self.lecture_set.all())
        else:
            return list(self.lecture_set.all().filter(semester=semester))

    def hasTutorials(self):
        if len(self.tutorial_set.all()) == 0:
            return False
        else:
            return True

    def allTutorials(self, semester=None):
        if len(self.tutorial_set.all()) == 0:
            return []
        elif semester is None:
            return list(self.tutorial_set.all())
        else:
            return list(self.tutorial_set.all().filter(event__semester=semester))

    def hasLabs(self):
        if len(self.lab_set.all()) == 0:
            return False
        else:
            return True

    def allLabs(self, semester=None):
        if len(self.lab_set.all()) == 0:
            return []
        elif semester is None:
            return list(self.lab_set.all())
        else:
            return list(self.lab_set.all().filter(event__semester=semester))

    def addStudent(IDNumber):
        pass

    def removeStudent(IDNumber):
        pass

    class Meta:
        app_label = 'app'
        managed= True

# End class Course