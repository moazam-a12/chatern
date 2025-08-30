# model/gemini_service.py
import json
import pandas as pd
from google import genai
import os

class ChaternService:
    def __init__(self, api_key, dataset_path=None):
        if dataset_path is None:
            dataset_path = os.path.join("data", "intern_support_finetune_gemini.jsonl")

        self.client = genai.Client(api_key=api_key)
        self.dataset = self._load_dataset(dataset_path)

    def _load_dataset(self, dataset_path):
        with open(dataset_path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
        return pd.DataFrame(data)

    def preview_dataset(self, n=5):
        return self.dataset.sample(n)

    def get_context_examples(self, n=3):
        examples = self.dataset.sample(n)
        context = "You are **Chatern**, an AI internship support assistant. Use these examples:\n\n"
        for _, row in examples.iterrows():
            context += f"Q: {row['input']}\nA: {row['output']}\n\n"
        return context

    def ask(self, query, n=3):
        context = self.get_context_examples(n)
        resp = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"{context}\nIntern asked: {query}"
        )
        return resp.text