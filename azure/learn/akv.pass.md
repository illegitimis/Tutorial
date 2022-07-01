# Manage a password in Azure Key Vault

azure portal \
msft learn sandbox \
create a resource \
https://portal.azure.com/#create/Microsoft.KeyVault \
Create a key vault \
Concierge Subscription \
Resource group: learn-fb9aee48-e576-405d-88a2-65e4d2e8e121 \
Deployment name:password-key-vault-5 \
vault uri: https://password-key-vault-5.vault.azure.net/ \
settings - secrets sidebar \
Generate/Import \
Create a secret page

```bash
az keyvault secret set --vault-name password-key-vault-5 --name MySecretName --value MyVault

az keyvault secret show --name MyPassword --vault-name password-key-vault-5 --query value --output tsv
# "id": "https://password-key-vault-5.vault.azure.net/secrets/MyPassword"
#  "name": "MyPassword"
az keyvault secret list --vault-name password-key-vault-5
# https://password-key-vault-5.vault.azure.net/secrets/MyPassword/1e7a7e72c0e14839ab937fe74c0a0297
az keyvault secret list-versions --vault-name password-key-vault-5 --name MyPassword
az keyvault secret [delete|recover] --vault-name password-key-vault-5 --name MyPassword
```

[< LP4](4-lp-az-900.md)