#may not work with a storage outside of your own subscription due to SPN adding not MSI itself.
#user assigned MSI -> dbmanagedidentity
#Working sample - using managed identity with spark conf ... variable substituted
standalone_storage_account_name = "your_azure_storage_name_here" #do not use storage that is inside your managed resource group. it does not work as of 4/1/2025
container_name = "your_blob_container_name"
file_path = "your_csv_file_name" #for this sample, use a csv file.
client_id = "your_client_id_of_the_MSI_named_dbmanagedidentity"
tenant_id = "your_own_tenant_id_here"


spark.conf.set("fs.azure.account.auth.type."+standalone_storage_account_name+".dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type."+standalone_storage_account_name+".dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.MsiTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id."+standalone_storage_account_name+".dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.msi.tenant."+standalone_storage_account_name+".dfs.core.windows.net", tenant_id)

df = (spark.read
  .format("csv")
  .option("mode", "PERMISSIVE")
  .load("abfss://"+container_name+"@"+standalone_storage_account_name+".dfs.core.windows.net/"+file_path)
)
df.show()
