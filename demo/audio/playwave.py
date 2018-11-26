import subprocess
audio_file = "message.wav"

return_code = subprocess.call(["afplay", audio_file])
