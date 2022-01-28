#!/home/studentb07/.local/share/virtualenvs/sprawozdanie-5D_5EEiY/bin/python
import czytnik

# Załadowanie danych z pliku. "data" jest listą zawierającą linie wczytanego pliku
data = czytnik.load_data_from_file("Zad_3.csv")
# Przetworzenie danych z pliku
items_ok, items_nok = czytnik.parse_data(data)
# Obliczanie opóźnienia i czasu postoju
czytnik.calc_delay_and_layover_time(items_ok)
# Zapis do pliku SQLite
czytnik.save_to_sqlite("result.sqlite3", items_ok)
# Zapis do pliku CSV
czytnik.save_to_csv("Not_ok.csv", items_nok)

# Wyświetlenie statystyk
print("Items loaded: " + str(len(items_ok) + len(items_nok)))
print("Correct data: " + str(len(items_ok)))
print("Incorrect data: " + str(len(items_nok)))
