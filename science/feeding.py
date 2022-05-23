{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'analise': {'23/05/2022 à 20/05/2022': {'despesas': 11171.611666666664,\n",
       "   'faturamento': 11862.283233329566,\n",
       "   'saldo': 690.6715666629025},\n",
       "  '30/05/2022 à 20/05/2022': {'despesas': 21970.376666666663,\n",
       "   'faturamento': 11862.283233329566,\n",
       "   'saldo': -10108.093433337097},\n",
       "  '06/06/2022 à 20/05/2022': {'despesas': 5879.9366666666665,\n",
       "   'faturamento': 11862.283233329566,\n",
       "   'saldo': 5982.3465666629},\n",
       "  '20/06/2022 à 20/05/2022': {'despesas': 730.0,\n",
       "   'faturamento': 11862.283233329566,\n",
       "   'saldo': 11132.283233329566}},\n",
       " 'negadas': {'cara preta': {'valor parcela': 158.4,\n",
       "   'preco': 316.8,\n",
       "   'data': '05/06/2022'},\n",
       "  'gatão': {'valor parcela': 157.425, 'preco': 314.85, 'data': '05/06/2022'},\n",
       "  'recheados brasil': {'valor parcela': 906.36,\n",
       "   'preco': 906.36,\n",
       "   'data': '05/06/2022'},\n",
       "  'dona beth': {'valor parcela': 191.425,\n",
       "   'preco': 382.85,\n",
       "   'data': '05/06/2022'},\n",
       "  'porcão': {'valor parcela': 959.0666666666666,\n",
       "   'preco': 2877.2,\n",
       "   'data': '05/06/2022'}}}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests.get('http://127.0.0.1:5000/relatorio').json()"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "ad2bdc8ecc057115af97d19610ffacc2b4e99fae6737bb82f5d7fb13d2f2c186"
  },
  "kernelspec": {
   "display_name": "Python 3.8.8 ('base')",
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
   "version": "3.8.8"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
