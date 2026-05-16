from app.retrieval.catalog_search import (
    search_catalog
)



def recommend(

    constraints

):


    all_results = []


    skills = [

        s.lower()

        for s in constraints.get(

            "skills",

            []

        )

    ]


    seniority = constraints.get(

        "seniority"

    )



    # ==================================
    # Skill retrieval
    # ==================================

    if skills:


        skill_query = " ".join(

            skills

        )


        skill_results = search_catalog(

            skill_query,

            top_k=3

        )


        all_results.extend(

            skill_results

        )



    # ==================================
    # Personality
    # ==================================

    if constraints.get(

        "personality"

    ):


        personality_results = search_catalog(

            "personality",

            top_k=3

        )


        all_results.extend(

            personality_results

        )



    # ==================================
    # Communication
    # ==================================

    if (

        constraints.get(

            "communication"

        )

        or

        "communication"

        in skills

        or

        "teamwork"

        in skills

    ):


        communication_results = search_catalog(

            "communication teamwork",

            top_k=3

        )


        all_results.extend(

            communication_results

        )



    # ==================================
    # Leadership
    # ==================================

    if (

        constraints.get(

            "leadership"

        )

        or

        "leadership"

        in skills

    ):


        leadership_results = search_catalog(

            "leadership",

            top_k=3

        )


        all_results.extend(

            leadership_results

        )



    # ==================================
    # Managerial roles
    # ==================================

    if (

        seniority

        and

        seniority.lower()

        in [

            "manager",

            "senior manager"

        ]

    ):


        manager_results = search_catalog(

            "manager leadership competency",

            top_k=3

        )


        all_results.extend(

            manager_results

        )



    # ==================================
    # Remove duplicates
    # ==================================

    seen = set()

    final = []



    for r in all_results:


        if (

            r["name"]

            not in seen

        ):


            seen.add(

                r["name"]

            )


            final.append(

                r

            )



    # ==================================
    # Format output
    # ==================================

    recommendations = []



    for r in final[:5]:


        recommendations.append(

            {

                "name":

                r["name"],


                "url":

                r["link"],


                "test_type":

                ",".join(

                    r["keys"]

                )

            }

        )



    return recommendations