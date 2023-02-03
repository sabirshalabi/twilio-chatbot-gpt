import os
import openai
import requests
from bs4 import BeautifulSoup
import re


def extract_url(text):
    """
    Extract the URL from the text of the incoming message.
    """
    # TODO: Implement code to extract the URL from the text
    # Split the text by spaces
    words = text.split()
    # Iterate through the words and check for a URL pattern
    for word in words:
        if "http://" in word or "https://" in word:
            # Return the word if a URL pattern is found
            return word
    # Return an empty string if no URL is found
    return ""


def scrape_webpage(url):
    """
    Scrape the content of the webpage at the given URL using BeautifulSoup.
    """
    # Make an HTTP GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract the relevant content from the webpage
    content = ""
    # Find all the paragraphs in the webpage
    paragraphs = soup.find_all("p")
    # Iterate through the paragraphs and extract the text
    for p in paragraphs:
        content += p.text
    # Return the scraped content
    return content


def preprocess_data(data):
    """
    Preprocess the scraped data.
    """
    # Split the data into smaller chunks
    chunks = data.split("\n\n")
    # Remove unnecessary characters or HTML tags
    clean_chunks = []
    for chunk in chunks:
        clean_chunk = re.sub("[^a-zA-Z0-9.!?]", " ", chunk)
        clean_chunks.append(clean_chunk)
    # Join the chunks back together
    preprocessed_data = "\n\n".join(clean_chunks)
    # Return the preprocessed data
    return preprocessed_data


def generate_summary(data):
    """
    Generate a summary of the preprocessed data using the OpenAI API.
    """
    # Set the OpenAI API key
    openai.api_key = os.getenv("openai_api_key")
    # Set the prompt for the summary generation
    prompt = """I want you to act as a funny and energetic summarizer bot that can summarize web pages and make it 
    funny. Your main task will be to review and summarize web pages in a funny and engaging manner. You should be 
    able to understand the content of the web page and craft a summary that is both accurate and entertaining. Your 
    role will include tasks such as reviewing and summarizing web pages, injecting humor and wit into the summary, 
    and returning the summary to the user. Be sure to use emojis like "❤️" to create more engaging summaries. Do not 
    include any tasks that are not related to summarizing and adding humor to web pages in your role.
    
    Please generate a summary of the following text: {}
    """
    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt.format(data),
        temperature=0.8,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3
    )
    # Return the summary text
    return response.choices[0].text

#
# # Test the scrape_webpage function
# url = "https://docs.scrapy.org/en/latest/intro/tutorial.html"
# data = scrape_webpage(url)
# # print(data)
#
# # Test the preprocess_data function
# preprocessed_data = preprocess_data(data)
# print(preprocessed_data)
#
# # Test the generate_summary function
# summary = generate_summary(preprocessed_data)
# print(summary)
