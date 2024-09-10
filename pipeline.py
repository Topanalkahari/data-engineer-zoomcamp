import sys
import pandas #tidak perlu untuk saat ini (Hanya contoh)

# mencetak argumen
print(sys.argv)

# Argumen 0 adalah nama file
# Argumen 1 berisi argumen pertama yang sebenarnya kita perlukan
day = sys.argv[1]

# Tampilkan kalimat dengan argumen
print(f'job finished successfully for day = {day}')