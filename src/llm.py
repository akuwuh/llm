#!/usr/bin/env python3
# ----------------------------
#       Import Modules
# ----------------------------
import os
import sys
import openai 
from dotenv import load_dotenv

class LLM:
    _prompt_ = ""
    _file_type_ = ""

    def __init__(self, prompt=None, file_type=None) -> None:
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        try:
            openai.Model.list()
        except openai.error.AuthenticationError as error:
            print(f"\nError Encountered: \n \t {error} \n")
            print("Failed to Initialize GPT Model. Exiting Program . . \n")
            sys.exit(1)
        
        # gpt initialization successful
        if prompt is not None: self._prompt_ = prompt
        if file_type is not None: self._file_type_ = file_type
        
        

    def set_prompt(self, prompt: str):
        self._prompt_ = prompt

    def set_file_type(self, file_type: str):
        self._file_type_ = file_type.lower()

    def generate_response(self) -> str:
        scenario = self._prompt_
        file_type = self._file_type_
        assistant = "You generate a " + file_type + " testfile for a MATLab that simulates the scenario based on the prompt given by the user. The test " + file_type + " file should be descriptive in it specifications for the test. ONLY output the generated " + file_type + " file without anything else in your response."
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": assistant},
                    {"role": "user", "content": scenario}
                ]
            )
        except Exception as error:
            print(f"\nError Encountered: \n \t {error} \n")
            print("Failed to GET resopnse. Exiting Program . . \n")
            sys.exit(1)

        # Successfully Generated Response
        output = response.choices[0].message.content
        return output

