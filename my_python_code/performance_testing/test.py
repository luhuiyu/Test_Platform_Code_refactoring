from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
  #  @task(1)
  #  def test_post(self):
  #      self.client.get("/report")
    @task(1)
    def test_get(self):
        self.client.get("/rest_api/rest_api_tset_of_class")
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10  #最小等待 ms
    max_wait = 50
    stop_timeout = 100
    weight = 1   #权重
    host = "http://47.94.10.221:8000"

