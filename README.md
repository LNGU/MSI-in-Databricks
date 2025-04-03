# Using user-managed identity in Azure Databricks
*Disclaimer*  this MSI solution does not work with managed storage that was created with Databricks. This solution works with external storages (standalone storages)

## problem
You cannot use secrets or certificates anymore because your security stance are restricter now. your option is federated identity setup using managed identity.
With Azure databricks, MI is not supported without Unity Catalog and you cannot enable Unity Catalog for some reason.

### Pre-requisites
1. make sure you have user assigned identity created in managed resource - it's named dbmanagedidentity
2. Assign RBAC to the above MSI. (e.g. reader, storage blob data reader, storage blob contributor)
3. For federated identity only, make sure MSI is added to your app registration

## 3 samples are provided : 
1. Under spark conf, using the MSI to talk to a standalone storage (dbutils, delta, etc.)
2. Using Azure identity, using the MSI to talk to a blob
3. In case you can't move away from app registration, there is a sample using Federated identity credentials. It explains app registration without secret via confidential client auth flow

## FAQ
Q : I got an error related to softDelete. what do I do? \
A : go to your storage settings and uncheck enable softdelete option. this one only happens with using Spark. If unchecking the setting is not an option, explore other ways to connect such as Azure Blob SDK.
