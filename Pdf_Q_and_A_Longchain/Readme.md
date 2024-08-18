# :sparkles: PDF Question and Answer Application -- you can upload any PDF and ask questions about it.

This is a RAG application, which uses the uploaded document as a extra knowledge to answer your questions.

# 1 | The Application UI:
1. This is a single page web application, looks like this:

2. You can upload any PDF and ask questions about it, The LLM which integrated in the backend will analyze the document and answer your questions.


# 2 | Skills Used
- 1. RAG
- 2. LLM
- 3. Python
- 4. Docker
- 5. React JS
- 6. FastAPI

# 3 | How to Use.
- 1. Run the docker containers using the below command:

This will pull the Docker image from the Docker repository and run it.
```
docker run -d --name "noso_api" -p 127.0.0.1:8000:8000  pavithra495/pdf_qa_api
docker run -d --name "noso_ui" -p 127.0.0.1:3000:3000  pavithra495/pdf_qa_ui
```
containers:
```
(gen_ai_projects) pavithra@pmurugesan-lnx1:~/projects/GenAI/Pdf_Q_and_A_Longchain$(git_branch)$ docker ps
CONTAINER ID   IMAGE                    COMMAND       CREATED          STATUS          PORTS                      NAMES
2da2c21237d1   pavithra495/pdf_qa_ui    "/start.sh"   2 seconds ago    Up 2 seconds    127.0.0.1:3000->3000/tcp   noso_ui
9231dc8ee377   pavithra495/pdf_qa_api   "/start.sh"   18 seconds ago   Up 17 seconds   127.0.0.1:8000->8000/tcp   noso_api
(gen_ai_projects) pavithra@pmurugesan-lnx1:~/projects/GenAI/Pdf_Q_and_A_Longchain$(git_branch)$
```
- 2. Now you can go to **localhost:3000** to see the Web page and start interacting.

# 4 | Places to improve :arrow_up:
- 1. Make a mechanism to upload more document at the same time.
- 2. Improve logging for better error handling.
- 3. For UI, I can add the loading indicator when I submit a question.