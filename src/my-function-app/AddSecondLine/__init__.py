import logging
import os
from azure.functions import InputStream
from azure.storage.blob import BlobServiceClient

def main(myblob: InputStream):
    print("AZURE CONNECTION:", os.environ.get("AzureWebJobsStorage"))
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Read original content
    original_content = myblob.read().decode('utf-8')
    
    # Append a second line
    modified_content = original_content + "\nThis is the second line."

    # Prepare to upload to a second container
    connection_string = os.environ["AzureWebJobsStorage"]
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    target_container = "bazcontainerprocessed"
    target_blob_name = os.path.basename(myblob.name)
    blob_client = blob_service_client.get_blob_client(container=target_container, blob=target_blob_name)

    # Upload modified content
    blob_client.upload_blob(modified_content, overwrite=True)