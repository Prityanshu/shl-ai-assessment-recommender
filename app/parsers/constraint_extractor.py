import json
import re

from app.llm.groq_client import (
    ask_llm
)



def extract_constraints(

    messages

):


    text = "\n".join(

        [

            m["content"]

            for m in messages

        ]

    )



    prompt = f"""

Extract FINAL hiring requirements from the ENTIRE conversation.


Rules:

1. Combine information across turns

2. Later messages OVERRIDE earlier requirements

Examples:


Conversation:

Need senior Java developer

Actually make it entry level


Output:

{{
"skills":["Java"],

"seniority":"entry level",

"duration":null,

"communication":false,

"personality":false
}}



Conversation:

Need Java developer

Add personality tests


Output:

{{
"skills":["Java"],

"personality":true
}}



Conversation:

Need leadership assessment for managers


Output:

{{
"skills":["leadership"],

"seniority":"manager",

"personality":true,

"communication":false
}}



Conversation:

Need communication and teamwork assessment


Output:

{{
"skills":["communication","teamwork"],

"communication":true,

"personality":false
}}



Conversation:

Need personality assessments


Output:

{{
"skills":[],

"personality":true
}}



Return ONLY valid JSON using EXACT schema:


{{
"skills":[],

"seniority":null,

"duration":null,

"communication":false,

"personality":false
}}



Conversation:

{text}

"""



    response = ask_llm(

        prompt

    )



    print(

        "\nRAW LLM OUTPUT:\n",

        response

    )



    try:


        cleaned = re.sub(

            r"```json|```",

            "",

            response

        ).strip()



        parsed = json.loads(

            cleaned

        )



        # Ensure required fields exist


        defaults = {

            "skills": [],

            "seniority": None,

            "duration": None,

            "communication": False,

            "personality": False

        }



        for k,v in defaults.items():


            if k not in parsed:


                parsed[k] = v



        return parsed



    except Exception as e:


        print(

            "\nPARSE ERROR:",

            e

        )



        return {

            "skills": [],

            "seniority": None,

            "duration": None,

            "communication": False,

            "personality": False

        }