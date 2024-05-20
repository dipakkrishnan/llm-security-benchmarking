from typing import List
from src.utils.logger import logger
from src.client.base import BaseClient


class OllamaClient(BaseClient):

    def __init__(
        self,
        model: str = "llama3"
    ):
        """
        :param model: foundation model for generating content
        """
        self.model = model

    def __call__(
        self,
        prompt: str,
        messages = List
    ):
        """
        Calls Ollama to generate completions

        :param prompt: user prompt to LM
        :param messages: messages that user can define to help model interpret chat, defaults to None
        """
        try:
            # Build messages to pass for completion
            messages = messages or [{"role": "user", "content": prompt}]

            # TODO: add call to Ollama endpoint

        except Exception as e:
            logger.exception(f"Failed to generate completion against Ollama with model={self.model}.")
