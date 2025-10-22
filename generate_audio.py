from gtts import gTTS
import os
import zipfile

os.makedirs("audio", exist_ok=True)

letters = [chr(i) for i in range(65, 91)]

ipa_examples = {
    "iː": "see", "ɪ": "sit", "e": "pen", "æ": "cat", "ʌ": "cup",
    "ɑː": "father", "ɒ": "hot", "ɔː": "law", "ʊ": "book", "uː": "food",
    "ɜː": "bird", "ə": "ago", "eɪ": "name", "aɪ": "my", "ɔɪ": "boy",
    "aʊ": "now", "əʊ": "go", "ɪə": "near", "eə": "hair", "ʊə": "tour",
    "p": "pen", "t": "ten", "k": "cat", "f": "fish", "θ": "think",
    "s": "sun", "ʃ": "she", "tʃ": "chair", "h": "hat", "b": "bat",
    "d": "dog", "g": "go", "v": "van", "ð": "this", "z": "zoo",
    "ʒ": "measure", "dʒ": "jump", "m": "man", "n": "nose", "ŋ": "sing",
    "l": "leg", "r": "red", "j": "yes", "w": "we"
}

# 生成字母发音
for letter in letters:
    tts = gTTS(text=letter, lang='en', tld='us')
    tts.save(f"audio/{letter}.mp3")

# 生成音标发音
for symbol, word in ipa_examples.items():
    tts = gTTS(text=word, lang='en', tld='us')
    tts.save(f"audio/{symbol}.mp3")

# 打包为 zip 文件
with zipfile.ZipFile("audio.zip", "w") as zipf:
    for root, _, files in os.walk("audio"):
        for file in files:
            zipf.write(os.path.join(root, file))
print("✅ audio.zip created successfully!")
