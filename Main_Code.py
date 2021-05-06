# Create your own Image and Audio Captcha

# For Image Captcha
from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)

data = image.generate('github2104klop')

image.write('github2104klop','create Captcha2.png')


# For Audio Captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

data1 = audio.generate('406')

audio.write('406', 'Create Audio Captcha1.wav')