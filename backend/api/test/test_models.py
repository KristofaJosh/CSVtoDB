from django.test import TestCase
from ..models import ZenoModel


class TestModels(TestCase):

    def test_string_representation(self):
        csv_row = ZenoModel(csv_id='test id',
                            csv_duration='test duration',
                            csv_temperature='test temp',
                            csv_timestamp='test timestamp')

        self.assertEqual(str(csv_row), csv_row.csv_id)
