# this is the sample for FIC+MSI using Azure Identity (using SPN/app registration but wihtout secret)
from azure.identity import ClientAssertionCredential
from azure.storage.blob import BlobServiceClient

# Define necessary variables
tenant_id = "your_azure_tenant_id"  # Replace with your tenant ID
client_id = "your_app_registration_client_id_with_federated_identity"  # Replace with your app client ID/app Registration

# Define a function to get the assertion token
def get_assertion_token():
    from azure.identity import DefaultAzureCredential
    credential = DefaultAzureCredential()
    token = credential.get_token("api://AzureADTokenExchange/.default") #important scope
    Assertion_Token = token.token
    return token.token

# Create a ClientAssertionCredential instance
credential = ClientAssertionCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    func=get_assertion_token
)

# Azure Data Lake Storage Gen2 details
account_name = "your_storage_name"
container_name = "your_container_name"
file_path = "yourfile.csv"

# Get the Blob Client for the specific file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)

# Download the file content
downloaded_blob = blob_client.download_blob()
file_content = downloaded_blob.readall()

# Print the file content
print(file_content.decode("utf-8"))

container_client = blob_service_client.get_container_client(container=container_name)

# List all blobs in the container
print(f"Listing blobs in container '{container_name}':")
blobs = container_client.list_blobs()
for blob in blobs:
    print(f"- {blob.name}")