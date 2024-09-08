## ALOHa: A New Measure for Hallucination in Captioning Models
This directory contains the implementation of ALOHa, a modern open-vocabulary metric designed to measure object hallucinations in captioning models. ALOHa utilizes large language models (LLMs) to extract groundable objects from candidate captions, measures their semantic similarity to reference captions and object detections, and employs Hungarian matching to compute a hallucination score.

ALOHa improves upon existing hallucination metrics like CHAIR by expanding beyond a fixed set of MS COCO objects and synonyms. In testing, ALOHa identified 13.6% more hallucinated objects on MS COCO Captions and 30.8% more on nocaps, demonstrating its superior performance for evaluating object hallucinations.

## Getting Started
Setup
First, install ALOHa and its dependencies:


# Install the package from GitHub
pip install git+https://github.com/DavidMChan/aloha.git

# Install the SpaCy model if you haven't already
pip install -U spacy
python -m spacy download en_core_web_lg
Usage
You can compute the ALOHa score for a single caption using the following script:


from aloha.metrics import ALOHa
from aloha.object_parser import GPT35TurboObjectParser
from aloha.string_similarity import MPNetSimilarity

# Initialize the ALOHa evaluator
evaluator = ALOHa(
    name="aloha",
    object_parser=GPT35TurboObjectParser,
    similarity_measure=MPNetSimilarity,
    num_reference_examples=3,
    num_target_examples=3,
    detect_objects=True,
)

candidate_caption = "A cat is sitting on a table"
reference_captions = ["A dog is sitting on a table", "A hound is sitting on a table"]
optional_image_path = None
optional_precomputed_detections = None

# Compute the ALOHa score
score, matches = evaluator(
    target=candidate_caption,
    references=reference_captions,
    image_path=optional_image_path,
    object_detections=optional_precomputed_detections,
)

print(score)
# Example output: 0.6081229448318481

print(matches)
# Example output:
# {'matches': [{'ref_word': 'table', 'similarity': 1.0, 'target_word': 'table'},
#              {'ref_word': 'dog',
#               'similarity': 0.6081229448318481,
#               'target_word': 'cat'}],
#  'reference_objects': [['dog'], ['table'], ['hound']],
#  'target_objects': [['cat'], ['table']]}
Evaluating a Dataset
You can also evaluate a full dataset using the evaluate-dataset script. Prepare your dataset in a JSON file with the following format:


[
    {
        "caption": "A caption",
        "references": ["Ref 1", "Ref 2", ...],
        "image_path": "path/to/image.jpg"
    },
    ...
]


Then, run the evaluation:

aloha evaluate-dataset -m aloha path/to/dataset.json
For additional options, you can run:

aloha evaluate-dataset --help


## Citation
If you find this repository useful, please cite the original ALOHa paper:

The orginial GitHub repo is given below.
https://github.com/DavidMChan/aloha

@inproceedings{petryk2024aloha,
    title = "ALOHa: A New Measure for Hallucination in Captioning Models",
    author = "Petryk, Suzanne and
              Chan, David M and
              Kachinthaya, Anish and
              Zou, Haodi and
              Canny, John and
              Gonzalez, Joseph E and
              Darrell, Trevor",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    year = "2024",
    publisher = "Association for Computational Linguistics",
}
