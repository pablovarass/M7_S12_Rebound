from django.test import TestCase
from django.urls import reverse
from .models import Fabrica, Producto

class StaticContentTests(TestCase):
    
    def setUp(self):
        # Crear una fábrica y un producto de prueba
        self.fabrica = Fabrica.objects.create(nombre='Fabrica', pais='Chile')
        self.producto = Producto.objects.create(
            nombre='Producto',
            precio=2000,
            descripcion='descripcion',
            fecha_vencimiento='2024-12-02',
            fabrica_id=self.fabrica.id
        )

    
    def test_1_url_crear_producto_status(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertEqual(response.status_code, 200)
        print("Test 1: Verificar que la URL '/producto/crear_producto/' devuelve un código de estado 200 OK.")

    
    def test_2_url_reverso_crear_producto(self):
        url = reverse('crear_producto')
        self.assertEqual(url, '/producto/crear_producto/')
        print("Test 2: Verificar el enlace reverso 'crear_producto' OK.")

    
    def test_3_plantilla_crear_producto(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertTemplateUsed(response, 'crear_producto.html')
        print("Test 3: Verificar nombre correcto de la plantilla 'crear_producto.html' OK.")

    
    def test_4_contenido_plantilla_crear_producto(self):
        response = self.client.get(reverse('crear_producto'))
        self.assertContains(response, '<h2 class="text-center">Crear Producto</h2>')
        print("Test 4: Verificar contenido específico en la plantilla 'crear_producto' OK.")

