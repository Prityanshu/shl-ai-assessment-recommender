from app.parsers.constraint_extractor import (
extract_constraints
)


messages=[

{

"role":"user",

"content":
"Need senior Java developer with communication skills"

}

]


print(

extract_constraints(

messages

)

)