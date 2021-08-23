
import logging as logger
import pytest
from helpers import TestHelper
from user_management.use_case import UserAPIUseCases
from .test_data.user_test_data import users_data, delete_key

logger.basicConfig(level=logger.INFO)


class TestUsersAPI:
    @pytest.fixture(scope="class", autouse=True)
    def __suite_setup(self):
        logger.info(
            "{0} {1}: TestClass Setup {0}".format("*" * 10, self.__class__.__name__)
        )
        type(self).user_api_use_case = UserAPIUseCases()

    @pytest.fixture(scope="function", autouse=True)
    def __test_setup(self, request):
        logger.info("{0} Test Setup: {1} {0}".format("*" * 10, request.node.name))
        request.addfinalizer(self.__test_teardown)

    def __test_teardown(self):
        pass

    @pytest.mark.parametrize("username,score", users_data)
    def test_create_user(self, username, score):
        """
        Test user Creation. Get all users and verify creation
        """
        response = TestHelper.create_user(self.user_api_use_case, username, score)
        assert response["status"].lower() == "success", "Expected success"

        # get Users and check if created
        users = TestHelper.get_users(self.user_api_use_case)
        found = False
        for user in users:
            if user["username"] == username:
                found = True
                logger.info(f"User {username} found")
                assert user["score"] == score, "Score mismatch"
                break
        if not found:
            pytest.fail(f"User {username} not created")

    def test_get_users(self):
        """
        Get Users. verify response
        """
        users = TestHelper.get_users(self.user_api_use_case)
        assert users, "No users returned"

    @pytest.mark.parametrize("username,score", users_data)
    def test_update_user(self, username, score):
        """
        Test User Update. Get all users and verify user updation.
        """
        updated_score = score+10
        TestHelper.update_user(self.user_api_use_case, username, score=updated_score)
        users = TestHelper.get_users(self.user_api_use_case)
        assert users, "No users returned though expected"
        found = False
        for user in users:
            if user["username"] == username:
                found = True
                assert user["score"] == updated_score, f"score not updated for user {username}"
                break
        if not found:
            pytest.fail(f"User {username} not found")

    def test_delete_users(self):
        """
        Test User deletion
        """
        TestHelper.delete_user(self.user_api_use_case, delete_key)
        users = TestHelper.get_users(self.user_api_use_case)
        assert not users, "No all users deleted"
