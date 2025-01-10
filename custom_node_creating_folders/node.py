import os
import json

class ReflejosResultsOrganizer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wf_folder_name": ("STRING", {"default": ""}),
                "exp_folder_name": ("STRING", {"default": ""}),
                "wf_api_json": ("STRING", {"default": '\{\}'}),
                "wf_params_dict": ("STRING", {"default": "\{\}"}),
                "time_of_submission": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "set_wf_experiment_info"
    CATEGORY = "file_operations"
    OUTPUT_NODE = True

    def set_wf_experiment_info(
            self, 
            wf_folder_name:str, 
            exp_folder_name:str,
            wf_api_json:str,
            wf_params_dict:str,
            time_of_submission:str     
        ):
        # Create the folder for the workflow resutls if it doesn't exist
        if not os.path.exists(wf_folder_name):
            os.makedirs(wf_folder_name)

        # Create the folder of the experiment results if it doesn't exist
        if not os.path.exists(exp_folder_name):
            os.makedirs(exp_folder_name)

        # Create the folder for storing the workflows and parameters json
        workflow_info_folder = os.path.join(exp_folder_name, "workflow__info")
        if not os.path.exists(workflow_info_folder):
            os.makedirs(workflow_info_folder)
    

        # Create the file path
        wf_api_path = os.path.join(workflow_info_folder, f"workflow_api_{time_of_submission}.json")
        wf_params_path = os.path.join(workflow_info_folder, f"workflow_params_{time_of_submission}.json")

        # Write the content to the file
        json.dump(json.loads(wf_api_json), open(wf_api_path, "w"), indent=4)
        json.dump(json.loads(wf_params_dict), open(wf_params_path, "w"), indent=4)

        print(f"Workflow API saved in {wf_api_path}")
        print(f"Workflow Params saved in {wf_params_path}")
        return {}