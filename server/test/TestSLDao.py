import sys

sys.path.append("../")  # append /server/
# print sys.path.__str__()
import unittest
import SLModels
import SLDao


class TestSLDao(unittest.TestCase):
        def setUp(self):
                SLModels.re_populate_model()
                self.slDao = SLDao.SLDao()

        def test_find_all_agencies(self):
                agencies = self.slDao.find_all_agencies()
                self.assertEqual(len(agencies), 4)
                self.assertEqual(agencies[0].name, 'Havas worldwide')
                self.assertTrue('digital agency' in agencies[1].description)
                self.assertTrue('Brand activation' in agencies[2].tags)
                self.assertEqual(agencies[3].grade, SLModels.GRADE_PADAWAN)

                self.slDao.close()

        def test_add_agency(self):
                agency = self.slDao.add_agency("Test", "Desc", SLModels.GRADE_JEDI, "Tags")
                self.assertIsNotNone(agency.id, "None!")
                self.assertEqual(agency.id, 5)
                self.assertEqual(len(self.slDao.find_all_agencies()), 5)
                self.slDao.close()


if __name__ == '__main__':
        unittest.main()
