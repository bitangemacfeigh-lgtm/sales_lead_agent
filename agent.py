import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

class SalesLeadAgent:
    def __init__(self):
        api_key = os.getenv("MISTRAL_API_KEY")
        # Ensure the client is initialized correctly
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"

    def research_lead(self, lead_description):
        prompt = (
            f"Act as a professional sales researcher. Analyze this lead: '{lead_description}'. "
            "Provide a bulleted list of 3 potential pain points and a brief strategy for engagement."
        )
        
        response = self.client.chat.complete(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def draft_outreach(self, research_data):
        prompt = (
            f"Based on this research: {research_data}, write a high-converting cold email. "
            "Keep it under 150 words. Use a professional yet conversational tone."
        )
        
        response = self.client.chat.complete(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content