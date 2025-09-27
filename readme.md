## This project's whole purpose is to run LLMs locally and to make use of them using RestAPI in Python using - FastAPI.

## Requirements

1. Docker installed on your system.
2. Ollama as a Docker image, running as a container.
3. OpenWebUI image running as a container.
4. After installing both, Ollama backend should be on port `11434` and OpenWebUI interface on port `3000`.
5. Login to OpenWebUI and download any required open-source model from Ollama.  
   [OpenWebUI Installation Guide](https://docs.openwebui.com/getting-started/quick-start/)

---

## Clone the Repository & Install Dependencies

First, clone this repository and install the Python dependencies listed in `requirements.txt`.

````bash
git clone https://github.com/Shailesh2003-arch/Running_LLM_Locally.git
cd Running_LLM_Locally

# Install requirements
pip install -r requirements.txt

## Precise instructions: step-by-step guide to install OpenWebUI on Docker

**Step 1: Pull the latest OpenWebUI Docker image**
using the command :

```bash
docker pull ghcr.io/open-webui/open-webui:main
````

![Pull image from dockerhub](src/assets/images/pull_OpenWebUI.png)

step 2: Run the Container.
Run the container with default settings. This command includes a volume mapping to ensure persistent data storage.
using the command :

```bash
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

![Run the container](src/assets/images/run_OpenWebUI.png)

After successfull run of the ollama container you'll see something as:
![Running backend of Ollama on Port localhost:11434](src/assets/images/localhost_running.png)

After successfull run of the OpenWebUI container you'll see something as:
![Running User-Interface of OpenWebUI on Port localhost:3000](src/assets/images/OpenWebUI_running.png)

Run the FastAPI Server ⚡
Inside the src directory using the command:

```bash
fastapi dev server.py
```

By default, FastAPI will start on port 8000

visit: Swagger UI (API Docs): 👉 http://localhost:8000/docs

Here you can interactively test endpoints and check the model’s responses in real time.

Attaching some images for reference:

You can ask your required query to the model:
![query - who are you?](src/assets/images/interacting_via_FastAPI_with_Ollama_server.png)

Model responds back with the answer:
![Response from the model](src/assets/images/response_from_the_model.png)
