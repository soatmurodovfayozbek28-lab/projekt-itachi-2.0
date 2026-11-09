import unittest

from backend.core.ai_gateway import (
    AIProvider,
    AIGateway
)


class MockProvider(AIProvider):

    async def generate(self, prompt: str) -> str:
        return f"AI response: {prompt}"


class GatewayTests(unittest.IsolatedAsyncioTestCase):

    async def test_provider_connection(self):
        gateway = AIGateway()
        gateway.register_provider(MockProvider())

        result = await gateway.generate("Hello Itachi")

        self.assertEqual(
            result,
            "AI response: Hello Itachi"
        )

    async def test_without_provider(self):
        gateway = AIGateway()

        with self.assertRaises(RuntimeError):
            await gateway.generate("Hello")


if __name__ == "__main__":
    unittest.main()