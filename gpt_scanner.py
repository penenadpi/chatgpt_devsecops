import openai

openai.api_key = "place-your-own-key"

def scan_file(file_type: str, path: str)->str:
	contents = ""
	with open(path, 'r') as file:
		contents = file.read().replace('\n', '')
		print(contents)	
	question = f"Find security flaws in {file_type} script:{contents}"
	response = openai.Completion.create(
	    engine="text-davinci-002",
	    prompt=question,
	    max_tokens=2048,
	    n = 1,
	    stop=None,
	    temperature=0.5,
	)
	result = response["choices"][0]["text"]
	print(result)
	return result
	
scan_file("Terraform", "main.tf")
