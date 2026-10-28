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
    # 5. Print the summary
    print(name)
    print(role)
    #print(", ".join(str(skill) for skill in skills)) 
    valid_skills = [skill for skill in skills if isinstance(skill, str)]
    print(", ".join(valid_skills))

print("\n--- Test 1: Missing fields ---")
summarize_response({})

print("\n--- Test 2: Invalid skills type ---")
summarize_response({
    "name": "Sam",
    "role": "Developer",
    "skills": "Python"
})

print("\n--- Test 3: Mixed skill types ---")
summarize_response({
    "name": "Alex",
    "role": "AI Developer",
    "skills": ["Python", 123, "GenAI", None]
})

try: 
    with open ("Python/json_response_processor.json", "r") as file:
        response = json.load(file)
    if not isinstance(response, dict):
        print("Expected a JSON object.")
    else:
        summarize_response(response)

except FileNotFoundError:
    print("Error: response.json was not found.")

except json.JSONDecodeError:
    print("Error: The file does not contain valid JSON.")
    
