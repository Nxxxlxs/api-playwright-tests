from api.clients.base_client import BaseClient


class UsersClient(BaseClient):
    
    def list_users(self):
        return self.get("/users")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")
    
    def create_user(self, data):
        return self.post("/users", data)