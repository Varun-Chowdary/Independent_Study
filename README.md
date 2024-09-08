## Independent Study - Fine-Tuning LLaVA 1.5 and Hallucination Detection
### Student: Varun Chowdary Sayapaneni
### Instructor: Prof. Naveen Kumar
### Course: DSA 5990

## Abstract
This independent study explores the fine-tuning of the LLaVA 1.5 Multimodal Large Language Model (MLLM) using the OK-VQA dataset, focusing on enhancing object detection and minimizing hallucinations. LLaVA 1.5 integrates visual and linguistic processing, making it suitable for tasks like visual question answering and image captioning. The model is fine-tuned on 9,100 training samples and tested on 5,050 samples, with an additional 250 zero-shot images to evaluate performance. Three specialized tools—ALOHa, MMHal-Bench, and GroundingDINO—were used to test and evaluate hallucinations in the model's object detection capabilities. The results show a significant improvement in detection accuracy and a reduction in hallucinations.

ALOHa: Average score of 0.886, highlighting precise object detection.

MMHal-Bench: Hallucination score of 4.428, indicating improved accuracy.

GroundingDINO: Hallucinations in only 4% of the responses, demonstrating the model's reliability.


### Folders and Structure
llava-finetune_latest
Contains the script to fine-tune the LLaVA-1.5 model. This script is specifically designed to improve the model's object detection accuracy and reduce hallucinations in its outputs.

Aloha
This folder contains the files and documentation for testing the fine-tuned model using ALOHa. ALOHa measures hallucination rates in object detection by analyzing the similarity between objects in the image and the generated text.

MMHal
The MMHal-Bench tool is used for detecting hallucinations and scoring the model based on its performance in identifying correct objects. Details on how the tool is customized for this study are provided in the folder.

GroundingDINO
GroundingDINO is a zero-shot object detection tool. The folder contains files that demonstrate the evaluation of hallucinations using this tool by comparing detected objects with ground truth.

Each directory includes further instructions and files for setting up and running the respective evaluations.

How to Run
To fine-tune the LLaVA model:

Clone the repository:


git clone https://github.com/Varun-Chowdary/Independent_Study.git
Navigate to the llava-finetune directory and run the script to start fine-tuning the model:


cd llava-finetune_latest
python finetune.py
Use the respective tools from the Aloha, MMHal, and GroundingDINO folders to evaluate the fine-tuned model’s performance.


