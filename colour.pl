% Facts: fruit and color
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(grapes, black).
fruit_color(orange, orange).

% Rule to find fruit and its color
color_of(Fruit, Color) :-
    fruit_color(Fruit, Color).
