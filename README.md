# 📦 Project: Azure Event-Driven Blob Processor

This repository contains a minimal, production-structured implementation of an **Azure Function App** triggered directly by Azure Blob Storage.

## 🧭 Structure

```
Queue/ (repo root)
├── README.md                <- [You are here] high-level description
├── src/
│   └── my-function-app/     <- Azure Function App source code
│       ├── AddSecondLine/   <- Blob-triggered function logic
│       ├── requirements.txt
│       ├── host.json
│       ├── local.settings.json
│       ├── README.md        <- Technical details of the function
│       └── .github/workflows/deploy.yml
```

## 🎯 Purpose

This project demonstrates a **direct integration between Blob Storage and Azure Functions** without using any intermediate queue. It serves as a baseline before introducing more scalable patterns like Azure Queue Storage or Event Grid routing.

## 🚀 Deployment

Deployment is handled via GitHub Actions. On push to `main`, the function app is automatically published to Azure using a publish profile secret.

To deploy manually:
```bash
func azure functionapp publish <your-function-app-name>
```

## 🔄 What Happens

1. A blob is uploaded to a monitored container (e.g., `bazcontaineruploads`).
2. The function `AddSecondLine` is triggered automatically.
3. The content is read, a line is appended, and the result is saved to a second container (e.g., `bazcontainerprocessed`).

## 🧰 Technologies Used

- Azure Blob Storage
- Azure Functions (Python)
- GitHub Actions
- Azure CLI

## 📌 Next Steps

The next version of this project will introduce:
- Azure Queue Storage as a decoupling layer
- Event Grid custom routing
- Durable Functions or logic fan-out

---

📝 See [`src/my-function-app/README.md`](src/my-function-app/README.md) for in-depth function details.
