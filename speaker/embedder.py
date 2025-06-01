# Speaker embedding extraction
"""
Function:
- get_speaker_embedding
"""

import torchaudio
from speechbrain.pretrained import SpeakerRecognition


def get_speaker_embedding(audio_path: str):
    """
    Load audio file and return speaker embedding vector.
    Ensures audio is 16kHz mono.
    """
    # Load pretrained model
    model = SpeakerRecognition.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="models/spkrec-ecapa-voxceleb",
    )

    # Load audio
    signal, fs = torchaudio.load(audio_path)

    # Resample and convert to mono if needed
    if fs != 16000:
        resampler = torchaudio.transforms.Resample(fs, 16000)
        signal = resampler(signal)
    if signal.shape[0] > 1:
        signal = signal.mean(dim=0, keepdim=True)

    # Get embedding (tensor)
    embedding = model.encode_batch(signal)

    # Return as numpy array (flattened)
    return embedding.squeeze().cpu().numpy()
