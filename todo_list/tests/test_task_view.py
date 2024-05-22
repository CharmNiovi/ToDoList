import datetime

from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task, Tag


class TaskListViewTestCase(TestCase):
    def test_get(self):
        done_task = Task.objects.create(
            content="task1",
            done=True
        )
        Task.objects.create(
            content="task3",
            deadline=datetime.datetime(2020, 2, 1)
        )
        Task.objects.create(
            content="task2",
            deadline=datetime.datetime(2020, 1, 1)
        )

        response = self.client.get(reverse("todo_list:task-list"))
        object_list = response.context_data["object_list"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(object_list.count(), 3)
        self.assertEqual(object_list.last(), done_task)
        self.assertEqual(object_list.first().content, "task2")


class TaskCreateViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse("todo_list:task-create"))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tag = Tag.objects.create(name="test")

        self.client.post(
            reverse("todo_list:task-create"),
            data={"content": "test", "tags": [tag.pk]}
        )

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().content, "test")


class TaskUpdateViewTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="test")

    def test_get(self):
        response = self.client.get(reverse(
            "todo_list:task-update", kwargs={"pk": self.task.pk}
        ))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tag = Tag.objects.create(name="test")
        self.client.post(
            reverse(
                "todo_list:task-update",
                kwargs={"pk": self.task.pk}
            ),
            data={"content": "test1", "tags": [tag.pk]}
        )
        self.assertEqual(Task.objects.first().content, "test1")


class TaskDeleteViewTestView(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="test")

    def test_get(self):
        response = self.client.get(reverse(
            "todo_list:task-delete", kwargs={"pk": self.task.pk}
        ))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(reverse(
            "todo_list:task-delete", kwargs={"pk": self.task.pk}
        ))
        self.assertEqual(Task.objects.count(), 0)


class TaskSwitchToCompletedViewTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="test")

    def test_get(self):
        self.client.get(reverse(
            "todo_list:task-switch-to-done", kwargs={"pk": self.task.pk}
        ))
        self.assertTrue(Task.objects.first().done)


class TaskSwitchToUncompletedViewTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="test", done=True)

    def test_get(self):
        self.client.get(reverse(
            "todo_list:task-switch-to-undone", kwargs={"pk": self.task.pk}
        ))
        self.assertFalse(Task.objects.first().done)