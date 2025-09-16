% ----------------------------
% Knowledge Base: Graph + Heuristic
% ----------------------------

% Graph edges: edge(Node, Neighbor, Cost)
edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 5).
edge(b, e, 3).
edge(c, f, 4).
edge(c, g, 6).
edge(e, h, 2).

% Heuristic values (estimated cost to goal)
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 4).
heuristic(d, 5).
heuristic(e, 2).
heuristic(f, 3).
heuristic(g, 6).
heuristic(h, 0).  % goal node

% ----------------------------
% Best First Search Algorithm
% ----------------------------

best_first_search(Start, Goal, Path) :-
    best_first([[Start]], Goal, Path).

best_first([[Goal|RestPath]|_], Goal, FinalPath) :-
    reverse([Goal|RestPath], FinalPath).

best_first([CurrentPath|OtherPaths], Goal, FinalPath) :-
    CurrentPath = [CurrentNode|_],
    findall([NextNode|CurrentPath],
            (edge(CurrentNode, NextNode, _),
             \+ member(NextNode, CurrentPath)),
            NewPaths),
    evaluate_paths(NewPaths, ScoredPaths),
    append(OtherPaths, ScoredPaths, AllPaths),
    sort_paths(AllPaths, SortedPaths),
    best_first(SortedPaths, Goal, FinalPath).

% ----------------------------
% Helper Predicates
% ----------------------------

% Evaluate paths based on heuristic of first node in each path
evaluate_paths([], []).
evaluate_paths([[Node|Rest]|T], [[Node|Rest]|ScoredT]) :-
    heuristic(Node, _),
    evaluate_paths(T, ScoredT).

% Sort paths based on heuristic values
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

% Get heuristic of first node in path
path_heuristic([Node|_], H) :-
    heuristic(Node, H).
