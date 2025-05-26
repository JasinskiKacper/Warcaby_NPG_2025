# Warcaby_NPG_2025
  Projekt na Narzędzia Pracy Grupowej
#Wymagania sprzętowe i założenia projektu
  Celem projektu jest stworzenie gry planszowej "Warcaby" z interfejsem graficznym w środowisku Python.
  Będzie ona korzystała z interfejsu graficznego, który zapewnia biblioteka tkinter, tworząc przyjemny intefejs dla gracza.
  Głównym założeniem jest możliwość ciągłego rozwoju i łatwość rozbudowy, w przyszłości gra będzie pozwalała na
  dodatnie takich opcji jak tryb jednoosobowy z AI, rozgrywka wieloosobowa jak i tych mniejszych dotyczących
  np stylu graficznego czy dodania licznika czasu.

  Gra będzie oparta na prostym GUI (w tym przypadku tkinter), brak to złożonych obliczeń, grafiki 3D. Może działać nawet na archaicznym sprzęcie.

    System: Windows 10, Linux 22.04LTS, macOS 12;
      tutaj może być dowolny z obsługą GUI i pozwalający na zainstalowanie pythona w wersji 3.7 i nowszej, 
      (pełne wsparcie dla popularnym konstrukcji składniowych). Windows 10 jest zalecany ponieważ jest nadal wspierany przez Microsoft, 
      a to zapewnia bezpieczeństwo. Dla innych wyżej wymienionych systemów operacyjnych sprawa ma się podobnie. 
      Starsze wersje mogą mieć problemy z biblioteką tkinter i wsparciem dla Pythona.
      
      

    Grafika: Zintegrowana lub GT710 (Nvidia) lub HD6450 (Radeon);
      wymagania co do układu graficznego nie są duże, gra nie obsługuję grafiki 3D czy rozbudowanego silnika
      graficznego, zadaniem grafiki będzie wyświetlenie planszy o wymiarach 640 x 640 pikseli na której będą proste
      geometryczne figury, zatem nawet stary zintegrowany układ graficzny z lat 2012 poradzi sobie bez problemów. 
      Jako zalecenie dotyczące kart dedykowanych, wymienione wyżej układy obsługują DirectX 11 i mają sterowniki do
      wskazanych wcześniej systemów, to pierwsze nie jest konieczne ale gwarantuje pełną kompatybilność z 
      nowoczesnym środowiskiem. Mimo wszystko podane wymagania muszą zagwarantować możliwość rozwoju projektu,
      które w tym przypadku jest pierwszorzędne.

    Procesor: 4 rdzenie, 2.5GHz;
      zapewnia płynną pracę systemu w tle ,np przeglądarka. Tryb gry z AI może wymagać intensywniejszych obliczeń.
      Jest to typowa specyfikacja budżetowych laptopów i PC.

    Ram: 4GB
      system operacyjny wymaga miniumum 2GB przy tym same wymagania gry są bardzo niskie (kilkanaście MB).
      Optymalnym wyborem będzie 4GB.

    Dysk: 200MB (sama gra)
      sam skrypt waży w okolicach 50KB ale do tego należy doliczyć Python,tkinter, pliki tymczasowe jak i 
      również ewentualne rozszerzenia.
      
    
  Jako domyślne przyjmujemy następujące zasady warcabów:
  - plansza 8x8 z dwoma rzędami pionków ustawionych na czarnych polach ponumerowanych od 0 do 7
  - zaczyna kolor biały
  - pionki poruszają się o jedno pole po ukosie do przodu
  - bicie jest możliwe, gdy pionek przeciwnika jest bezpośrednio o jedno pole na ukos od pionka gracza, i pole za pionkiem przeciwnika jest wolne (po biciu pionek gracza ląduje na polu za zbitym pionkiem)
  - w przypadku, gdy po zbiciu nowa pozycja gracza umożliwia kolejne zbicie w tej samej turze, gracz jest zobowiązany do wykonania takiego ruchu
  - w ogólnym przypadku bicie nie jest obowiązkowe
  - bicie w tył jest niemożliwe
  - po dojściu pionkiem do końca planszy gracz otrzymuje w zamian pionka królówkę
  - królówka może poruszać się dowolną ilość pól po ukosie, zarówno w przód jak i w tył (bicie również wykonuje w obu kierunkach)
  - nie ma ograniczenia czasowego dla wykonania ruchu
  - gra kończy się, gdy jeden z graczy nie ma już żadnych figur - wygrywa jego przeciwnik
