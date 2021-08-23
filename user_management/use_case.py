from .requess import UsersRequested
from .events import UserCreated, UserUpdated, UserDeleted
from helpers.infra.user_client import UserAPIClient
from constants import USER_API_ROOT


class UserAPIUseCases:
    def __init__(self):
        self.user_api_client = UserAPIClient(USER_API_ROOT)

    def process_request(self, request_obj):
        if request_obj.__class__ == UsersRequested:
            return self.user_api_client.get_users()
        else:
            raise TypeError(
                f"Unknown UserAPIUseCases request object type: {request_obj.__class__}"
            )

    def process_command(self, event_obj):
        if event_obj.__class__ == UserCreated:
            return self.user_api_client.create_user(payload=event_obj.as_dict())
        elif event_obj.__class__ == UserUpdated:
            return self.user_api_client.update_user(payload=event_obj.as_dict())
        elif event_obj.__class__ == UserDeleted:
            return self.user_api_client.delete_user(delete_key=event_obj.delete_key)
        else:
            raise TypeError(
                f"Unknown UserAPIUseCases event type: {event_obj.__class__}"
            )