import time
from llm import LLM
from export import export_yaml

LINE_CLEAR = '\x1b[2K'
YAML = ".yaml"

def main():
    print("\n[ATTENTION] - Remember to Provide a Valid OpenAI API Key in the \'.env\' File \n")

    # Set Prompt
    prompt =  input("Enter Test Scenario: \n")
    print()

    # Set File Type
    # Can Add Support for Other File Types Later
    file_type = input("Enter Export File Type (i.e \"YAML\"): \n")
    print()

    # Set Filename
    file_name =  input("Enter Export File Name (ommit file extension): \n")
    print()

    # Initializing API Connection
    time.sleep(0.5)
    print("[LLM] Initializing GPT . . ",end='\r')
    gpt = LLM(prompt, file_type)
    print(end=LINE_CLEAR)
    time.sleep(0.3)
    print("[LLM] GPT Successfully Initialized. \n")
    
    # Prompting GPT
    time.sleep(0.5)
    print("[LLM] Generating Test . . ", end="\r")
    result = gpt.generate_response()
    print(end=LINE_CLEAR)
    time.sleep(0.3)
    print("[LLM] Test Generated. \n \n")
    
    # Printing Result
    time.sleep(0.5)
    print("Result: \n \n")
    
    time.sleep(0.3)
    print(result)
    print()


    # Exporting to YAML
    time.sleep(0.5)
    print(f"Exporting to '{file_name + YAML}' . . ", end="\r")
    export_yaml(result, file_name + YAML)
    print(end=LINE_CLEAR)
    time.sleep(0.3)
    print(f"Successfully Exported to '{file_name + YAML}'. Exiting Program . . \n ")
    time.sleep(0.5)


if __name__ == "__main__": 
    main()