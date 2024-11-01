from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag

TASK_URL = reverse("todo:index")
TAG_URL = reverse("todo:tags-list")


class PublicViewsTest(TestCase):
    def test_login_required(self):
        for url in [TASK_URL, TAG_URL]:
            res = self.client.get(url)
            self.assertNotEqual(res.status_code, 200)


class PrivateViewsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_task(self):
        Task.objects.create(content="test", done=False)
        Task.objects.create(content="test1", done=True)
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["task_list"]),
                         list(tasks))
        self.assertTemplateUsed(response,
                                "todo/index.html")

    def test_create_task(self):
        form_data = {
            "content": "test",
            "done": False
        }
        self.client.post(reverse("todo:task-create"), form_data)
        task = Task.objects.get(content="test")
        self.assertEqual(task.content, form_data["content"])
        self.assertEqual(task.done, form_data["done"])


    def test_retrieve_tag(self):
        Tag.objects.create(name="test")
        Tag.objects.create(name="test2")
        response = self.client.get(TAG_URL)
        self.assertEqual(response.status_code, 200)
        tags = Tag.objects.all()
        self.assertEqual(list(response.context["tag_list"]),
                         list(tags))
        self.assertTemplateUsed(response,
                                "todo/tag_list.html")

    def test_create_tag(self):
        form_data = {
            "name": "test",
        }
        self.client.post(reverse("todo:tag-create"), form_data)
        tag = Tag.objects.get(name="test")
        self.assertEqual(tag.name, form_data["name"])
