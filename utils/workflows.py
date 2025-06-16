from utils.llm import LLMHandler
from dotenv import dotenv_values
import json

class LinearWorkflow:
    def __init__(self, workflow_file:str=""):
        self.config         = dotenv_values(".env")

        self.pointer        = 0
        self.last_output    = ""
        self.session_output = ""
        self.session_store  = []

        self.llm_handler    = LLMHandler(model_name="gpt-4o",
                                api_key=self.config["OPENAI_API_KEY"],
                                temperature=0.8)
        
        if workflow_file == "":
            self.workflow = None
        else:
            print(f"-> Loading workflow file {workflow_file}...")
            self.workflow = self.read_workflow_file(workflow_file)

    def save_session_output(self):
        # Save to markdown file
        with open('session_output.md', 'w') as f:
            f.write(self.session_output)
    
    def read_workflow_file(self, path:str):
        # Reset all runtime variables
        self.pointer = 0
        self.last_output = ""
        
        # Read in a workflow definition file in JSON format
        f = open(path,)
        workflow_tmp = json.load(f)
        f.close()

        # print(workflow_tmp["workflow"][0])
        return workflow_tmp["workflow"]
    
    def next_step(self, input:str = ""):
        # Stepping over to the next step of the sequence

        # Replace inputs

        # </user_input/>
        # </last_response/>

        query_prompt = str(self.workflow[self.pointer])
        query_prompt.replace("</user_input/>", input)
        query_prompt.replace("</last_response/>", self.last_output)

        self.session_store.append(["query_prompt", query_prompt])
        self.session_output += f"{query_prompt}\n\n"

        # Invoke inference
        self.last_output = self.llm_handler.query(query_prompt)
        self.session_store.append(["llm_output", self.last_output])

        self.session_output += f"{self.last_output}\n\n"

        self.save_session_output()

        # Shift pointer
        self.pointer += 1

    def detached_step(self, input:str = ""):
        # Detach session and insert a human action
        pass
