# Using user-managed identity in Azure Databricks
#securingAzure \
*Disclaimer*  this MSI solution does not work with the managed storage that is created with Databricks managed resource group, as it is not recommended to be used as a normal storage. The storage is more like a cache for compute. \
This solution works with external Azure storages (standalone storages), preferably within the same subscription. \
This solution does not work with mounting. 

## Problem
You cannot use secret or certificate anymore because your security stance are restricter now. Your option is federated identity setup using managed identity.
With Azure databricks, MSI is not supported without Unity Catalog and you cannot enable Unity Catalog for some reason.

### Pre-requisites
1. make sure you have a user assigned identity created in the managed resource - it's named dbmanagedidentity
2. Assign RBAC permission to the MSI in the storage. or, you can use Azure role assignments (e.g. reader, storage blob data reader, storage blob contributor)
3. For federated identity only, make sure MSI is added to your app registration (aka. SPN)

## 3 samples are provided : 
1. Under spark conf, using the MSI to talk to a standalone storage (dbutils, delta, etc.). you must add RBAC as managed identity, not as a SPN - you cannot add as MSI, only SPN, when you don't have access to the subscription where the msi resides.
2. Using Azure identity, using the MSI to talk to a blob
3. In case you can't move away from app registration, there is a sample using Federated identity credentials. It explains app registration without secret via confidential client auth flow

## FAQ
Q : I got an error related to softDelete. what do I do? \
A : go to your storage settings and uncheck enable softdelete option. this one only happens with using Spark. If unchecking the setting is not an option, explore other ways to connect such as Azure Blob SDK. \
Q : I don't have access to the subscription and cannot add as MSI, what do I do? \
A : you can use Azure identity code but not able to use spark based code. so you have to use a different libraries such as Python deltalake. \
