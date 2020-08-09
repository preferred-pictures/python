import urllib.request
import unittest
import preferred_pictures
import os
import re
import http


class RedirectFilter(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        return None  # do not redirect.


class TestIntegration(unittest.TestCase):
    def test_create_url(self):
        pp = preferred_pictures.Client("testidentity", "testsecret")
        url = pp.create_choose_url(["1", "2", "3"], "test-tourney")
        self.assertTrue(url.startswith("https://api.preferred-pictures.com"))

    def test_raises_error_with_no_choices(self):
        pp = preferred_pictures.Client("testidentity", "testsecret")
        with self.assertRaises(ValueError):
            pp.create_choose_url([], "test-tourney")

    def test_raises_error_with_too_many_choices(self):
        pp = preferred_pictures.Client("testidentity", "testsecret")
        with self.assertRaises(ValueError):
            pp.create_choose_url(range(100), "test-tourney")

    def test_returns_expected_choices(self):

        if not ("PP_IDENTITY" in os.environ and "PP_SECRET_KEY" in os.environ):
            self.skipTest("PP_IDENTITY and PP_SECRET_KEY not specified")

        identity = os.environ["PP_IDENTITY"]
        secret_key = os.environ["PP_SECRET_KEY"]

        pp = preferred_pictures.Client(identity, secret_key)
        url = pp.create_choose_url(
            ["a", "b", "c"], "test-tourney", 600, 3600, "http://example.com/choice-")

        opener = urllib.request.build_opener(RedirectFilter)

        try:
            request = urllib.request.Request(url, data=None, headers={
                'User-Agent': "python-tester"
            })
            opener.open(request)
        except urllib.error.HTTPError as err:
            self.assertEqual(err.code, 302)
            self.assertTrue(re.compile(
                "http:\/\/example.com\/choice-(.)$").search(err.headers["Location"]))


if __name__ == '__main__':
    unittest.main()
