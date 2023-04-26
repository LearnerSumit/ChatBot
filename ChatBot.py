import openai
import requests
import bs4

openai.api_key = "Enter Your OpenAI API"

def chatbot(prompt):
  # Use OpenAI's Completion API to generate a response
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    temperature=0.7,
  )
    # Extract the response text
  response_text = response["choices"][0]["text"]
  return response_text
 

def search(query):
  results = []
  API_KEY = "AIzaSyCLnjz9rxWVDTXYSG-vnTQzIB8-g2cGXD8"
  CX_ID = "d7633c053b9c24361"
  URL = "https://www.googleapis.com/customsearch/v1"
  params = {
  "q": query,
  "key": API_KEY,
  "cx": CX_ID
  }
  response = requests.get(URL, params=params)
  data = response.json()
  for item in data["items"]:
    title = item["title"]
    link = item["link"]
    snippet = item["snippet"]
    results.append({
      "title": title,
      "link": link,
      "snippet": snippet
    })
  return results

while True:
  prompt = input("Enter your question: ")
  results = search(prompt)
  if not results:
    print(chatbot(prompt))
  else:
    print(chatbot(prompt))
    print("\n\nHere are some related links that may be of interest:\n")
    for result in results:
      print(result["title"])
      print(result["link"])
      print(result["snippet"],"\n")

