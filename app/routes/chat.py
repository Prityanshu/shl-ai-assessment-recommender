from fastapi import APIRouter

from app.models.request_schema import (
    ChatRequest
)

from app.parsers.constraint_extractor import (
    extract_constraints
)

from app.agents.conversation_agent import (
    need_clarification
)

from app.agents.recommender import (
    recommend
)

from app.agents.guardrails import (
    check_guardrails
)

from app.agents.comparison import (
    compare_assessments
)


router = APIRouter()



@router.post(
    "/chat"
)

def chat(

    request: ChatRequest

):


    messages = [

        m.model_dump()

        for m in request.messages

    ]


    full_text = " ".join(

        m["content"]

        for m in messages

    ).lower()



    # ==================================
    # Guardrails
    # ==================================

    allowed, guardrail_reply = (

        check_guardrails(

            messages

        )

    )


    if not allowed:


        return {

            "reply":

            guardrail_reply,


            "recommendations": [],


            "end_of_conversation":

            True

        }



    # ==================================
    # Comparison mode
    # ==================================

    if "compare" in full_text:


        comparison = compare_assessments(

            full_text

        )


        return {

            "reply":

            comparison,


            "recommendations": [],


            "end_of_conversation":

            True

        }



    # ==================================
    # Extract constraints
    # ==================================

    constraints = extract_constraints(

        messages

    )


    print(

        "\nEXTRACTED:",

        constraints

    )



    # ==================================
    # Clarification
    # ==================================

    clarify, clarification_reply = (

        need_clarification(

            constraints

        )

    )


    if clarify:


        return {

            "reply":

            clarification_reply,


            "recommendations": [],


            "end_of_conversation":

            False

        }



    # ==================================
    # Recommendations
    # ==================================

    recs = recommend(

        constraints

    )



    if not recs:


        return {

            "reply":

            "I couldn't find suitable SHL assessments for those requirements.",


            "recommendations": [],


            "end_of_conversation":

            True

        }



    explanation_lines = []

    shown_categories = set()



    for r in recs:


        category = r["test_type"]

        name = r["name"].lower()



        if category in shown_categories:

            continue



        shown_categories.add(

            category

        )



        explanation = ""



        # ==================================
        # Leadership FIRST
        # ==================================

        if (

            "leadership"

            in name

            or

            "manager"

            in name

        ):


            explanation = (

                f"• {r['name']} "

                "assesses leadership capability, managerial effectiveness, and development potential."

            )



        # ==================================
        # Communication
        # ==================================

        elif (

            "communication"

            in name

            or

            "interpersonal"

            in name

            or

            "business communication"

            in name

            or

            "teamwork"

            in name

        ):


            explanation = (

                f"• {r['name']} "

                "evaluates communication effectiveness, teamwork, and workplace interaction skills."

            )



        # ==================================
        # Personality
        # ==================================

        elif (

            "Personality"

            in category

        ):


            explanation = (

                f"• {r['name']} "

                "evaluates personality traits, behavioral tendencies, and workplace fit."

            )



        # ==================================
        # Competencies
        # ==================================

        elif (

            "Competencies"

            in category

        ):


            explanation = (

                f"• {r['name']} "

                "evaluates competencies relevant to job performance and success."

            )



        # ==================================
        # Technical
        # ==================================

        elif (

            "Knowledge"

            in category

        ):


            explanation = (

                f"• {r['name']} "

                "assesses technical knowledge and role-specific skills."

            )



        # ==================================
        # Development / 360
        # ==================================

        elif (

            "Development"

            in category

            or

            "360"

            in category

        ):


            explanation = (

                f"• {r['name']} "

                "supports leadership development and multi-perspective evaluation."

            )



        # ==================================
        # Fallback
        # ==================================

        else:


            explanation = (

                f"• {r['name']} "

                "matches your hiring requirements."

            )



        explanation_lines.append(

            explanation

        )



        if len(

            explanation_lines

        ) >= 3:

            break



    reply = (

        "Recommended assessments based on your requirements:\n\n"

        +

        "\n".join(

            explanation_lines

        )

    )



    return {

        "reply":

        reply,


        "recommendations":

        recs,


        "end_of_conversation":

        True

    }