from pprint import pprint

import click
import pymongo

client = pymongo.MongoClient("mongodb://root:example@localhost:27018/")


@click.command()
@click.option("-d", "--db", "db", required=True)
@click.option("-c", "--collection", "collection", required=True)
def cli(db: str, collection: str) -> None:
    agg_pipeline = [
        {
            "$group": {
                "_id": "$author_id",
                "count": {"$sum": 1}
            }
        }
    ]
    col: pymongo.collection.Collection = client[db][collection]
    cursor = col.aggregate(agg_pipeline)
    pprint(list(cursor))


if __name__ == "__main__":
    cli()
