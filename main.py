from src.aloha.metrics import ALOHa
from src.aloha.object_parser import GPT35TurboObjectParser
from src.aloha.string_similarity import MPNetSimilarity

# Initialize the ALOHa metric
evaluator = ALOHa(
    name="aloha",
    object_parser=GPT35TurboObjectParser,
    similarity_measure=MPNetSimilarity,
    num_reference_examples=3,
    num_target_examples=3,
    detect_objects=True,
)

candidate_caption = "bridge, river, water"
reference_captions = ["river, bridge, water, man, woman "]
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
# 0.6081229448318481

