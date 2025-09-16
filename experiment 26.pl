% Knowledge Base: fruit and its color
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, green).
fruit(orange, orange).
fruit(mango, yellow).
fruit(blueberry, blue).
fruit(cherry, red).

% Rule to display fruit and color
fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).
