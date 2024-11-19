from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Function to fetch and parse webpage
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

# Function to scrape news headlines and their metadata
def scrape_data(html, headline_selector, image_selector, para_selector, base_url=None):
    soup = BeautifulSoup(html, 'html.parser') # Parse the HTML content of the webpage
    
    # Extract headlines
    headlines = soup.select(headline_selector)
    headline_texts = [headline.get_text(strip=True) for headline in headlines]
    
    # Extract paragraph
    paras = soup.select(para_selector)
    para_texts = [para.get_text(strip=True) for para in paras]
    
    # Extract image URLs
    images = soup.select(image_selector)
    image_urls = [img.get('src') for img in images]

    if base_url:
        image_urls = [url if url.startswith("http") else base_url + url for url in image_urls]
    
    # Combine headlines and images
    data = [{"Headline": headline,"Paragraph":para, "Image URL": image} for headline,para, image in zip(headline_texts,para_texts, image_urls)]
    
    # Filter out items with missing or placeholder images
    filtered_data = [
        item for item in data 
        if item["Image URL"] and not item["Image URL"].endswith("grey-placeholder.png")
    ]
    
    return filtered_data

app = Flask(__name__)
CORS(app)
@app.route("/scrape", methods=["POST"])
def scrape():
    user = request.json.get("user")
    if not user:
        return jsonify({"status": "error", "message": "User parameter is missing"}), 400

    # Using BBC News' Website for Web Scraping
    url = f"https://www.bbc.com/{user}"
    headline_selector = "h2"
    image_selector = "img"
    para_selector = "p"
    base_url = "https://www.bbc.com"

    print("Fetching webpage...")
    html = fetch_webpage(url)

    if html:
        print("Scraping headlines and images...")
        data = scrape_data(html, headline_selector, image_selector, para_selector, base_url)
        if data:
            return jsonify({"status": "success", "category": user, "data": data}) 
    return jsonify({"status": "error", "message": "Failed to fetch or scrape data"}), 500

if __name__ == '__main__':
    app.run(port=5001,debug=True)