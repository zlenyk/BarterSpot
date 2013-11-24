from django.test import TestCase
from BarterSpot.announcements.models import Announcement, Tag
from BarterSpot.users.models import BarterUser



class Announcement_AddTag_Test(TestCase):
    """Class testing adding Tag"""

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


class Announcement_TagCound_Test(TestCase):
    """Class testing popularity of Tags"""
    def setUp(self):
        self.testUser = BarterUser.createUser("testUser", "x", "x",
                                              "x@x.pl", "x", "x", False)

    def test_pure(self):
        tag1 = Tag.addTag("tag_1_1")
        tag2 = Tag.addTag("tag_1_2")

        self.assertEquals(tag1.getCount(), 0)
        self.assertEquals(tag2.getCount(), 0)

    def test_create_announcement(self):
        Announcement.createAnnouncement(self.testUser,
                                        "x",
                                        "x",
                                        tagsStrList=['t_2_1', 't_2_2', 't_2_3'])

        self.assertEquals(Tag.getTagByName('t_2_1').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_2_2').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_2_3').getCount(), 1)

        Announcement.createAnnouncement(self.testUser,
                                        "x",
                                        "x",
                                        tagsStrList=['t_2_1', 't_2_2', 't_2_4'])

        self.assertEquals(Tag.getTagByName('t_2_1').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_2_2').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_2_3').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_2_4').getCount(), 1)

    def test_add_tag(self):
        ann1 = Announcement.createAnnouncement(self.testUser,
                                               "x",
                                               "x",
                                                tagsStrList=['t_3_1', 't_3_2', 't_3_3'])

        self.assertEquals(Tag.getTagByName('t_3_1').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_2').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_3').getCount(), 1)

        Tag.addTag("t_3_4")
        Tag.addTag("t_3_5")
        Tag.addTag("t_3_6")

        self.assertEquals(Tag.getTagByName('t_3_4').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_3_5').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_3_6').getCount(), 0)

        ann1.addStrTag('t_3_1')
        ann1.addStrTag('t_3_2')
        ann1.addStrTag('t_3_3')
        ann1.addStrTag('t_3_4')
        ann1.addStrTag('t_3_5')
        ann1.addStrTag('t_3_6')

        self.assertEquals(Tag.getTagByName('t_3_1').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_2').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_3').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_4').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_5').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_3_6').getCount(), 1)

        ann2 = Announcement.createAnnouncement(self.testUser,
                                               "x",
                                               "x",
                                                tagsStrList=['t_3_1', 't_3_2', 't_3_7'])

        self.assertEquals(Tag.getTagByName('t_3_1').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_2').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_7').getCount(), 1)

        ann2.addStrTag('t_3_1')
        ann2.addStrTag('t_3_2')
        ann2.addStrTag('t_3_3')
        ann2.addStrTag('t_3_4')
        ann2.addStrTag('t_3_5')
        ann2.addStrTag('t_3_6')
        ann2.addStrTag('t_3_7')

        self.assertEquals(Tag.getTagByName('t_3_1').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_2').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_3').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_4').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_5').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_6').getCount(), 2)
        self.assertEquals(Tag.getTagByName('t_3_7').getCount(), 1)

    def test_remove_tag(self):
        ann1 = Announcement.createAnnouncement(self.testUser,
                                               "x",
                                               "x",
                                                tagsStrList=['t_4_1', 't_4_2', 't_4_3'])

        self.assertEquals(Tag.getTagByName('t_4_1').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_4_2').getCount(), 1)
        self.assertEquals(Tag.getTagByName('t_4_3').getCount(), 1)

        Tag.addTag("t_4_4")
        Tag.addTag("t_4_5")
        Tag.addTag("t_4_6")

        self.assertEquals(Tag.getTagByName('t_4_4').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_5').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_6').getCount(), 0)

        ann1.removeStrTag('t_4_1')
        ann1.removeStrTag('t_4_2')
        ann1.removeStrTag('t_4_3')
        ann1.removeStrTag('t_4_4')
        ann1.removeStrTag('t_4_5')
        ann1.removeStrTag('t_4_6')
        ann1.removeStrTag('t_4_7')

        self.assertEquals(Tag.getTagByName('t_4_1').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_2').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_3').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_4').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_5').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_6').getCount(), 0)
        self.assertEquals(Tag.getTagByName('t_4_7'), None)
