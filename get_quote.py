""" Send Motivational Mail to ALL"""
import os
import requests


def quote(category):
    """Return: Quotes from open API - api-ninjas"""

    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"

    response = requests.get(
        api_url,
        headers={"X-Api-Key": os.getenv("APIKEY")},
        timeout=30,
    )

    return response.json()
