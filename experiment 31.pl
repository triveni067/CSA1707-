% ----------------------------
% Predicate: Count Vowels
% ----------------------------

count_vowels(String, Count) :-
    string_chars(String, Chars),       % Convert string to list of characters
    include(is_vowel, Chars, Vowels),  % Keep only vowels
    length(Vowels, Count).             % Count them

% ----------------------------
% Helper Predicate: Check Vowel
% ----------------------------

is_vowel(Char) :-
    member(Char, ['a','e','i','o','u','A','E','I','O','U']).
