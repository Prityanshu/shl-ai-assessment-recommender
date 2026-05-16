import re

from app.retrieval.catalog_search import (
    search_catalog
)



def compare_assessments(

query:str

):


    matches = re.findall(

        r'compare\s+(.*?)\s+and\s+(.*)',

        query,

        re.IGNORECASE

    )



    if not matches:


        return (

            "Please specify two assessments to compare."

        )



    first,second = matches[0]



    result1 = search_catalog(

        first,

        top_k=1

    )



    result2 = search_catalog(

        second,

        top_k=1

    )



    if (

        not result1

        or

        not result2

    ):


        return (

            "Unable to compare assessments."

        )



    a=result1[0]
    b=result2[0]



    comparison=f"""

Assessment 1:
{a["name"]}

Type:
{",".join(a["keys"])}

Description:
{a["description"][:180]}



---------------------



Assessment 2:
{b["name"]}

Type:
{",".join(b["keys"])}

Description:
{b["description"][:180]}



---------------------



Suggested usage:

• {a["name"]}

Use when:
evaluating {",".join(a["keys"]).lower()}



• {b["name"]}

Use when:
evaluating {",".join(b["keys"]).lower()}


"""



    return comparison