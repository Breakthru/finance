from django.db import models


class Account(models.Model):
    name = models.TextField()
    def __str__(self):
        return str(self.name)


class Statement(models.Model):
    date_added = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    # raw data from online banking
    document = models.BinaryField()


class Tag(models.Model):
    """ tag transactions """
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    raw = models.TextField()  # un-modified csv row
    ordering = ['-date']

    def __str__(self):
        return str(self.date)+" "+str(self.amount)

    @property
    def display_amount(self):
        return u"\xA3 %1.02f" % (self.amount / 100.0,)


