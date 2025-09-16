% --------------------------
% Knowledge Base: Symptoms & Diseases
% --------------------------

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(headache),
    symptom(sore_throat).

disease(common_cold) :-
    symptom(runny_nose),
    symptom(cough),
    symptom(sneezing).

disease(typhoid) :-
    symptom(fever),
    symptom(abdominal_pain),
    symptom(loss_of_appetite).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

disease(covid19) :-
    symptom(fever),
    symptom(cough),
    symptom(loss_of_smell),
    symptom(breathing_difficulty).

% --------------------------
% Ask for Symptoms Dynamically
% --------------------------

symptom(S) :-
    format('Do you have ~w? (yes/no): ', [S]),
    read(Reply),
    (Reply == yes -> assert(symptom(S)) ; fail).

% --------------------------
% Main Diagnosis Rule
% --------------------------

diagnose :-
    disease(Disease),
    format('You may have: ~w~n', [Disease]),
    fail.  % force backtracking to show all possibilities

diagnose :-
    write('Diagnosis complete.').
