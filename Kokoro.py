from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code="h")


# text = """
# एक रात... एक सुनसान गाँव में, एक अजीब-सी आवाज़ सुनाई दी लेकिन... उस आवाज़ के पीछे जो राज़ था, वो किसी ने सोचा भी नहीं था।
# """
text = """
आशीष के पिछले 1 महीने से 4 असाइनमेंट पेंडिंग हैं। प्लीज़ उनसे कहें कि वे अगले 2 दिनों में अपने सभी पेंडिंग असाइनमेंट पूरे कर लें।अगर अगले 2 दिनों में असाइनमेंट पूरे नहीं हुए, तो ऑर्गनाइज़ेशन ज़रूरी और सख़्त एक्शन ले सकती है।प्लीज़ इस मामले को सीरियसली लें और आशीष को असाइनमेंट समय पर पूरे करने में सपोर्ट करें।
"""

generator = pipeline(text, voice="hm_psi")

for i, (_, _, audio) in enumerate(generator):
    sf.write(f"ashish2_{i}.wav", audio, 24000)

print("Hindi voice generated!")




# lang_code="h" → Hindi
# hf_alpha → Hindi female
# hf_beta → Hindi female
# hm_omega → Hindi male
# hm_psi → Hindi male