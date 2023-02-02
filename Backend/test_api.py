import unittest
from main import create_app
from config import TestConfig
from exts import db
import auth

#helps with declaration of variables we will need
class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)

            db.create_all()

    def test_hello_world(self):
        hello_response = self.client.get("/photos/hello")

        json = hello_response.json

        # print(json)
        self.assertEqual(json, {"message": "Hello World"})

    def test_signup(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "name": "user",
                "username": "testuser",
                "email": "testuser@test.com",
                #"password": "password",
            },
        )

        status_code = signup_response.status_code

        self.assertEqual(status_code, 201)

    def test_login(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "name": "user",
                "username": "testuser",
                "email": "testuser@test.com",
                #"password": "password",
            },
        )

        login_response = self.client.post(
            "auth/login", json={"username": "testuser", "email": "testuser@test.com"}
        )

        status_code = login_response.status_code

        json = login_response.json

        # print(json)

        self.assertEqual(status_code, 200)

    def test_get_all_users(self):
        """TEST GETTING ALL users"""
        response = self.client.get("/users/users")

        # print(response.json)

        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_get_one_user(self):
        id = 1
        response = self.client.get(f"/users/users/{id}")

        status_code = response.status_code
        # print(status_code)

        self.assertEqual(status_code, 404)

    def test_create_user(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "name": "user",
                "username": "testuser",
                "email": "testuser@test.com",
                #"password": "password",
            },
        )

        login_response = self.client.post(
            "auth/login", json={"username": "testuser", "email": "testuser@test.com"}
        )

        access_token = login_response.json["access_token"]

        create_user_response = self.client.post(
            "/users/users",
            json={"name": "Test Name", "email": "Test.email@address"},
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = create_user_response.status_code

        # print(create_user_response.json)

        self.assertEqual(status_code, 201)

    def test_update_user(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "name": "user",
                "username": "testuser",
                "email": "testuser@test.com",
                #"password": "password",
            },
        )

        login_response = self.client.post(
            "auth/login", json={"username": "testuser", "email": "testuser@test.com"}
        )

        access_token = login_response.json["access_token"]

        create_user_response = self.client.post(
            "/users/users",
            json={"name": "Test Name", "email": "Test.email@address"},
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = create_user_response.status_code

        id = 1

        update_response = self.client.put(
            f"users/users/{id}",
            json={
                "name": "Test Name", 
                "email": "Test.email@address"
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = update_response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_user(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "name": "user",
                "username": "testuser",
                "email": "testuser@test.com",
               # "password": "password",
            },
        )

        login_response = self.client.post(
            "auth/login", json={"username": "testuser", "email": "testuser@test.com"}
        )

        access_token = login_response.json["access_token"]

        create_user_response = self.client.post(
            "/users/users",
            json={"name": "Test Name", "email": "Test.email@address"},
            headers={"Authorization": f"Bearer {access_token}"},
        )

        id = 1
        delete_response = self.client.delete(
            f"/users/users/{id}", headers={"Authorization": f"Bearer {access_token}"}
        )

        status_code = delete_response.status_code

        print(delete_response.json)

        self.assertEqual(status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
    
    <Photos />
        <Login />
        <LandingPage />
        <Route exact path="/" component={Home} />
        <Route path="/users/:id" component={Users} />