{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "b7fb38e0-285d-4bfc-b7f0-ad19a2785339",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd #Using library panda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "90a82100-0412-4e91-b108-198e1dca7456",
   "metadata": {},
   "outputs": [],
   "source": [
    "cars = pd.read_csv('cars.csv') #Reading file cars.csv and getting data from there"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cef868ab-85fa-4c6b-909a-31d0856c5b78",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "87d6ca4e-f436-45af-af0b-664b2e5a4e6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#THIS IS FOR PROBLEM 2 PART A: FIRST 5 ROWS WITH ODD NUMBERED COLUMNS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "596a98e8-1513-43e9-9815-ea356472aa01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "odd = cars.iloc[:5, ::2] #using the iloc function, we include 0-4, and the use for the increments of 2. LOC DOES NOT WORK HERE.\n",
    "print(odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08358abb-aab4-4c79-a92c-aad8da115e4c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "68755884-292f-4885-a2f0-c91913a7b9d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#THIS IS FOR PROBLEM 2 PART B: ROW THAT CONTAINS MODEL OF MAZDA RX4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d216566c-0e2b-41f3-abb7-1bbc87a02fc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
      "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "mazda = cars.loc[cars['Model'] == 'Mazda RX4'] #using of loc function just like in class.\n",
    "print(mazda)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7149277c-7086-4d4a-b4a2-13bdfd609ade",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "45dea778-ac4a-464f-b1d5-0e955270080d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#THIS IS FOR PROBLEM 2 PART C: NUMBER OF CYLINDERS OF CAMARO Z28"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5a1f46a3-13c2-4a38-9591-a09d7c697626",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is how many clinders Camaro Z28 have:  8\n"
     ]
    }
   ],
   "source": [
    "camaro = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0] #same as used in class, but used values[0] here to not include multiple rows.\n",
    "print(\"This is how many clinders Camaro Z28 have: \", camaro)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a11a0ce-3738-4133-963f-7cde5e88b007",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "021c810e-8bbc-40cf-a087-664dbe22e00b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#THIS IS FOR PROBLEM 2 PART D: FOR MAZDA, FORD HONDA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a1a7a52a-1396-4da5-a127-a660127bb459",
   "metadata": {},
   "outputs": [],
   "source": [
    "models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "b83d615c-bebd-4fe1-9f1b-6bd37fb805be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "group = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']] #Since the loc function only considers column and row selection, used group (models) instead.\n",
    "print(group)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da0e7a29-df73-4f64-baa4-9243ca4a0843",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
