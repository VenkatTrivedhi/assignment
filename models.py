from django.db import models


class Contest(models.Model):
    contest_id = models.IntegerField(primary_key=True)
    hacker_id = models.IntegerField(max_length=20)
    Name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.contest_id)


class Colleges(models.Model):
    college_id = models.IntegerField(primary_key=True)
    contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.college_id)


class Challenges(models.Model):
    challenge_id = models.IntegerField(primary_key=True)
    college_id = models.ForeignKey(Colleges,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.challenge_id)


class View_Stats(models.Model):
    challenge_id = models.ForeignKey(Challenges,on_delete=models.CASCADE)
    total_views = models.IntegerField(max_length=20)
    total_unique_views = models.IntegerField(max_length=20)


class Submission_Stats(models.Model):
    challenge_id = models.ForeignKey(Challenges,on_delete=models.CASCADE)
    total_submission = models.IntegerField(max_length=20)
    total_accepted_submissions = models.IntegerField(max_length=20)