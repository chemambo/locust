from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):   
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 20)
