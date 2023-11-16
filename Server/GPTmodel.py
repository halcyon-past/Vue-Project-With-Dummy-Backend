def initialize():
    print("GPT Model Initialized")
    return "Model is Initialized"

def giveResults(file_path):
    print("The file is: ", file_path)
    result = {
        "Software": "This is the result from the GPT model for the software requirement",
        "Hardware": "This is the result from the GPT model for the hardware requirement",
        "Network": "This is the result from the GPT model for the network requirement",
        "Security": "This is the result from the GPT model for the security requirement",
    }
    return result
