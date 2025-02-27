# main.py
# Importing the necessary modules from the ALOHa package for evaluation
from src.aloha.metrics import ALOHa  # ALOHa metric for evaluating hallucination in object detection
from src.aloha.object_parser import GPT35TurboObjectParser  # Object parser based on GPT-3.5 Turbo for object extraction
from src.aloha.string_similarity import MPNetSimilarity  # MPNet-based similarity measure for comparing captions

# Initialize the ALOHa metric evaluator
# ALOHa is a modern open-vocabulary metric designed to measure object hallucinations
# It uses a large language model to extract objects and compare them with reference captions and object detections
evaluator = ALOHa(
    name="aloha",  # Name identifier for the metric
    object_parser=GPT35TurboObjectParser,  # The parser to extract objects from captions
    similarity_measure=MPNetSimilarity,  # The similarity function used to measure semantic similarity
    num_reference_examples=3,  # Number of reference examples to consider for comparison
    num_target_examples=3,  # Number of target examples to evaluate
    detect_objects=True,  # Whether to detect objects in the image
)

# Example candidate caption generated by a model
candidate_caption = "bridge, river, water"

# Reference captions that contain ground-truth object descriptions
reference_captions = ["river, bridge, water, man, woman"]

# Optional parameters for providing an image path and precomputed object detections (if available)
optional_image_path = None  # If an image is available, you can provide its path here
optional_precomputed_detections = None  # Precomputed object detections can be passed if available

# Compute the ALOHa score
# The evaluator computes the hallucination score by comparing the candidate caption with reference captions
# It uses object detection and semantic similarity to determine how well the candidate caption matches
score, matches = evaluator(
    target=candidate_caption,  # Candidate caption to be evaluated
    references=reference_captions,  # Ground-truth captions to compare against
    image_path=optional_image_path,  # Optional image for object detection
    object_detections=optional_precomputed_detections  # Optional precomputed object detections
)

# Print the computed score
# The score indicates how well the candidate caption aligns with the reference in terms of object presence and description
print(score)  # Example output: 0.6081229448318481
