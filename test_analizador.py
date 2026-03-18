import unittest
import tempfile
import os
from analizador import contar_lineas, contar_palabras, contar_caracteres, analizar_archivo

class TestAnalizador(unittest.TestCase):

    def setUp(self):
        # Crear archivo temporal con tres líneas, cada una con dos palabras
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
        self.test_file.write("línea uno\nlínea dos\nlínea tres")
        self.test_file.close()
        self.test_filename = self.test_file.name

    def tearDown(self):
        os.unlink(self.test_filename)

    def test_contar_lineas(self):
        contenido = "a\nb\nc"
        self.assertEqual(contar_lineas(contenido), 3)

    def test_contar_palabras(self):
        contenido = "hola mundo desde python"
        self.assertEqual(contar_palabras(contenido), 4)

    def test_contar_caracteres(self):
        contenido = "12345"
        self.assertEqual(contar_caracteres(contenido), 5)

    def test_analizar_archivo_con_salida(self):
        # Probar que genera archivo de salida correctamente
        salida = tempfile.NamedTemporaryFile(mode='r', delete=False, encoding='utf-8')
        salida.close()
        analizar_archivo(self.test_filename, salida.name)

        with open(salida.name, 'r', encoding='utf-8') as f:
            resultado = f.read()

        # Verificar que el contenido del archivo de salida sea el esperado
        self.assertIn("Líneas: 3", resultado)
        self.assertIn("Palabras: 6", resultado)  # Ahora esperamos 6 palabras
        self.assertIn("Caracteres: 30", resultado)  # El archivo tiene 30 caracteres (contando saltos de línea)
        os.unlink(salida.name)

    def test_analizar_archivo_sin_salida(self):
        # Verificar que no lanza excepción al imprimir (archivo existente)
        try:
            analizar_archivo(self.test_filename)
        except Exception as e:
            self.fail(f"analizar_archivo lanzó excepción: {e}")

    def test_archivo_no_existe(self):
        # Ahora la función debe lanzar FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            analizar_archivo("no_existe.txt")