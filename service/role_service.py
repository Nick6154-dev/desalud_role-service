from model.role_model import Role
from config.dbConfig import initialize_mongo_instance
import os


async def get_collection(collection_name=None):
    if collection_name is None:
        collection_name = os.getenv('MONGO_DATABASE_COLLECTION', 'role')
    mongo = await initialize_mongo_instance()
    return mongo[collection_name]


async def find_all():
    collection = await get_collection()
    cursor = collection.find({}, {'_id': 0})
    documents = [doc async for doc in cursor]
    return documents


async def find_by_role_name(role_name: str):
    collection = await get_collection()
    filter_query = {'role_name': role_name}
    cursor = collection.find(filter_query, {'_id': 0})
    documents = [doc async for doc in cursor]
    return documents


async def save_new_role(role: Role):
    collection = await get_collection()
    role_dict = role.dict()
    try:
        result = await collection.insert_one(role_dict)
        return result.inserted_id
    except Exception as e:
        return "Error al guardar el nuevo role en la base de datos: " +str(e)
