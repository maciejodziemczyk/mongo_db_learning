from pprint import pprint

import click
import pymongo

client = pymongo.MongoClient("mongodb://root:example@localhost:27018/")


@click.command()
@click.argument("regex")
@click.option("-o", "--options", required=False)
@click.option("-d", "--db", "db", required=True)
@click.option("-c", "--collection", "collection", required=True)
def cli(regex: str, options: str, db: str, collection: str) -> None:
    col: pymongo.collection.Collection = client[db][collection]
    query = {"text": {"$regex": regex}}
    if options:
        query["text"]["$options"] = options
    cursor = col.find(
        query, {"text": 1, "_id": 0}
    )
    pprint(list(cursor))


if __name__ == "__main__":
    cli()
