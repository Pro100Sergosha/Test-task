from django.test import TestCase
from django.urls import reverse


class GetWeatherSimpleTests(TestCase):

    def test_get_weather_with_city_param(self):
        response = self.client.get(reverse("get_weather"), {"city": "Москва"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("city", response.context)
        self.assertEqual(response.context["city"], "Москва")
        self.assertIn("weather", response.context)

    def test_get_weather_without_city_param(self):
        response = self.client.get(reverse("get_weather"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["weather"])

    def test_get_weather_with_empty_city(self):
        response = self.client.get(reverse("get_weather"), {"city": ""})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["city"], "")
        self.assertIsNone(response.context["weather"])

    def test_get_weather_with_invalid_city_name(self):
        response = self.client.get(reverse("get_weather"), {"city": "asldkjfasldkjf"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["city"], "asldkjfasldkjf")
        self.assertIsNone(response.context["weather"])
