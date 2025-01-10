import os
import json

class ReflejosResultsOrganizer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "wf_folder_name": ("STRING", {"default": ""}),
                "exp_folder_name": ("STRING", {"default": ""}),
                "wf_api_json": ("STRING", {"default": "\{\}"}),
                "wf_params_dict": ("STRING", {"default": "\{\}"}),
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
            wf_params_dict:str     
        ):
        # Create the folder if it doesn't exist
        if not os.path.exists(wf_folder_name):
            os.makedirs(wf_folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(exp_folder_name):
            os.makedirs(exp_folder_name)

        # Create the file path
        wf_api_path = os.path.join(wf_folder_name, "workflow_api.json")
        wf_params_path = os.path.join(wf_folder_name, "workflow_params.json")

        # Write the content to the file
        json.dump(json.loads(wf_api_json), open(wf_api_path, "w"), indent=4)
        json.dump(json.loads(wf_params_dict), open(wf_params_path, "w"), indent=4)

        return {}