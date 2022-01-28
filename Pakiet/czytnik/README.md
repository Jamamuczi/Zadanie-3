Przeprowadzono pomiary dotyczące punktualności odjazdów w komunikacji miejskiej. W ramach pomiarów zebrano od osób przeprowadzających pomiary następujące dane:

    numer przystanku

    numer linii

    numer pojazdu

    data

    godzina planowa (z rozkładu)

    godzina faktycznego przyjazdu

    godzina faktycznego odjazdu

Dane zbierano zarówno przy użyciu aplikacji androidowej jak i ręcznie wpisując dane do tabeli i później wpisując je do arkusza kalkulacyjnego. Ponieważ pomiary przeprowadzane były przez wiele osób na różne sposoby następuje obawa o właściwy format danych. W efekcie końcowym pomiarów wszystkie zebrane dane dostępne są w formacie CSV.

Podjęto zatem decyzję o tym, że powstanie pakiet napisany w Pythonie, który będzie:

    wczytywać plik

    sprawdzać poprawność danych:

        czy numery przystanku i linii są poprawnymi liczbami

        czy numer/oznaczenie pojazdu jest poprawne

        czy data jest w dobrym formacie (właściwy format trzeba samemu wybrać)

        czy godzina jest w dobrym formacie (właściwy format trzeba samemu wybrać)

    dodawać kolumnę zawierającą wartość opóźnienia odjazdu

    dodawać kolumnę zawierającą czas jaki pojazd był na danym przystanku

    sprawdzony i poprawny pomiar zapisywać w pojedynczym pliku sqlite

Do wyboru są dwie opcje zadania:

    Wersja łatwiejsza to taka w której wiersze nie spełniające wymagań są zapisywane nie do pliku sqlite tylko do pliku CSV w celu ich edycji i poprawy manualnej (np. w programie typu Calc, Excel, Gnumeric itd.)

    Wersja bardziej złożona to taka w której pakiet posiada nie tylko opcję sprawdzenie danych ale też próbuje poprawić błędy formatowania w danych a dopiero dla przypadków kiedy nie jest w stanie tego zrobić następuje zapisanie tych wierszy do pliku CSV
