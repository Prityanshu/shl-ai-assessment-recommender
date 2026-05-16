from sentence_transformers import (
    SentenceTransformer
)


model = None


def get_model():

    global model


    if model is None:

        print(

            "Loading embedding model..."

        )


        model = SentenceTransformer(

            "BAAI/bge-small-en-v1.5"

        )


    return model




def create_document(item):


    return f"""

Assessment:
{item["name"]}

Description:
{item["description"]}

Job Levels:
{", ".join(item.get("job_levels",[]))}

Duration:
{item.get("duration","")}

Adaptive:
{item.get("adaptive","")}

Remote:
{item.get("remote","")}

Categories:
{", ".join(item.get("keys",[]))}

Languages:
{", ".join(item.get("languages",[]))}

"""



def generate_embedding(


    text

):


    return get_model().encode(

        text,

        normalize_embeddings=True

    )