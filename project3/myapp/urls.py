from django.urls import path
from . import views
urlpatterns=[
    path('dinnerreg/',views.dinnerreg,name="dinnaerreg"),
    path('homepage/',views.homepage,name="homepage"),
    path('party/',views.party,name="party"),
path('partys/<name>',views.partys,name="partys"),
    path('partyd/<name>', views.partyd, name="partyd"),
    path('portfolio/<name>',views.portfolio,name="portfolio"),
path('portfoliow/<name>',views.portfoliow,name="portfoliow"),
    path('partyreg1/<dname>/<vname>', views.partyreg1, name="partyreg1"),

path('dates/',views.dates,name="dates"),
path('datesc/<name>',views.datesc,name="datesc"),
path('familydinner/',views.familydinner,name="familydinner"),
path('familydinnerc/<name>',views.familydinnerc,name="familydinnerc"),
path('wedding/',views.wedding,name="wedding"),
path('weddings/<name>',views.weddings,name="weddings"),
path('weddingd/<name>',views.weddingd,name="weddingd"),
path('weddingreg/<dname>/<vname>',views.weddingreg,name="weddingreg"),

path('contactus/',views.contactus,name="contactus"),
path('details/<name>',views.details,name="details"),
path('detailsd/<name>',views.detailsd,name="detailsd"),

path('gallery/',views.gallery,name="gallery"),
path('galleryreg/',views.galleryreg,name="galleryreg"),


path('decor/', views.decor, name='decor'),

path('aboutus/',views.aboutus,name="aboutus"),

path('venue/', views.venue, name='venue'),


]
