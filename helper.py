from faker import Faker

from data import TestAuthorizationData


class TestDataHelper:
    @staticmethod
    def modify_registration_body_request(key, value):
        body = TestAuthorizationData.REGISTRATION_USER_BODY.copy()
        body[key] = value

        return body

    @staticmethod
    def generate_registration_body():
        fake = Faker()

        return TestDataHelper.modify_registration_body_request('email', fake.email(domain='eatric.ru'))
