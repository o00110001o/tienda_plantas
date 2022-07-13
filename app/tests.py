from django.test import TestCase

# Create your tests here.
import requests
response = requests.get('https://rickandmortyapi.com/')
print(response['characters'])