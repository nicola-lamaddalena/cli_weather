# CLI weather app

Simple weather app that fetches weather information.

## Table of contents

* [General info](#general-info)
* [Tecnologies](#tecnologies)
* [Setup](#setup)
* [Features](#features)

## General info

This app is an attempt to work with external APIs and with the library [click](https://click.palletsprojects.com/en/8.1.x/).

The external API used to fetch the data is [Open-Meteo](https://open-meteo.com/).

## Tecnologies

* Python 3.11.0
* requests 2.31.0
* pandas 2.0.3
* geopy 2.3.0
* click 8.1.3

## Setup

To run this project, first install the dependencies with:

```powershell
cd folder_path
pip install -r requirements.txt
```

then start it from the command line:

```powershell
cd app\src
python main.py
```

To get information about the arguments:

```poweshell
python main.py --help
```

## Usage

* If you run the project without the arguments, you will be prompted for the name of the city.

```powershell
python main.py
Insert your desired location: 
```

* If you omit the temperature unit, Celsius will be used as default.

* If you want to pass one or both arguments at command line, you need to specify their names.

```powershell
python main.py --city=name_of_the_city --unit=F
```

## Features

* Get the temperature of the current day
* Get the forecast for the next 7 days with minimum and maximum temperature and mean probability of precipitation
* Choose the temperature unit (Celsius or Fahrenheit)
