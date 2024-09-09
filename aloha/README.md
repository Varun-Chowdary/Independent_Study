## ALOHa: A New Measure for Hallucination in Captioning Models
This script demonstrates how to compute the ALOHa score, a metric designed to evaluate hallucinations in captioning models by comparing candidate captions with reference captions and object detections.

Refer to main.py for the code.

## Setup:

Install ALOHa and dependencies.

pip install git+https://github.com/DavidMChan/aloha.git
pip install -U spacy
python -m spacy download en_core_web_lg

Usage:
To compute the ALOHa score, execute the following command:
python main.py


main.py

from src.aloha.metrics import ALOHa
from src.aloha.object_parser import GPT35TurboObjectParser
from src.aloha.string_similarity import MPNetSimilarity

# Initialize ALOHa evaluator
evaluator = ALOHa(
    name="aloha",
    object_parser=GPT35TurboObjectParser,
    similarity_measure=MPNetSimilarity,
    num_reference_examples=3,
    num_target_examples=3,
    detect_objects=True,
)

candidate_caption = "bridge, river, water"
reference_captions = ["river, bridge, water, man, woman"]

# Compute the ALOHa score
score, _ = evaluator(target=candidate_caption, references=reference_captions)
print(score)


## Citation:
Please cite the original ALOHa paper if you use this work:

@inproceedings{petryk2024aloha, title = "ALOHa: A New Measure for Hallucination in Captioning Models", 
author = "Petryk, Suzanne and Chan, David M and others", 
year = "2024", publisher = "ACL", }

Refer to the Official GitHub link- https://github.com/DavidMChan/aloha
