import json

def summarize_response(data):
    # 1. Get name safely
    name = data.get("name", "Unknown")
    # 2. Get role safely
    role = data.get("role", "Unknown")
    # 3. Get skills safely
    skills = data.get("skills", [])
    # 4. Validate that skills is a list
    if not isinstance(skills, list):
        skills = []
    #print(", ".join(str(skill) for skill in skills)) 
    valid_skills = [skill for skill in skills if isinstance(skill, str)]

    return (
    f"Name: {name}\n"
    f"Role: {role}\n"
    f"Skills: {', '.join(valid_skills)}"
    )
try: 
    with open ("Python/json_response_processor.json", "r") as file:
        response = json.load(file)
    if not isinstance(response, dict):
        print("Expected a JSON object.")
    else:
        summary = summarize_response(response)
        print(summary)

except FileNotFoundError:
    print("Error: response.json was not found.")

except json.JSONDecodeError:
    print("Error: The file does not contain valid JSON.")
    
