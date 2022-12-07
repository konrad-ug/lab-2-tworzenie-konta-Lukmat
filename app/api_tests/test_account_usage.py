import unittest
import requests

class TestAccountUsage(unittest.TestCase):
    body = {
        "name": "Dariusz",
        "lastname": "Januszewski",
        "pesel": "02310634908"
    }

    body2 = {
            "name": "Janusz",
            "lastname": "Dariuszewski",
        }

    url = "http://127.0.0.1:5000"

    def test_1_create_account(self):
        response = requests.post(
            self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(response.status_code, 201)

    def test_2_find_account(self):
        response = requests.get(self.url + "/konta/konto/02310634908")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.body['name'])
        self.assertEqual(response.json()['lastname'], self.body['lastname'])
        self.assertEqual(response.json()['pesel'], self.body['pesel'])

    def test_3_update_account(self):
        response = requests.put(self.url + "/konta/update_konto/02310634908", json=self.body2)
        self.assertEqual(response.status_code, 200)

    def test_4_find_account(self):
        response = requests.get(self.url + "/konta/konto/02310634908")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.body2['name'])
        self.assertEqual(response.json()['lastname'], self.body2['lastname'])

    def test_5_find_non_existing_account(self):
        response = requests.get(self.url + "/konta/konto/03395246235")
        self.assertEqual(response.status_code, 404)

    def test_6_delete_account(self):
        response = requests.delete(self.url + "/konta/delete_konto/02310634908")
        self.assertEqual(response.status_code, 200)