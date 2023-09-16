   from elevenlabs import generate, play, set_api_key, save

            voice = generate(
                text=f"{cop}",
                voice="Bella",
                model="eleven_multilingual_v2"
            )
            save(voice,'data.mp3')
#just ading this in palce of speak
