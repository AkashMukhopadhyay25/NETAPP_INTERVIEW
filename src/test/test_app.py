import requests
import unittest


class TestGetVolumes(unittest.TestCase):
    API = "http://127.0.0.1:5000/getVolume"
    INVALID_API = "http://127.0.0.1:5000/getVolume123"

    def test_get_all_records(self):
        r = requests.get(TestGetVolumes.API)
        data = r.json()
        # Checks the StatusCode
        self.assertEqual(r.status_code, 200)
        # Checks the total Number of Records Outputted
        self.assertEqual(data["Total Number of Volumes"], 3)
        # Checks the total Number of Fields Outputted
        self.assertEqual(len(data["Volumes"][0]), 4)

    def test_invalid_request_url(self):
        r = requests.get(TestGetVolumes.INVALID_API)
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()
