"""DONT USE THIS!!! IT'S PRE-ALPHA TEST CASES!!!"""
import unittest

from prodia_api import prodia


class TestProdia(unittest.IsolatedAsyncioTestCase):
    async def test_prodia(self):
        b = await prodia("test prompt")

        self.assertIsInstance(b, bytes)

        with open("image.png", "wb") as img:
            img.write(b)
