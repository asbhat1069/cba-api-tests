from user_management.requess import UsersRequested
from user_management.events import UserCreated,UserUpdated,UserDeleted


class UserAPIHelper:
    @classmethod
    def create_user(cls, use_case, username, score=0):
        user_created = UserCreated(username, score)
        return use_case.process_command(user_created)

    @classmethod
    def get_users(cls, use_case):
        users_rquested = UsersRequested()
        return use_case.process_request(users_rquested)

    @classmethod
    def update_user(cls, use_case, username, score=0):
        user_updated = UserUpdated(username, score)
        use_case.process_command(user_updated)

    @classmethod
    def delete_user(cls, use_case, delete_key):
        user_deleted = UserDeleted(delete_key=delete_key)
        use_case.process_command(user_deleted)

