% ----------------------------
% Predicate: match/2
% match(Pattern, String) succeeds if Pattern matches String
% ----------------------------

% Case 1: Both lists are empty -> match
match([], []).

% Case 2: Match first character and continue
match([H|TPattern], [H|TString]) :-
    match(TPattern, TString).

% Case 3: '_' acts as a wildcard that can match any single character
match(['_'|TPattern], [_|TString]) :-
    match(TPattern, TString).
