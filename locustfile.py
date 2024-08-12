from locust import HttpUser, task

class UserTesting(HttpUser):
    @task
    def testing(self):
        self.client.get("/api/jobs/")