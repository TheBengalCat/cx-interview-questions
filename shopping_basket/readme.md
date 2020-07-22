## Documentation

## Documentation

## Introduction
My attempt at implementing the shopping basket task can be found here. 

## Running the code
The code can be run/tested using pytest - "pipenv run pytest"

## Catalogue and Offers
The format for the Catalogue is a simple dictionary:
{
    "peach": 1.53,
    "tomato": 0.60,
    "cornflakes": 2.35
    }

The format for Offers is a nested dictionary:
Buy X Get Y contains a string key with a value that is a list of integers representing x and y
Percentage Discount contains a string key with a float value that is the decimal equivalent of a percentage discount
{
    "BuyXGetY": {
        "peach": [2, 1]
        }, 
    "PercentageDiscount": {
        "tomato": 0.25
        }
    }

## Assumptions:
- Any single item will only have 1 offer at any given time
- To be eligible for buy x get y free, you must have a quantity > x + y