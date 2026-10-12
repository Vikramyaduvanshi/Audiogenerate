import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Load API key
load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

# Hindi story narration
text = """
एक रात, एक सुनसान गाँव में,
एक अजीब सी आवाज़ सुनाई दी।
लेकिन उस आवाज़ के पीछे जो राज़ था,
वो किसी ने सोचा भी नहीं था।
"""

# Generate voice
audio = client.text_to_speech.convert(
    text=text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128"
)

# Save audio file
with open("story.mp3", "wb") as file:
    for chunk in audio:
        file.write(chunk)

print("Voice generated successfully!")
print("Saved as story.mp3")