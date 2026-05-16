from app.retrieval.catalog_search import search_catalog


results=search_catalog(

"Need Java assessment for experienced developer"

)



for r in results:

    print(

        r["name"],

        r["similarity"]

    )