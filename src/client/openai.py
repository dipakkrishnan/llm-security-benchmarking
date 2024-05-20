import os
from openai import OpenAI
from typing import List
from src.utils.logger import logger
from dotenv import load_dotenv

load_dotenv()


class OpenAIClient:

    def __init__(
        self,
        model: str = "gpt-3.5-turbo"
    ):
        """
        :param model: foundation model for generating content
        """
        self.model = model
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    def __call__(
        self,
        prompt: str,
        messages: List = None
    ):
        """
        Calls OpenAI to generate completions

        :param prompt: user prompt to LM
        :param messages: 
        """
        try:
            # Build messages to pass for completion
            messages = messages or [{"role": "user", "content": prompt}]

            # Make call for completion generation
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            # Parse to retrieve content
            return response.choices[0].message['content']
        
        except Exception as e:
            logger.exception("Failed to generate completion against OpenAI.")   
