import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_group_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from fooodie.models import Photo, UserProfile, UserFactory, slugify
import random
import sys, os, glob, shutil
import factory  
import factory.django
import random

#Variable declaration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(os.path.join(BASE_DIR, 'media'))
population_photos=os.listdir(os.path.join(BASE_DIR,'population_photos'))
population_photos_old_path=os.path.join(BASE_DIR,'population_photos')

#Might be useful to create random data for users: stackoverflow.com/questions/33024510/populate-django-database



def create_user_profile():
    user = UserFactory() #User created with UserFactory() in models
    user.set_password("JoseIsAwesome") #Facts
    #Passowrd given to ALL random users so we can access them if necessary
    user.save()
    profile = UserProfile(user=user)
    profile.save()
    folder_path = os.path.join(MEDIA_DIR, str(profile.id))
    os.mkdir(folder_path)
    try:
        add_photo(profile)
        print("photo added "+str(profile.id))
    except:
        print("couldn't add photo")
        pass
    
def add_photo(userProfile):
    p = Photo(user=userProfile)
    p.votes = random.randint(0,10)
    p.name = photo
    photo = random.choice(population_photos)
    photo_old_path = os.path.join(population_photos_old_path,photo)
    photo_new_path = os.path.join(os.path.join(MEDIA_DIR,str(userProfile.id)),photo)
    p.photo = photo_new_path
    p.save()
    population_photos.remove(photo)
    shutil.move(photo_old_path,photo_new_path)
    

if __name__ == '__main__':
    print('Starting fooodie population script...')
    for i in range (0,20):
        create_user_profile()
        
"""     p = Photo(user=userProfile)
    p.votes = random.randint(0,10)
    photo = random.choice(population_photos)
    p.photo = photo
    p.save()
    population_photos.remove(photo)"
"""