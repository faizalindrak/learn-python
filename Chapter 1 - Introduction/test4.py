#import library
from datetime import datetime
import random

# ganti dengan sebuah nama
nama  = "Faizal Indra kusmawan"
# variabel tanggal
tanggal = datetime.now().day
# default variabel untuk pertanyaan tidak diketahui
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

# Membuat objek dictionary berisi berbagai opsi jawaban

# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
      "nama saya  {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
    ]

# opsi pertanyaan yang bisa dijawab
pertanyaan = {
  "nama kamu siapa?": jawaban_nama,
  "kamu siapa?" : jawaban_nama,
  "tanggal berapa hari ini?": jawaban_tanggal,
  "hari ini tanggal berapa?" : jawaban_tanggal,
  "default": default
}

# list jawaban untuk sebuah argument selain pertanyaan
statement =  [
                  'ceritakan lebih banyak!',
                  'kenapa kamu berpikir begitu?',
                  'sudah berapa lama kamu merasa seperti ini?',
                  'Itu sangat menarik!',
                  'oh wow!',
                  ':)'
              ]

# respon keseluruhan
responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement
}
#------
             
# ayo buat chatbotmu
def chatbot(message):
    if message == 'Selamat pagi':
        responses['statement']
        return random.choice(statement)
    elif message == 'Mau bermain bersamaku?':
        responses['pertanyaan']
        if default in pertanyaan.values():
          return default
    elif message == 'nama kamu siapa?':
        responses['pertanyaan']
        if jawaban_nama in pertanyaan.values():
          return random.choice(jawaban_nama)
    elif message == 'hari ini tanggal berapa?':
        responses['pertanyaan']
        if jawaban_tanggal in pertanyaan.values():
          return random.choice(jawaban_tanggal)
print(chatbot('Selamat pagi'))
print(chatbot('Mau bermain bersamaku?'))
print(chatbot('nama kamu siapa?'))
print(chatbot('hari ini tanggal berapa?'))
