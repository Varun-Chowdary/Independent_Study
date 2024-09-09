## Running the Script

Use the following command to run the script.


python eval_gpt4.py --response "response_mymodel.json" --api-key "your_openai_api_key"

This script evaluates Large Multimodal Model (LMM) responses using OpenAI's GPT-4 model. The script compares LMM responses against ground-truth (human-generated) answers to detect hallucinations, providing a rating based on informativeness and hallucination occurrence.

Parameters:
--response: Path to the JSON file containing model responses.
--api-key: Your OpenAI API key.
--evaluation (optional): Path to save evaluation results.
--gpt-model (optional): GPT model to use (default: gpt-4).
