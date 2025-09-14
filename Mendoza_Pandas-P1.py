{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "207e7dfc-6f7e-4dec-be0a-4900dc28a72e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd #Using lib panda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b6e5b256-2cd2-4e2d-a600-4c9e03199a12",
   "metadata": {},
   "outputs": [],
   "source": [
    "cars = pd.read_csv('cars.csv') #reading and using the cars.csv files from the same folder."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40fe1fd7-a552-4bfd-9fd7-b1853eb02c5c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "64a662cc-d164-4458-af8e-6dc345494812",
   "metadata": {},
   "outputs": [],
   "source": [
    "first = cars.head(5) #head function or first 5 rows function\n",
    "last = cars.tail(5) #tail function or last 5 rows function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "74b89bc5-8f18-46cc-a2db-7b831ef98e03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
      "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
      "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
      "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
      "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
      "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
      "\n",
      "   carb  \n",
      "0     4  \n",
      "1     4  \n",
      "2     1  \n",
      "3     1  \n",
      "4     2  \n"
     ]
    }
   ],
   "source": [
    "print(first)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "de4524bc-ea13-4b3c-a7b6-e03776fc8b0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
      "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
      "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
      "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
      "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
      "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
      "\n",
      "    carb  \n",
      "27     2  \n",
      "28     4  \n",
      "29     6  \n",
      "30     8  \n",
      "31     2  \n"
     ]
    }
   ],
   "source": [
    "print(last)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "def4531e-7054-4a87-a0ec-f3795d37d087",
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
