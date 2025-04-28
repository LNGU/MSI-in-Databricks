from azure.storage.blob import BlobServiceClient
from azure.identity import ManagedIdentityCredential

# Azure Data Lake Storage Gen2 details
account_name = "your_azure_storage_name"
container_name = "your_blob_container_name"
file_path = "your_csv_file_name" #for this sample, use a csv file
client_id = "your_MSI_client_id"

# Construct the Blob Service Client using Managed Identity
credential = ManagedIdentityCredential(client_id=client_id) 
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=credential)

# Get the Blob Client for the specific file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)

# Download the file content
downloaded_blob = blob_client.download_blob()
file_content = downloaded_blob.readall()

# Print the file content
print(file_content.decode("utf-8"))
