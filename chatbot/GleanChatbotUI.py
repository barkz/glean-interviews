import requests
import json
import tkinter as tk
from tkinter import scrolledtext

#AUTH_ENDPOINT = 'https://support-lab-be.glean.com/rest/api/v1/authenticate'
API_KEY = 'ong6bNNqAF/re+uU2YJ5Pymdui3n2VdgiDJoM+X5xo0='
CHATBOT_ENDPOINT = 'https://support-lab-be.glean.com/rest/api/v1/chat'

def authenticate():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    response = requests.post(CHATBOT_ENDPOINT, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('token')
    else:
        response.raise_for_status()

def send_chatbot_request(messages, author, fragments):
    token = authenticate()
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    payload = {
       'stream': True, # Set to False to toggle off streaming mode
        'messages': [{
            'author': 'USER',
            'fragments': [{'text': 'What are the holidays this year?'}]
        }],
    }
    
    response = requests.post(CHATBOT_ENDPOINT, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def process_message_fragment(message):
    message_type = message['messageType']
    fragments = message.get('fragments', [])
    citations = message.get('citations', [])

    if message_type == 'CONTENT':
        if fragments:
            for fragment in fragments:
                text = fragment.get('text', '')
                print(text, end='', flush=True)
        if citations:
            print('\nSources:')
            for idx, citation in enumerate(citations):
                sourceDocument = citation.get('sourceDocument', {})
                if sourceDocument:
                    source = citation['sourceDocument']
                    print(f'Source {idx + 1}: Document title - {source["title"]}, url: {source["url"]}')
                sourcePerson = citation.get('sourcePerson', {})
                if sourcePerson:
                    source = citation['sourcePerson']
                    print(f'Source {idx + 1}: Person name - {source["name"]}')

def process_response_message_stream(response):
    for line in response.iter_lines():
        if line:
            line_json = json.loads(line)
            messages = line_json.get('messages', [])
            for message in messages:
                process_message_fragment(message)

def on_send_request():
    messages = [{"author": author_entry.get(), "fragments": [{"text": message_entry.get()}]}]
    author = author_entry.get()
    fragments = [fragment.strip() for fragment in fragments_entry.get().split(',')]
    
    try:
        response = send_chatbot_request(messages, author, fragments)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, json.dumps(response, indent=4))
    except Exception as e:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, str(e))

# GUI setup
root = tk.Tk()
root.title("Chatbot Request GUI")

tk.Label(root, text="Message:").grid(row=0, column=0, padx=10, pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=5)
author_entry = tk.Entry(root, width=50)
author_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Fragments (comma-separated):").grid(row=2, column=0, padx=10, pady=5)
fragments_entry = tk.Entry(root, width=50)
fragments_entry.grid(row=2, column=1, padx=10, pady=5)

send_button = tk.Button(root, text="Send Request", command=on_send_request)
send_button.grid(row=3, column=0, columnspan=2, pady=10)

response_text = scrolledtext.ScrolledText(root, width=60, height=20)
response_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()