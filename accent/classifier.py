# Accent classification
"""
Function:
- classify_accent
"""

from speechbrain.pretrained import EncoderClassifier


def classify_accent(audio_path: str):
    """
    Run accent classification on a 16 kHz mono WAV file.
    Returns predicted accent label, index, confidence score, and full prediction.
    """
    classifier = EncoderClassifier.from_hparams(
        source="Jzuluaga/accent-id-commonaccent_ecapa",
        savedir="pretrained_models/accent_id",
    )

    prediction = classifier.classify_file(audio_path)

    predicted_label = prediction[3][0]  # label string
    predicted_index = prediction[2][0].item()  # class index
    confidence_score = prediction[0][0][predicted_index].item() * 100  # percent

    return predicted_label, predicted_index, confidence_score, prediction
