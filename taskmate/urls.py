
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as tviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tviews.index, name='index'),
    path ('todolist/',include('todolist_app.urls')),
    path('primary/',tviews.primary, name='primary'),
    path('secondary/',tviews.secondary, name='secondary'),
    path('srsec/',tviews.srsec, name='srsec'),
    path('csxii/',tviews.csxii, name='csxii'),
    path('hindixii/',tviews.hindixii, name='hindixii'),
    path('engxii/',tviews.engxii, name='engxii'),
    path('mathxii/',tviews.mathxii, name='mathxii'),
    path('phyxii/',tviews.phyxii, name='phyxii'),
    path('chexii/',tviews.chexii, name='chexii'),
    path('bioxii/',tviews.bioxii, name='bioxii'),
    path('csxi/',tviews.csxi, name='csxi'),
    path('hindixi/',tviews.hindixi, name='hindixi'),
    
]
