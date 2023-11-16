def initialize():
    print("GPT Model Initialized")
    return "Model is Initialized"

def giveResults(file_path):
    print("The file is: ", file_path)
    filename = "path\\Hardware_results.txt"
    content = "This is the result from the GPT model for the hardware requirement"

    with open(filename, "w") as f:
        f.write(content)
    
    filename = "path\\Software_results.txt"
    content = "This is the result from the GPT model for the software requirement"

    with open(filename, "w") as f:
        f.write(content)

    result = {
        "Software": "This is the result from the GPT model for the software requirement",
        "Hardware": "This is the result from the GPT model for the hardware requirement",
    }
    return result
