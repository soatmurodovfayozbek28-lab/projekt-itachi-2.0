from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass


class AIGateway:

    def __init__(self):
        self.provider = None

    def register_provider(self, provider: AIProvider):
        self.provider = provider

    async def generate(self, prompt: str) -> str:
        if self.provider is None:
            raise RuntimeError("No AI provider configured")

        return await self.provider.generate(prompt)


ai_gateway = AIGateway()