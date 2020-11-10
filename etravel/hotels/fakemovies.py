import random

HotelA = {
  "name": "Hotel A",
  "continent": "asia",
  "location": "Singapore",
  "price": 420
}

HotelB = {
  "name": "Hotel B",
  "continent": "asia",
  "location": "Malaysia",
  "price": 208
}
HotelC = {
  "name": "Hotel C",
  "continent": "asia",
  "location": "India",
  "price": 280
}
HotelD = {
  "name": "Hotel D",
  "continent": "antartica",
  "location": "Antartica Base 2",
  "price": 230
}
HotelE = {
  "name": "Hotel E",
  "continent": "antartica",
  "location": "Antartica USSR Base",
  "price": 260
}
HotelF = {
  "name": "Hotel F",
  "continent": "australia",
  "location": "australia",
  "price": 720
}
HotelG = {
  "name": "Hotel G",
  "continent": "africa",
  "location": "Kenya",
  "price": 620
}
HotelH = {
  "name": "Hotel H",
  "continent": "africa",
  "location": "Egypt",
  "price": 520
}
HotelI = {
  "name": "Hotel I",
  "continent": "southamerica",
  "location": "Argentina",
  "price": 210
}
HotelJ = {
  "name": "Hotel J",
  "continent": "southamerica",
  "location": "Brazil",
  "price": 210
}
HotelK = {
  "name": "Hotel K",
  "continent": "southamerica",
  "location": "Cuba",
  "price": 220
}
HotelL = {
  "name": "Hotel L",
  "continent": "southamerica",
  "location": "Mexico",
  "price": 20
}
HotelM = {
  "name": "Hotel M",
  "continent": "europe",
  "location": "Germany",
  "price": 260
}
HotelN = {
  "name": "Hotel N",
  "continent": "northamerica",
  "location": "USA",
  "price": 110
}
HotelO = {
  "name": "Hotel O",
  "continent": "europe",
  "location": "Luxembourg",
  "price": 210
}
HotelP = {
  "name": "Hotel P",
  "continent": "northamerica",
  "location": "Canada",
  "price": 220
}
HotelQ = {
  "name": "Hotel Q",
  "continent": "europe",
  "location": "Italy",
  "price": 120
}


hotels = [HotelA,HotelB,HotelC,HotelD,HotelE,HotelF,HotelG,HotelH,HotelI,HotelJ,HotelK,HotelL,HotelN,HotelO,HotelP,HotelQ,HotelA,HotelB,HotelC,HotelD,HotelE,HotelF,HotelI,HotelJ,HotelK,HotelL,HotelN,HotelO,HotelP,HotelQ]

random.shuffle(hotels)