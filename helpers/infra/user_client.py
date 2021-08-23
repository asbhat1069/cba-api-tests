from .http_client import RESTClient


class UserUrls:
    def __init__(self, user_api_root):
        self.user_api_root = user_api_root

    def user_url(self):
        return f"{self.user_api_root}/v1/user"


class UserAPIClient:
    def __init__(self, user_api_root):
        self.urls = UserUrls(user_api_root)
        self.ses = RESTClient()

    def create_user(self, payload):
        headers = {"Content-Type": "application/json"}
        return self.ses.post(
            self.urls.user_url(), payload, headers=headers
        ).json()

    def get_users(self):
        headers = {"accept": "application/json"}
        return self.ses.get(
            self.urls.user_url(), headers=headers
        ).json()

    def update_user(self, payload):
        headers = {"Content-Type": "application/json"}
        return self.ses.put(
            self.urls.user_url(), payload, headers=headers
        )

    def delete_user(self, delete_key):
        headers = {"delete-key": delete_key}
        return self.ses.delete(
            self.urls.user_url(), headers=headers
        )
