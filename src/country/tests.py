from django.test import TestCase
from rest_framework.test import APITestCase
from .models import State
from .serializers import StateSerializer

# Create your tests here.

class StateTests(APITestCase):
    def test_can_get_state_details(self):
        state = State.objects.create(state_name='example', country_id=1)
        response = self.client.get(f'/state/{state.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, StateSerializer(instance=state).data)
