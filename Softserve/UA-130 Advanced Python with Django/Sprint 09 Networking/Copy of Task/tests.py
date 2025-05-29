import json
import multiprocessing
import unittest
import time

import requests

from main import run

DOMAIN = "localhost"
PORT = 8765

HOST = f"http://{DOMAIN}:{PORT}"

process = multiprocessing.Process(target=run, kwargs={"host": DOMAIN, "port": PORT})


def setUpModule():
    process.start()
    time.sleep(3)


def tearDownModule():
    process.terminate()


class UserTestGET(unittest.TestCase):
    def setUp(self):
        requests.get(f"{HOST}/reset")

    def test_get_all_users(self):
        response = requests.get(f"{HOST}/users")
        expected_status_code = 200
        expected_data = [
            {
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345"
            }
        ]

        self.assertEqual(expected_status_code, response.status_code)
        self.assertListEqual(expected_data, response.json())

    def test_get_user_by_username(self):
        username = "theUser"
        response = requests.get(f"{HOST}/user/{username}")
        expected_status_code = 200
        expected_data = {
            "id": 1,
            "username": "theUser",
            "firstName": "John",
            "lastName": "James",
            "email": "john@email.com",
            "password": "12345"
        }

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_get_user_by_username_not_found(self):
        username = "User_not_found"
        response = requests.get(f"{HOST}/user/{username}")
        expected_status_code = 400
        expected_data = {
            "error": "User not found"
        }

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())


class UserTestPOST(unittest.TestCase):
    def setUp(self):
        requests.get(f"{HOST}/reset")

    def test_create_user(self):
        data = {
            "id": 2,
            "username": "theUser",
            "firstName": "John",
            "lastName": "James",
            "email": "john@email.com",
            "password": "12345"
        }
        response = requests.post(f"{HOST}/user", data=json.dumps(data))

        expected_status_code = 201
        expected_data = data

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_create_user_duplicate_id(self):
        data = {
            "id": 1,
            "username": "theUser",
            "firstName": "John",
            "lastName": "James",
            "email": "john@email.com",
            "password": "12345"
        }
        response = requests.post(f"{HOST}/user", data=json.dumps(data))

        expected_status_code = 400
        expected_data = {}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_create_user_not_valid_data(self):
        data = {
            "lastName": "James",
            "email": "john@email.com",
            "password": "12345"
        }
        response = requests.post(f"{HOST}/user", data=json.dumps(data))

        expected_status_code = 400
        expected_data = {}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_create_users(self):
        data = [
            {
                "id": 2,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345"
            },
            {
                "id": 3,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john2@email.com",
                "password": "12345"
            }

        ]
        response = requests.post(f"{HOST}/user/createWithList", data=json.dumps(data))

        expected_status_code = 201
        expected_data = data

        self.assertEqual(expected_status_code, response.status_code)
        self.assertListEqual(expected_data, response.json())

    def test_create_users_duplicate_id(self):
        data = [
            {
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345"
            },
            {
                "id": 2,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john2@email.com",
                "password": "12345"
            }

        ]
        response = requests.post(f"{HOST}/user/createWithList", data=json.dumps(data))

        expected_status_code = 400
        expected_data = {}

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_create_users_not_valid_data(self):
        data = [
            {
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345"
            },
            {
                "id": 2,
                "username": "theUser2",
                "firstName": "John2",
                "lastName": "James2"
            },
            {
                "id": 3,
                "username": "theUser3",
                "firstName": "John3",
                "lastName": "James3"
            }

        ]
        response = requests.post(f"{HOST}/user/createWithList", data=json.dumps(data))

        expected_status_code = 400
        expected_data = {}
        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())


class UserTestPUT(unittest.TestCase):
    def setUp(self):
        requests.get(f"{HOST}/reset")

    def test_update_user(self):
        data = {
            "username": "newtheUser",
            "firstName": "newJohn",
            "lastName": "newJames",
            "email": "john@email.com",
            "password": "new12345"
        }
        response = requests.put(f"{HOST}/user/1", data=json.dumps(data))
        expected_status_code = 200
        expected_data = dict(**data, id=1)

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_update_user_not_valid_data(self):
        data = {
            "firstName": "newJohn",
            "lastName": "newJames",
            "email": "john@email.com",
            "password": "new12345"
        }
        response = requests.put(f"{HOST}/user/1", data=json.dumps(data))
        expected_status_code = 400
        expected_data = {
            "error": "not valid request data"
        }

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_update_user_not_found(self):
        data = {
            "username": "newtheUser",
            "firstName": "newJohn",
            "lastName": "newJames",
            "email": "john@email.com",
            "password": "new12345"
        }
        response = requests.put(f"{HOST}/user/999", data=json.dumps(data))
        expected_status_code = 404
        expected_data = {
            "error": "User not found"
        }

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())


class UserTestDELETE(unittest.TestCase):
    def setUp(self):
        requests.get(f"{HOST}/reset")

    def test_delete_by_id(self):
        id = 1
        response = requests.delete(f"{HOST}/user/{id}")
        expected_status_code = 200
        expected_data = {}

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())

    def test_delete_by_not_valid_id(self):
        id = 22
        response = requests.delete(f"{HOST}/user/{id}")
        expected_status_code = 404
        expected_data = {
            "error": "User not found"
        }

        self.assertEqual(expected_status_code, response.status_code)
        self.assertDictEqual(expected_data, response.json())


if __name__ == '__main__':
    unittest.main()
