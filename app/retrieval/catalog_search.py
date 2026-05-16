import json
import faiss
import numpy as np

from app.retrieval.embedder import (
    generate_embedding
)


index = faiss.read_index(
    "data/catalog.index"
)


with open(
    "data/catalog.json",
    encoding="utf-8"
) as f:

    catalog = json.load(f)



def search_catalog(

    query,

    top_k=10

):


    emb=np.array(

        [

            generate_embedding(
                query
            )

        ]

    ).astype(
        "float32"
    )



    scores,ids=index.search(

        emb,

        30     # retrieve more

    )



    results=[]



    for score,idx in zip(

        scores[0],

        ids[0]

    ):


        item=catalog[idx]


        item["similarity"]=float(
            score
        )


        # -------- reranking --------

        boost=0


        query_lower=query.lower()


        keys=" ".join(

            item.get(

                "keys",

                []

            )

        ).lower()



        desc=item.get(

            "description",

            ""

        ).lower()



        if "personality" in query_lower:


            if (

                "personality" in keys

                or

                "personality" in desc

            ):

                boost+=0.20



        if "communication" in query_lower:


            if (

                "communication"

                in desc

            ):

                boost+=0.15



        item["score"]=(
            score+boost
        )


        results.append(
            item
        )



    results=sorted(

        results,

        key=lambda x:
        x["score"],

        reverse=True

    )



    return results[:top_k]