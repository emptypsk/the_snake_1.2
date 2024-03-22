# Змейка

Классическая компьютерная игра «Змейка» является одной из самых известных в мире игр. Простые правила, минималистичный дизайн и драйв — причины популярности этой игры на протяжении многих лет: прототип был придуман в 1976 году, а первая «Змейка», которую мы знаем, — в 1995-м.

## Установка и запуск

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.x).
2. Установите библиотеку Pygame, если она еще не установлена:

   ```bash
   pip install pygame
3. Скачайте исходный код из репозитория или скопируйте его в свой локальный проект.

4. Запустите файл the_snake.py:
    ```bash
    python the_snake.py

##  Правила игры
Змейка состоит из сегментов.
Змейка движется в одном из четырёх направлений — вверх, вниз, влево или вправо. Игрок управляет направлением движения, но змейка не может остановиться или двигаться назад.
Каждый раз, когда змейка съедает яблоко, она увеличивается в длину на один сегмент.
Змейка может проходить сквозь стену и появляться с противоположной стороны поля.
Если змейка столкнётся сама с собой — игра заканчивается.

## Управление
Управление змейкой осуществляется с помощью стрелок на клавиатуре:

#### Стрелка вверх: движение змейки вверх.
#### Стрелка вниз: движение змейки вниз.
#### Стрелка влево: движение змейки влево.
#### Стрелка вправо: движение змейки вправо.
#### Если игрок желает завершить игру, можно нажать клавишу "Esc" или закрыть окно.

## Цель игры

Цель игры - управляя змейкой, съесть как можно больше яблок, чтобы увеличивать ее размер. При этом следует избегать столкновения с собственным телом змейки.

# Snake

The classic computer game "Snake" is one of the most well-known games in the world. Simple rules, minimalist design, and excitement are the reasons for the popularity of this game over many years: the prototype was invented in 1976, and the first "Snake" as we know it appeared in 1995.

## Installation and Launch
1. Make sure you have Python installed (version 3.x is recommended).

2. Install the Pygame library if you haven't already:

   ```bash
   pip install pygame

3. Download the source code from the repository or copy it into your local project.

4. Run the file the_snake.py:

    ```bash
    python the_snake.py

## Game Rules
The snake consists of segments.
The snake moves in one of four directions — up, down, left, or right. The player controls the direction of movement, but the snake cannot stop or move backward.
Every time the snake eats an apple, it grows in length by one segment.
The snake can pass through walls and reappear on the opposite side of the field.
If the snake collides with itself, the game ends.

## Controls
Control of the snake is done using the arrow keys on the keyboard:

#### Up arrow: move the snake up.
#### Down arrow: move the snake down.
#### Left arrow: move the snake left.
#### Right arrow: move the snake right.
#### If the player wishes to end the game, they can press the "Esc" key or close the window.

## Objective
The goal of the game is to control the snake to eat as many apples as possible to increase its size. At the same time, one should avoid colliding with the snake's own body.
