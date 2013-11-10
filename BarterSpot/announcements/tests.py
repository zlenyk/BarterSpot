from django.test import TestCase
from BarterSpot.announcements.models import Announcement, Tag


class AnnouncementTest(TestCase):
    """Class testing Tag"""

    def setUp(self):
        tag1 = Tag(name="tag1")
        tag1.save()

        tag2 = Tag(name="tag2")
        tag2.save()

        tag3 = Tag(name="tag3")
        tag3.save()

    def test_tagExists(self):
        self.assertTrue(Tag.tagExists("tag1"))
        self.assertTrue(Tag.tagExists("tag2"))
        self.assertTrue(Tag.tagExists("tag3"))

        self.assertFalse(Tag.tagExists("xDxD"))
        self.assertFalse(Tag.tagExists("no_such_tag"))
        self.assertFalse(Tag.tagExists(""))

    def test_addTag(self):
        Tag.addTag("addedTag1")
        Tag.addTag("addedTag2")
        Tag.addTag("addedTag3")

        self.assertTrue(Tag.tagExists("addedTag1"))
        self.assertTrue(Tag.tagExists("addedTag2"))
        self.assertTrue(Tag.tagExists("addedTag3"))

        self.assertTrue(Tag.tagExists("tag3"))
        self.assertFalse(Tag.tagExists("xDxD"))
        self.assertFalse(Tag.tagExists("no_such_tag"))

    def test_addTagsList(self):
        tagsStrList = ["list_tag1", "list_tag2", "list_tag3", "list_tag4"]
        Tag.addTagsList(tagsStrList)

        self.assertTrue(Tag.tagExists("list_tag1"))
        self.assertTrue(Tag.tagExists("list_tag2"))
        self.assertTrue(Tag.tagExists("list_tag3"))
        self.assertTrue(Tag.tagExists("list_tag4"))

        self.assertTrue(Tag.tagExists("tag3"))
        self.assertFalse(Tag.tagExists("xDxD"))
        self.assertFalse(Tag.tagExists("no_such_tag"))
