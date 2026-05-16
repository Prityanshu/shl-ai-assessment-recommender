BLOCKED = [

    "ignore instructions",

    "legal advice",

    "medical advice",

    "financial advice",

    "hack",

    "bypass",

    "aws certification",

    "recommend courses"

]



def check_guardrails(

messages

):


    text = " ".join(

        [

            m["content"]

            for m in messages

        ]

    ).lower()



    for blocked in BLOCKED:


        if blocked in text:


            return (

                False,

                "I can only recommend SHL assessments and related hiring evaluations."

            )



    return (

        True,

        None

    )