from django.db import models


class WorkThread(models.Model):
    ON = "ON"
    OFF = "OF"
    NEW = "NW"
    STATUS_CHOICES = [(ON, 'thread running'),
                      (OFF, 'thread terminating'),
                      (NEW, 'thread initializing'),
                      ]
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=ON)
    models.ForeignKey("cleanIpCore.Session", on_delete=models.CASCADE)


class Session(models.Model):
    ON = "ON"
    OFF = "OFF"
    STATUS_CHOICES = [(ON, 'session runnig'),
                      (OFF, 'session offline'),
                      ]
    name = models.TextField(max_length=150,
                            default='unnamed')
    ip = models.CharField(max_length=25)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=ON)


class Message(models.Model):
    IN = "IN"
    OUT = "OU"
    DIRECT_CHOICES = [(IN, 'direct_in'),
                      (OUT, 'direct_out'),
                      ]
    direct = models.CharField(max_length=2,
                              choices=DIRECT_CHOICES,
                              default=IN)
    ip = models.CharField(max_length=25)
    text = models.TextField(default='')
    btext = models.BinaryField(default=b'')
