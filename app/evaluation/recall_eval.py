from app.agents.recommender import (
    recommend
)



# ==================================
# Conversation traces
# ==================================

test_queries = [


# ----------------------------------
# Single-turn traces
# ----------------------------------

{
"query":

"Entry Java",


"constraints":
{
"skills":["Java"],
"seniority":"entry level"
},


"expected":[

"Java",

"Core Java"

]

},



{
"query":

"Personality",


"constraints":
{
"personality":True
},


"expected":[

"OPQ",

"Personality"

]

},



{
"query":

"Communication",


"constraints":
{
"communication":True
},


"expected":[

"communication"

]

},



{
"query":

"Leadership",


"constraints":
{
"leadership":True
},


"expected":[

"leadership"

]

},



# ----------------------------------
# Multi-turn / refinement traces
# ----------------------------------

{
"query":

"Java + Personality",


"constraints":
{
"skills":["Java"],
"personality":True
},


"expected":[

"Java",

"OPQ"

]

},



{
"query":

"Manager + Leadership",


"constraints":
{
"seniority":"manager",
"leadership":True
},


"expected":[

"manager",

"leadership"

]

},



{
"query":

"Java + Communication",


"constraints":
{
"skills":["Java"],
"communication":True
},


"expected":[

"Java",

"communication"

]

},



{
"query":

"Senior Java + Personality",


"constraints":
{
"skills":["Java"],
"seniority":"senior",
"personality":True
},


"expected":[

"Java",

"OPQ"

]

}

]



# ==================================
# Evaluation
# ==================================

K = 10

recalls = []



for trace in test_queries:



    recs = recommend(

        trace["constraints"]

    )



    names = [

        r["name"].lower()

        for r in recs[:K]

    ]



    hits = 0



    for expected in trace["expected"]:



        matched = False



        for result in names:



            if (

                expected.lower()

                in result

            ):



                matched = True

                break



        if matched:

            hits += 1



    recall = (

        hits

        /

        len(

            trace["expected"]

        )

    )



    recalls.append(

        recall

    )



    print(

        "\n",

        "="*40

    )



    print(

        "Trace:",

        trace["query"]

    )



    print(

        "Constraints:",

        trace["constraints"]

    )



    print(

        "Top recommendations:"

    )



    for name in names:


        print(

            "-",

            name

        )



    print(

        f"\nRecall@{K}:",

        round(

            recall,

            2

        )

    )



# ==================================
# Mean Recall@10
# ==================================

mean_recall = (

    sum(

        recalls

    )

    /

    len(

        recalls

    )

)



print(

    "\n",

    "="*50

)



print(

    f"Mean Recall@{K}:",

    round(

        mean_recall,

        2

    )

)



print(

    "="*50
)