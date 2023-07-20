import openai

import os

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)

class OpenAiConnector:
    
    open_ai_model = os.getenv('OPENAI_MODEL')
    
    # OpenAI API credentials
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    def send_to_openai(self, prompt, email_dict):
        """Sends the email details and prompt to the OpenAI GPT API."""

        # combine email details and prompt
        message = f"Sender: {email_dict['from']}\nSend Date: {email_dict['send_date']}\nSubject: {email_dict['subject']}\nBody: {email_dict['body']}\n\n{prompt}"

        # send message to OpenAI GPT API
        retry_count = 0
        while retry_count < 3:
                 # combine email details and prompt
                message = f"Sender: {email_dict['from']}\nSend Date: {email_dict['send_date']}\nSubject: {email_dict['subject']}\nBody: {email_dict['body']}\n\n{prompt}"
                try:
                    completion = openai.ChatCompletion.create(
                        model=self.open_ai_model,
                        messages=[{"role": "user", "content": message}])
                except Exception as e:
                    logging.error(f"Error occurred while sending to OpenAI: {e}")
                    half_body = email_dict['body'][:len(email_dict['body'])//2]
                    message = f"Sender: {email_dict['from']}\nSend Date: {email_dict['send_date']}\nSubject: {email_dict['subject']}\nBody: {half_body}\n\n{prompt}"
                    
                retry_count += 1
        

        # get response text
        response_text = completion.choices[0].message.content

        # print response
        return response_text

    def set_model(self, model):
        """Sets the model to use for the OpenAI GPT API."""
        self.open_ai_model = model
        
    def extract_info(self, response_text):
        try:
            # Initialize default values
            importance = None
            summary = None
            response = None

            # Split the string into parts on newline characters
            parts = response_text.split("\n")

            # Further split each part on the colon character and store in a dictionary
            data = {part.split(": ")[0]: part.split(": ")[1] for part in parts}

            # Retrieve the values from the dictionary
            importance = int(data["Importance"])
            summary = data["Summary"]
            response = data["Response"]

            return importance, summary, response

        except Exception as e:
            logging.error(f"An error occurred when splitting the response: {e}")
            return 0, "error", "error"

