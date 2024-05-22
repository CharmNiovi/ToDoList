from django.test import TestCase
from django.urls import reverse

from todo_list.models import Tag


class TagListViewTestCase(TestCase):
    def test_get(self):
        Tag.objects.create(name="test")
        Tag.objects.create(name="test1")
        response = self.client.get(reverse("todo_list:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["object_list"].count(),
            2
        )


class TagCreateViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse("todo_list:tag-create"))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(
            reverse("todo_list:tag-create"),
            data={"name": "test"}
        )
        self.assertEqual(Tag.objects.count(), 1)


class TagUpdateViewTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test")
    def test_get(self):
        response = self.client.get(
            reverse(
                "todo_list:tag-update",
                kwargs={"pk": self.tag.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(
            reverse(
                "todo_list:tag-update",
                kwargs={"pk": self.tag.pk}
            ),
            data={
                "name": "test1"
            }
        )
        self.assertEqual(Tag.objects.first().name, "test1")


class TagDeleteViewTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test")

    def test_get(self):
        response = self.client.get(
            reverse(
                "todo_list:tag-delete",
                kwargs={"pk": self.tag.pk}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.post(
            reverse(
                "todo_list:tag-delete",
                kwargs={"pk": self.tag.pk}
            )
        )
        self.assertEqual(Tag.objects.count(), 0)
