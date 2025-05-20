# Country Guesser

A game made with Python, using pandas and tkinter, where you have to guess the capital or the continent of a country.

The game starts with a welcome screen where you can choose the difficulty level: Easy, Medium, or Hard.  
- On **Easy**, you guess the **continent** of the country.  
- On **Medium**, you choose the **capital city** from multiple options.  
- On **Hard**, you must **type the capital city** manually.

The game tracks your high score and saves it in a CSV file.

## Installation

```bash
pip install -r requirements.txt
```

## Features
- Three difficulty levels with increasing challenge;
- Interactive GUI with tkinter;
- Persistent high score saved locally;
- Uses pandas for data handling;

## Project Structure
- country_list.csv: contains the list of countries with their capitals and continents  
- game.py: main game script
- main.py: starts game
- scores.csv: score saving file
- welcome.py: starting window with difficulty choice  

## How to run
``` bash
python main.py
```
