def need_clarification(

constraints

):


    skills = constraints.get(

        "skills",

        []

    )



    personality = constraints.get(

        "personality",

        False

    )



    if (

        len(skills)==0

        and

        not personality

    ):


        return (

            True,

            "What role, skill, or position are you hiring for?"

        )



    # Seniority optional
    return (

        False,

        None

    )