# Whisper transcription logic
"""
Function:
- transcribe_audio
"""

import whisper


def transcribe_audio(
    audio_path: str, model_size: str = "base", device: str = "cpu"
) -> str:
    """
    Transcribe audio file using OpenAI's Whisper model.

    Args:
        audio_path (str): Path to the audio file.
        model_size (str): Size of the Whisper model to load ('tiny', 'base', 'small', etc.).
        device (str): Device to run the model on ('cpu' or 'cuda').

    Returns:
        str: Transcribed text from the audio.
    """
    model = whisper.load_model(model_size, device=device)
    result = model.transcribe(audio_path)
    return result["text"]


if __name__ == "__main__":
    # Example usage
    audio_file = "extracted_audio.wav"
    transcription_text = transcribe_audio(audio_file)
    print("Transcription:\n")
    print(transcription_text)
