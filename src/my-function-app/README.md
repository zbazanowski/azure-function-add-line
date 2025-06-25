# 🔧 Azure Function App: `AddSecondLine`

This Azure Function is triggered by the creation of a blob in a source container and appends a second line to the blob content. The modified result is written to a target container.

## 🧠 Function Overview

- **Trigger Type**: `blobTrigger`
- **Input Container**: `bazcontaineruploads`
- **Output Container**: `bazcontainerprocessed`
- **File Type**: Assumes UTF-8 text

## 📂 Function Structure

```
AddSecondLine/
├── __init__.py         # Function logic
└── function.json       # Binding configuration
```

## 🔄 Processing Logic

1. Triggered when a new blob is created in the source container.
2. Reads the original content of the blob.
3. Appends a second line.
4. Writes the new content to the output container with the same blob name.

## 📐 Architecture

```
[Client Uploads Image]
         │
         ▼
┌───────────────────────────────┐
│ Azure Blob Storage            │◄─── Receives image (in `uploads/`)
└───────────────────────────────┘
         │
         ▼
┌───────────────────────────────┐
│ Azure Event Grid              │─── Detects blob creation event
└───────────────────────────────┘
         │
         ▼
┌───────────────────────────────┐
│ Azure Function (Blob Trigger) │─── Processes image
└───────────────────────────────┘
         │
         ▼
┌───────────────────────────────┐
│ Azure Blob Storage            │─── Saves to `processed/`
└───────────────────────────────┘
```

## 📎 Sample function.json

```json
{
  "bindings": [
    {
      "name": "myblob",
      "type": "blobTrigger",
      "direction": "in",
      "path": "bazcontaineruploads/{name}",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```

## 🔐 Configuration Notes

- `AzureWebJobsStorage` is defined in `local.settings.json` or App Settings in Azure.
- Both containers must exist in the same storage account.
