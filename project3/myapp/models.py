from django.db import models

# Create your models here.
class dinner(models.Model):
    hname=models.CharField(max_length=255,help_text="resturant name")
    hadd=models.CharField(max_length=255,help_text="address of resturant")
    hpp=models.CharField(max_length=255,help_text="price per person")
    himage1=models.ImageField(upload_to='hreg',blank=True)
    himage2=models.ImageField(upload_to='hreg',blank=True)
    cusine1 = {('select_cusine', '--selectCusine--'),
            ('northindian', 'northindian'),
            ('none', 'none'),
            ('southindian', 'southindian'),
              ('chinese', 'chinese'),
              ('fastfood', 'fastfood'),
              ('italian', 'italian'),
              ('bakery','bakery'),
            }

    cusine1 = models.CharField(max_length=255, help_text="enter cusine", default='select_cusine', choices=cusine1)
    cusine2 = {('select_cusine', '--selectCusine--'),
               ('northindian', 'northindian'),
               ('none', 'none'),
               ('southindian', 'southindian'),
               ('chinese', 'chinese'),
               ('fastfood', 'fastfood'),
               ('italian', 'italian'),
               ('bakery', 'bakery'),
               }

    cusine2 = models.CharField(max_length=255, help_text="enter cusine", default='select_cusine', choices=cusine2)
    cusine3 = {('select_cusine', '--selectCusine--'),
               ('northindian', 'northindian'),
               ('southindian', 'southindian'),
               ('none', 'none'),
               ('chinese', 'chinese'),
               ('fastfood', 'fastfood'),
               ('italian', 'italian'),
               ('bakery', 'bakery'),
               }

    cusine3 = models.CharField(max_length=255, help_text="enter cusine", default='select_cusine', choices=cusine3)
    cusine4 = {('select_cusine', '--selectCusine--'),
               ('northindian', 'northindian'),
               ('none', 'none'),
               ('southindian', 'southindian'),
               ('chinese', 'chinese'),
               ('fastfood', 'fastfood'),
               ('italian', 'italian'),
               ('bakery', 'bakery'),
               }
    cusine4 = models.CharField(max_length=255, help_text="enter cusine", default='select_cusine', choices=cusine4)
    drinks = {('select', '--select--'),
               ('yes', 'yes'),
               ('no', 'no'),
               }

    drinks = models.CharField(max_length=255, help_text="enter yes or no", default='select1', choices=drinks)
    typef = {('select_type', '--selecttype--'),
               ('veg', 'veg'),
               ('non-veg', 'non-veg'),
               ('both', 'both'),
           }

    typef = models.CharField(max_length=255, help_text="enter cusine", default='select_type', choices=typef)

    class Meta:
        db_table = "hreg"
        ordering = ('hpp',)
        verbose_name = 'hreg'
        verbose_name_plural = 'hregs'

    def __str__(self):
        return '()'.format(self.hname)+''+ self.cusine1 + '' +self.cusine2 +''+self.cusine3 +''+self.cusine4+''+self.hname

class book(models.Model):
    phone=models.CharField(max_length=255,help_text="enter phone no")
    hname = models.CharField(max_length=255, help_text="resturant name")
    date=models.DateTimeField(help_text="enter date")
    person= models.CharField(max_length=255,help_text="no of persons")
    class Meta:
        db_table="booking"
        ordering=('hname',)
        verbose_name='booking'
        verbose_name_plural='bookings'
    def __str__(self):
        return '()'.format(self.phone)+''+self.phone
class usercom(models.Model):
    hname=models.CharField(max_length=255,help_text="resturant name")
    pname=models.CharField(max_length=255,help_text="person name")

    comments=models.CharField(max_length=255,help_text="comments")
    class Meta:
        db_table="comments"
        ordering=('pname',)
        verbose_name='comments'
        verbose_name_plural='commentss'
    def __str__(self):
         return '()'.format(self.hname)+''+self.hname




class decorModel(models.Model):
    decorname=models.CharField(max_length=255,help_text="enter decor name",unique=True)
    image1=models.ImageField(upload_to='decor',blank=True)


    class Meta:
        db_table="decor"
        ordering=('decorname',)
        verbose_name='decor'
        verbose_name_plural='decors'

    def __str__(self):
        return '()'.format(self.decorname)+''+self.decorname




class venueModel(models.Model):
    venuename=models.CharField(max_length=255,help_text="enter venue name",unique=True)
    image1=models.ImageField(upload_to='venue',blank=True)
    image2 = models.ImageField(upload_to='venue', blank=True)
    image3 = models.ImageField(upload_to='venue', blank=True)
    image4 = models.ImageField(upload_to='venue', blank=True)
    image5 = models.ImageField(upload_to='venue', blank=True)
    image6 = models.ImageField(upload_to='venue', blank=True)
    city = {('select_city', '--selectcity--'),
             ('Jaipur', 'JAIPUR'),
             ('Delhi', 'delhi'),
             ('Mumbai', 'mumbai'),
            ('Udaipur', 'udaipar'),
            ('Jodhpur', 'jodhpur'),
            ('Nagpur', 'nagpur'),
            ('Chennai', 'chennai'),
            ('Banglore', 'banglore'),
             }

    city= models.CharField(max_length=255, help_text="enter city", default='select_city', choices=city)

    class Meta:
        db_table="venue"
        ordering=('venuename',)
        verbose_name='venue'
        verbose_name_plural='venues'

    def __str__(self):
        return '()'.format(self.venuename)+''+self.city+''+self.venuename
class partyreg(models.Model):

     pname=models.CharField(max_length=255,help_text="user name")

     pemail=models.CharField(max_length=255,help_text="users email")
     phone=models.CharField(max_length=255,help_text="enter phone no")
     pdate=models.DateField(help_text="events date")
     ptype=models.CharField(max_length=255,help_text="pd")
     pguest=models.CharField(max_length=255,help_text="no of guest")
     venuename=models.CharField(max_length=255,help_text="your venue")
     decorname=models.CharField(max_length=255,help_text="your decor")
     photo=models.CharField(max_length=255,help_text="photographer")
     ds=models.CharField(max_length=255,help_text="dj & sound")
     class Meta:
         db_table="party"
         ordering=('pname',)
         verbose_name='party'
         verbose_name_plural='parties'
     def __str__(self):
         return '()'.format(self.pname)+''+self.phone
class gallerym(models.Model):
      image=models.ImageField(upload_to='gallery', blank=True)
      group=models.CharField(max_length=255,help_text="name of group")
      work=models.CharField(max_length=255,help_text="work shown in image")
      class Meta:
          db_table="gallery"
          ordering=('work',)
          verbose_name='gallery'
          verbose_name_plural='galleries'
      def __str__(self):
         return '()'.format(self.work)