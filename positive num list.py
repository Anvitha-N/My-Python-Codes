{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the start of range : -5\n",
      "Enter the end of range : 10\n",
      "0 1 2 3 4 5 6 7 8 9 10 "
     ]
    }
   ],
   "source": [
    "# python program to print all positive numbers in a range\n",
    "\n",
    "start = int(input(\"Enter the start of range : \"))\n",
    "end = int(input(\"Enter the end of range : \"))\n",
    "\n",
    "# iterating each number in a list \n",
    "for num in range( start , end + 1) :\n",
    "    \n",
    "    #checking condition\n",
    "    \n",
    "    if num >= 0:\n",
    "        print(num, end = \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 12 39 67 99 28 "
     ]
    }
   ],
   "source": [
    "# python program to print positive numbers in a given List\n",
    "\n",
    "# list of numbers\n",
    "list1 = [5, 12, -55, 39, -10, 67, 99, -78, 28]\n",
    "\n",
    "# iterating each number in list \n",
    "for num in list1:\n",
    "     \n",
    "        # checking condition \n",
    "        if num >= 0 :\n",
    "            print(num, end = \" \")\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
