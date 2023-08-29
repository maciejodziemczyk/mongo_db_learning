import json

import click
import pymongo

client = pymongo.MongoClient("mongodb://root:example@localhost:27018/")


@click.command()
@click.option("-d", "--db", "db", required=True)
@click.option("-c", "--collection", "collection", required=True)
@click.option(
    "-p", "--filepath", "filepath", required=True, type=click.Path(exists=True, file_okay=True, readable=True)
)
def cli(db: str, collection: str, filepath: str) -> None:
    with open(filepath) as file:
        file_data = json.load(file)

    client[db][collection].insert_many(file_data)


if __name__ == "__main__":
    cli()
