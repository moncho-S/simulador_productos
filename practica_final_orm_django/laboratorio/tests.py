from django.test import TestCase

# Create your tests here.
from django.test import TestCase 
from django.test import SimpleTestCase 
from django.urls import reverse 
from .models import *

class LaboratorioTests(TestCase): 
    @classmethod 
    def setUpTestData(cls): 
        cls.labo = Laboratorio.objects.create(nombre="testname", 
                                               ciudad='testcity', 
                                               pais='country@test.com')
    def test_model_content(self): 
        self.assertEqual(self.labo.nombre, "testname") 
        self.assertEqual(self.labo.ciudad, "testcity") 
        self.assertEqual(self.labo.pais, "country@test.com") 
    
    def test_url_exists_at_correct_location(self): 
        response = self.client.get("/laboratorio/") 
        self.assertEqual(response.status_code, 200) 

    def test_homepage(self): 
        response = self.client.get(reverse("mostrar-lab")) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "mostrar.html") 
        self.assertContains(response, "Información de Laboratorios")