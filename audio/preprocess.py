# Audio preprocessing for accent classification
"""
Function:
- preprocess_audio
"""
# audio/preprocess.py

import torchaudio


def preprocess_audio(input_path: str, output_path: str = "processed_audio.wav"):
    """
    Converts audio to mono and 16 kHz sample rate.
    Saves the processed audio to `output_path`.
    """
    signal, sample_rate = torchaudio.load(input_path)

    # Convert to mono if stereo
    if signal.shape[0] > 1:
        signal = signal.mean(dim=0, keepdim=True)

    # Resample if needed
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(
            orig_freq=sample_rate, new_freq=16000
        )
        signal = resampler(signal)

    # Save the processed audio
    torchaudio.save(output_path, signal, 16000)
    print(f"[✓] Preprocessed audio saved to {output_path}")

    return output_path
