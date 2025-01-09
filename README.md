# PUMprojekt_ROWRAS
  Wykorzystanie uczenia maszynowego we wstępnej analizie użyteczności analogów cisplatyny w terapii nowotworowej

      Wymagane biblioteki:
      -pandas
      -scikit_learn
      -rdkit
      -mordred
                  UWAGA!
                  Do użycia mordred wymagany jest maksymalnie python 3.11. Nowsze wersje nie działają :(
      W repozytorium zamieściliśmy naszą bazę danych oraz uzyskane pliki .csv gotowe do użycia.
      
1. Zbierz kody SMILES odpowiednich związków w pliku .csv z przypisaną aktywnością.
2. Uruchom pum_projekt.py, aby wygenerować deskryptory.
3. Z otrzymanego pliku .csv dodaj odpowiednie etykiety z aktywnością i usuń kolumnę z kodami SMILES.
4. Uruchom PUM_projekt_v1.0.

  W przypadku chęci predykcji aktywności związków nie zawartych w naszych danych należy przygotować ich kody SMILES w podobny sposób, zmienić
  ścieżki plików w kodzie, tak aby odpowiadały one plikom .csv nowych związków i ponownie uruchomić program.
  
