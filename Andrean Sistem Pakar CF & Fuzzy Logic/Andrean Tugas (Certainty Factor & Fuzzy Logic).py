# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_TkVF3F3ws316h4DcBbuViWJv7thUs-E
"""

gejala_user = {
    "demam": 0.2,
    "mual": 0.3,
    "diare": 0.2,
    "mata_berair": 0.6,
    "gatal_hidung": 0.5,
    "keringat_dingin": 0.4,
    "pegal": 0.6,
    "kesulitan_tidur": 0.5
}

pengetahuan = {
    "flu": {
        "demam": 0.8,
        "mual": 0.4,
        "diare": 0.3,
        "mata_berair": 0.5,
        "gatal_hidung": 0.6,
        "keringat_dingin": 0.5,
        "pegal": 0.7,
        "kesulitan_tidur": 0.4
    }
}

def hitung_cf(gejala_user, pengetahuan_pakar):
    cf_total = 0
    first = True
    for gejala, cf_user in gejala_user.items():
        if gejala in pengetahuan_pakar:
            cf_pakar = pengetahuan_pakar[gejala]
            cf = cf_user * cf_pakar
            if first:
                cf_total = cf
                first = False
            else:
                cf_total = cf_total + cf * (1 - cf_total)
    return cf_total

cf_flu = hitung_cf(gejala_user, pengetahuan["flu"])
print(f"CF diagnosis Flu: {cf_flu:.2f}")

# PENJELASAN (versi rephrased):
# Dengan menambahkan lima gejala baru, perhitungan kombinasi CF menjadi semakin rumit.
# Perhitungan tetap dimulai dari gejala "demam" yang bernilai 0.2 * 0.8 = 0.16.
# Karena nilainya cukup kecil, maka kontribusi gejala-gejala lain dihitung dengan memperhatikan sisa ketidakpastian,
# yaitu dikalikan dengan (1 - nilai CF sebelumnya).
# Setiap gejala tambahan seperti "mata_berair", "pegal", dan lainnya memberikan kontribusi terhadap CF total.
# Namun, seberapa besar penambahannya tergantung dari ruang sisa keyakinan yang tersedia.
# Jika CF sudah tinggi, kontribusi baru akan kecil. Tapi jika dimulai dari nilai rendah, dibutuhkan lebih banyak gejala untuk menaikkan CF secara signifikan.

!pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

suhu = np.arange(20, 41, 0.1)
kelembaban = np.arange(0, 101, 1)

rendah = fuzz.trimf(suhu, [20, 20, 28])
nyaman = fuzz.trimf(suhu, [25, 28, 31])
panas = fuzz.trimf(suhu, [30, 35, 40])

kering = fuzz.trimf(kelembaban, [0, 0, 50])
lembab = fuzz.trimf(kelembaban, [30, 60, 90])
sangat_lembab = fuzz.trimf(kelembaban, [70, 100, 100])

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(suhu, rendah, 'b', label='Rendah')
plt.plot(suhu, nyaman, 'g', label='Nyaman')
plt.plot(suhu, panas, 'r', label='Panas')
plt.title('Fuzzy Set Suhu')
plt.xlabel('Suhu (°C)')
plt.ylabel('Keanggotaan')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(kelembaban, kering, 'c', label='Kering')
plt.plot(kelembaban, lembab, 'm', label='Lembab')
plt.plot(kelembaban, sangat_lembab, 'y', label='Sangat Lembab')
plt.title('Fuzzy Set Kelembaban')
plt.xlabel('Kelembaban (%)')
plt.ylabel('Keanggotaan')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

input_suhu = 22
input_kelembaban = 75

suhu_rendah = fuzz.interp_membership(suhu, rendah, input_suhu)
suhu_nyaman = fuzz.interp_membership(suhu, nyaman, input_suhu)
suhu_panas = fuzz.interp_membership(suhu, panas, input_suhu)

kelembaban_kering = fuzz.interp_membership(kelembaban, kering, input_kelembaban)
kelembaban_lembab = fuzz.interp_membership(kelembaban, lembab, input_kelembaban)
kelembaban_sangat_lembab = fuzz.interp_membership(kelembaban, sangat_lembab, input_kelembaban)

angin_gelebug_pelan = np.fmin(suhu_rendah, kelembaban_kering)
angin_gelebug_normal = np.fmin(suhu_nyaman, kelembaban_lembab)
angin_gelebug_ekstra = np.fmin(suhu_rendah, kelembaban_sangat_lembab)
angin_gelebug_cepat = np.fmin(suhu_panas, kelembaban_lembab)

print(f'Derajat keanggotaan suhu {input_suhu}°C:')
print(f'- Rendah: {suhu_rendah:.2f}')
print(f'- Nyaman: {suhu_nyaman:.2f}')
print(f'- Panas: {suhu_panas:.2f}')
print(f'Derajat keanggotaan kelembaban {input_kelembaban}%:')
print(f'- Kering: {kelembaban_kering:.2f}')
print(f'- Lembab: {kelembaban_lembab:.2f}')
print(f'- Sangat Lembab: {kelembaban_sangat_lembab:.2f}')
print(f'Output aturan Angin Gelebug:')
print(f'- Pelan: {angin_gelebug_pelan:.2f}')
print(f'- Normal: {angin_gelebug_normal:.2f}')
print(f'- Ekstra: {angin_gelebug_ekstra:.2f}')
print(f'- Cepat: {angin_gelebug_cepat:.2f}')

# PENJELASAN:
# Saat input suhu 22°C, derajat keanggotaan tertinggi berada di kategori "Rendah".
# Karena kelembaban bernilai 75%, maka masuk ke kategori "Sangat Lembab".
# Kombinasi suhu rendah dan kelembaban sangat lembab menghasilkan output "Angin Gelebug Ekstra".
# Ini menunjukkan bahwa sistem dapat mengatur kecepatan kipas/AC secara lebih tepat sesuai kondisi.
# Kurva fuzzy yang saling tumpang tindih memungkinkan input seperti suhu 28°C memiliki keanggotaan di dua kategori,
# membuat sistem bisa memberikan keputusan yang lebih fleksibel dan realistis.