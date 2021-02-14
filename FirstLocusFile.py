from locust import TaskSet, task, User, between, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_Men_Products(self):
        print("Searching men products")

    @task
    def serach_Kids_Product(self):
        print("Searching kids product")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]



