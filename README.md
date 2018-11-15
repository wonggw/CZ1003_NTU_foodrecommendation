# CZ1003 NTU F&B recommendation

## Installing dependencies

```python
pip install -r requirements.txt
```

## To exceute:

```python
python main.py
```

*program need some time to calculate the shortest route. DO* **NOT** *spam on the map.*

## Description:

* **main.py** is used to link all the functions together.

* **display.py** is to display the image onto pygame and record the position of the is mouse clicked. Will update the image based on where the mouse is clicked.

* **Algo.py** contains statistical tools for computing the score for the 3 variable.
[X] Distance
[X] Type of cuisine
[X] Price range

* **Astar.py** contains astar search algorithm.
[x] To create the graph
[x] To compute the shortest distance and the cost.

### To collect the coordinate for obstacle and bus route:

```bash
cd ./data_collection
```
