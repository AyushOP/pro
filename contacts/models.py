from django.db import models
from django.contrib.auth.models import User
from django import forms

class Contact(models.Model):

    COMPANY_NAME = (
        ('NA','n'),
        ('TCS','TCS'),
        ('INFOSYS','INFOSYS'),
        ('ACCENTURE','ACCENTURE'),
        ('AMZON','AMAZON'),
        ('HIGHRADIUS','HIGHRADIUS'),
    )
    co_name = models.CharField(max_length=20,choices=COMPANY_NAME,default='NA')
    name = models.CharField(max_length=30)
    SALUTATION = (
        ('NA','NA'),
        ('Colonel','Colonel'),
        ('Mr.','Mr.'),
        ('Mrs','Mrs.'),
        ('Dr','Dr'),
    )
    salutation = models.CharField(max_length=20,choices=SALUTATION,default='NA')
    REFERRED_BY = (
        ('NA','NA'),
        ('Mr A.','Mr A.'),
        ('Mr B','Mr B'),
        ('Mr C','Mr C'),
    )
    referred_by = models.CharField(max_length=20,choices=REFERRED_BY,default='NA')
    DESIGNATION = (
        ('NA','NA'),
        ('HR','HR'),
        ('Finance','Finance'),
        ('Administration','Administration'),
        ('Accounts','Accounts'),
        ('IT','IT'),
        ('Management','Management'),
        ('Marketing','Marketing'),
        ('Technical','Technical'),
        ('Purchase','Purchase'),
    )
    designation = models.CharField(max_length=20,choices=DESIGNATION,default='NA')

  
    department = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    mob_no = models.CharField(max_length=20)
    direct_no = models.CharField(max_length=20)
    notes = models.TextField()
    INSTITUTIONS = [
        ('KIIT','KIIT'),
        ('Others','Others'),
    ]
    institution = forms.ChoiceField(choices=INSTITUTIONS,widget=forms.RadioSelect)
    SCHOOL = (
         ('NA','NA'),
        ('School 1','School 1'),
        ('School 2','School 2'),
        ('School 3','School 3'),
    )
    school = models.CharField(max_length=20,choices=SCHOOL,default='NA')
    STREAM = (
          ('NA','NA'),
        ('Stream1.1','Stream1.1'),
        ('Stream 1.2','Stream 1.2'),
        ('Stream 1.3','Stream 1.3'),
    )
    stream = models.CharField(max_length=20,choices=STREAM,default='NA')
    yop = models.CharField(max_length=10)
    degree = models.CharField(max_length=50)
    MONTH = (
       ('month','month'),
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )
    month = models.CharField(max_length=20,choices=MONTH,default='NA')
    YEAR = (
         ('year','year'),
        ('2001','2001'),
        ('2002','2002'),
        ('2003','2003'),
        ('2004','2004'),
        ('2005','2005'),
        ('2006','2006'),
        ('2007','2007'),
        ('2008','2008'),
        ('2009','2009'),
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
    )
    year = models.CharField(max_length=20,choices=YEAR,default='NA')
    linkedin = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    OFFICE_DETAILS = (
       ('NA','NA'),
        ('Head Office','Head Office'),
        ('Factory / Plant','Factory / Plant'),
        ('Branch Office','Branch Office'),
        ('Project Site','Project Site'),
        ('Regional Office','Regional Office'),
        ('Registered Office','Registered Office'),
        ('Zonal Office','Zonal Office'),
    )
    Of_details = models.CharField(max_length=20,choices=OFFICE_DETAILS,default='NA')
    board_line_number = models.CharField(max_length=20)
    address = models.TextField(max_length=200)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    RECRUITMENT_CHOICES = [('KIIT','OTHERS')]

    def __Officedetail__(self):
        return self.name


