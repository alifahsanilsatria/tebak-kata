import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','acak_kata.settings')

import django
# Import settings
django.setup()

from acak_kata_apps.models import Kata

def populate():
	file_kata = open("kata-indonesia.txt","r")
	daftar_kata = file_kata.read()
	daftar_kata = daftar_kata.split("\n")
	for kata in daftar_kata:
		kata_object = Kata(kata=kata)
		kata_object.save()

if __name__ == '__main__':
	populate()