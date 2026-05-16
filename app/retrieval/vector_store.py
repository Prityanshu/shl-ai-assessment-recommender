import json
import faiss
import numpy as np

from app.retrieval.embedder import (
    generate_embedding,
    create_document
)


INDEX_PATH="data/catalog.index"



def build_index():

    with open(

        "data/catalog.json",

        encoding="utf-8"

    ) as f:

        catalog=json.load(f)



    docs=[

        create_document(
            item
        )

        for item in catalog

    ]



    embeddings=np.array(

        [

            generate_embedding(
                d
            )

            for d in docs

        ]

    ).astype(
        "float32"
    )



    dimension=embeddings.shape[1]



    index=faiss.IndexFlatIP(

        dimension

    )



    index.add(

        embeddings

    )



    faiss.write_index(

        index,

        INDEX_PATH

    )



    print(

        f"stored {len(docs)} assessments"

    )



if __name__=="__main__":

    build_index()