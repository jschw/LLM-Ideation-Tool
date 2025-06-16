import time
import os, signal
from utils.workflows import LinearWorkflow

def main():
    current_workflow = 0

    # Init workflow object
    lflow = LinearWorkflow("workflows/workflow_1.json")

    def reinit_workflow():
        print("TODO: Reinit")

    # try:

    while True:
        new_txt = input("-> ")

        if new_txt == "/quit":
            quit()
        
        elif new_txt == "/clear":
            reinit_workflow()
            continue

        elif new_txt == "/nxt":
            # Step over
            lflow.next_step()


    '''except Exception as e:
        print(str(e))
        pass'''

if __name__ == '__main__':
    main()
