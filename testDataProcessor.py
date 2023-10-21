import os
import unittest
from dataProcessor import read_json_file
from dataProcessor import avgAgeCountry
from dataProcessor import filter_by_age
import pandas as pd

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Angela Ward')
        self.assertEqual(data[1]['age'], 19)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")


    # Novos testes....

    def test_avg_json(self):
        avg = avgAgeCountry('users.json')
        self.assertEquals(avg,38.648)

    def test_avg_json_convert_in_days(self):
        avg = avgAgeCountry('users.json', True)
        self.assertEquals(avg,14106.52)


    def test_json_vazio(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "json_vazio.json")

        with self.assertRaises(ValueError):
            read_json_file(file_path)
       
    def test_idade_vazio(self):

        df = pd.read_json('idade_vazia.json')
        df_filtrado = df[df['age'].isna()]

        self.assertEquals(len(df_filtrado), 1)

    def test_campo_ausente(self):

        df = pd.read_json('campo_ausente.json')
        df_filtrado = df[df['country'].isna()]

        self.assertEquals(len(df_filtrado), 1)

    def test_filter(self):

        df = filter_by_age('users.json', 30)

        self.assertEquals(len(df), 712)
        

        









if __name__ == '__main__':
    unittest.main()