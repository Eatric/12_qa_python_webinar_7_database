from data import TestAuthorizationData
from helper import TestDataHelper
from shop_api import ShopApi


class TestAuthorizationEndpoint:

    def test_successful_registration(self, database):
        registration_body = TestDataHelper.generate_registration_body()
        registration_request = ShopApi.registration(registration_body)
        user = database.get_user(registration_body['email'])

        assert registration_request.status_code == 200 and len(user) == 1 and user[0][0] == registration_body['email']

    def test_successful_login(self):
        login_request = ShopApi.login(TestAuthorizationData.LOGIN_USER_BODY)

        assert login_request.status_code == 200

    def test_failed_registration_existed_email_error_expected(self):
        body = TestDataHelper.generate_registration_body()

        ShopApi.registration(body)

        registration_request = ShopApi.registration(body)

        assert registration_request.status_code == 400 and registration_request.json()['detail'] == ('The user with '
                                                                                                     'this email '
                                                                                                     'already exists '
                                                                                                     'in the system')
