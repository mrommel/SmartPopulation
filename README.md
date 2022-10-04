# SmartPopulation

![](https://github.com/mrommel/SmartPopulation/workflows/Pylint/badge.svg)
![](https://github.com/mrommel/SmartPopulation/workflows/Pytest/badge.svg)

Python implementation of https://www.ined.fr/_modules/SimulateurPopulation/?lang=en (which is javascript).

This can manipulate a population distribution chart of a given setup (aka country).
This also plots this chart using plotly.

### execute application

```
make run
```

### execute pytests

```
make tests
```

### execute pylint

```
make pylint
```

## Links
* https://www.ined.fr/_modules/SimulateurPopulation/?lang=en
* https://service.destatis.de/bevoelkerungspyramide/#! from 2019 for germany
* https://democracygame.fandom.com/wiki/Democracy_4
* https://steamcommunity.com/sharedfiles/filedetails/?id=2242836711
* https://github.com/bakster55/W3JsonToExcel
* https://jsoncrack.com/
* https://github.com/ColorlibHQ/AdminLTE
* https://fontawesome.com/icons
* https://colorhunt.co/palette/25316d5f6f9497d2ecfef5ac

## Scratch pad


### Life span input

Health,0+(0.65*x),4	
Environment,-0.2+(0.4*x),6	
Technology,0.0+(0.15*x),8	
ViolentCrimeRate,0.0-(0.2*x)

### Life span effects

Retired_freq,0.0+(0.08*x)	
FoodPrice,0.0+(0.03*x)