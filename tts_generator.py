import tempfile
import scipy.io.wavfile
from pocket_tts import TTSModel

class TTSGenerator:
    def __init__(self):
        self.model = None

    def load_model(self):
        if self.model is None:
            self.model = TTSModel.load_model()
        return self.model

    def generate_from_text(self, text, voice="alba", voice_file=None):
        """
        Gera áudio a partir do texto.
        voice: nome de uma voz pré-definida ("alba", "marius", etc.) ou None se for clonagem.
        voice_file: caminho para arquivo WAV para clonagem (se fornecido, override a voice).
        """
        model = self.load_model()
        if voice_file:
            # clonagem
            voice_state = model.get_state_for_audio_prompt(voice_file)
        else:
            # voz pré-definida
            voice_state = model.get_state_for_audio_prompt(voice)

        audio = model.generate_audio(voice_state, text)
        # Salvar em arquivo temporário
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            scipy.io.wavfile.write(tmp.name, model.sample_rate, audio.numpy())
            return tmp.name
        
        