
# 🚀 GitHub Actions + Docker CI/CD Guide

This guide explains how to use **GitHub Actions** with **Docker** to automate your build, test, and deployment process.


## 🔹 What are GitHub Actions?

**GitHub Actions** is a **Continuous Integration and Continuous Delivery (CI/CD)** platform that lets you automate tasks such as:

* Building and testing your code on every pull request.
* Deploying applications automatically when changes are merged.
* Running scheduled jobs (e.g., nightly builds).

---

## 🔑 Key Components of GitHub Actions

| Component    | Description                                                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Workflow** | An automated process defined in a `.yml` file inside `.github/workflows/`.                                                                     |
| **Event**    | An activity that triggers a workflow (e.g., `push`, `pull_request`, `workflow_dispatch`).                                                      |
| **Job**      | A set of steps executed on the same runner. Jobs run in parallel by default.                                                                   |
| **Step**     | A single task inside a job (e.g., run a command, use an action).                                                                               |
| **Action**   | A reusable command (from GitHub Marketplace or custom).                                                                                        |
| **Runner**   | The server that executes your jobs. GitHub provides hosted runners (`ubuntu-latest`, `windows-latest`, etc.), or you can use self-hosted ones. |

---

## ⚙️ Example Workflow Explanation

```yaml
name: Example Workflow
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Run a script
        run: echo "Hello, GitHub Actions!"
```

📌 **How it works:**

1. **Trigger:** Runs on push to `main` or manual dispatch.
2. **Checkout code:** Clones repository into the runner.
3. **Set up Python:** Installs Python.
4. **Install dependencies:** Installs packages from `requirements.txt`.
5. **Run tests:** Executes `pytest`. If tests fail, deployment stops.
6. **Deploy:** SSHs into the server and redeploys the app.

---

## 🐳 Docker Integration

### **Step 1: Create a Dockerfile**

A `Dockerfile` defines how to build your app into a container image. Place it in the project root.

### **Step 2: Build the Docker Image**

```bash
docker build -t your-image-name .
```

### **Step 3: Log in to Docker Hub**

```bash
docker login
```

### **Step 4: Tag the Image**

```bash
docker tag your-image-name your-dockerhub-username/your-image-name
```

### **Step 5: Push the Image**

```bash
docker push your-dockerhub-username/your-image-name
```

✅ Your image will now be available on Docker Hub.

---

## 🤖 Automating Docker Builds with GitHub Actions

### **1. Add Docker Hub Secrets**

In your repository:
**Settings → Secrets and variables → Actions → New repository secret**

Add:

* `DOCKERHUB_USERNAME` → Your Docker Hub username
* `DOCKERHUB_TOKEN` → A Docker Hub Access Token

### **2. Add Variables**

For non-sensitive config:

* `DOCKER_IMAGE_NAME` → Example: `my-python-app`

### **3. Workflow File (`.github/workflows/docker-publish.yml`)**

```yaml
name: Build & Push Docker Image

on:
  push:
    branches: [main]

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/${{ vars.DOCKER_IMAGE_NAME }}:latest
```

---

## 🔒 GitHub Secrets vs Variables

| Feature        | **Secrets** 🔑                                      | **Variables** 📝                                  |
| -------------- | --------------------------------------------------- | ------------------------------------------------- |
| Purpose        | Store sensitive data (API keys, tokens, passwords). | Store non-sensitive config (project name, ports). |
| Encrypted?     | ✅ Yes                                               | ❌ No                                              |
| Visibility     | Hidden, cannot be viewed after saving.              | Visible to anyone with repo settings access.      |
| Access in YAML | `${{ secrets.SECRET_NAME }}`                        | `${{ vars.VARIABLE_NAME }}`                       |

---

## 📸 Visual Reference

Here are some GitHub screenshots for **Secrets** and **Variables** setup:

![Secrets Example](https://github.com/user-attachments/assets/4e8301d9-5848-471b-a89c-d5a6e9cb4ebd)
![Variables Example](https://github.com/user-attachments/assets/3bb09f99-b56e-4b4b-84ee-f5fd9a94c1b2)
![Docker Build](https://github.com/user-attachments/assets/ebbb19bd-5efd-4801-b61f-823a68dfefe1)

---

## ✅ Final Notes

* Use **Secrets** for sensitive credentials (Docker tokens, SSH keys).
* Use **Variables** for non-sensitive configuration (image names, ports).
* Always **test workflows locally** (via Docker or `act`) before pushing.
* Start small: run tests first, then add deployment steps.


Dev.to Article: https://lnkd.in/gX8En2iV
