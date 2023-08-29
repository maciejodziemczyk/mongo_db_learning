import click
import pymongo


client = pymongo.MongoClient("mongodb://root:example@localhost:27018/")


@click.command()
@click.option("-d", "--db", "db", required=True)
@click.option("-c", "--collection", "collection", required=True)
def count_documents(db: str, collection: str) -> None:
    print(client[db][collection].count_documents({}))


if __name__ == "__main__":
    count_documents()
