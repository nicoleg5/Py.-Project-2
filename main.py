import sys

def get_dimension():
#   Desc: Asks the user how many dimensions they want and returns their answer.
#   Inputs: (none)
#   Outputs: The desired number of dimensions (string)

    dims = int(input('How many dimensions do you wish? '))
    return(dims)


def get_trials():
#   Desc: Asks user for number of trials and returns their answer.
#   Inputs: (None)
#   Outputs: Returns the number of trials.

    tri = int(input('How many trials do you wish to execute? '))
    return(tri)


def is_positive_integer(n):
#   Desc: Determines if n can be understood as a positive integer and returns it.

  try:
      int(n)
      if n < 0:
        sys.exit('Cannot be understood as a positive integer')
  except ValueError:
        sys.exit()


def generate_point(d):
#   Desc: Returns a random_check point in c d-dimensional hyperbole of side length 1.

    from random import random
    random_points_1 = [random() for j in range(d)]
    random_points_2 = [random() for j in range(d)]

    return random_points_1, random_points_2


def get_distance(x, y, dim):
#   Desc: Returns the Euclidian distance between the points x and y.
#   Inputs: Two points, x and y.
#   Outputs: The distance between the two points, x and y.

    differences = []
    for j in range(dim):
        dist = abs(x[j] - y[j])
        differences.append(dist)

    return sum ((d ** 2 for d in differences)) ** (1/2)


def use_trials():
#   Desc: Takes the given number of trials and averages it.

  n = get_trials()
  dim = get_dimension()
  is_positive_integer(dim)
  is_positive_integer(n)

  average = 0
  for i in range(n):
      x, y = generate_point(dim)
      d = get_distance(x, y, dim)
      average += d
  average = average/n
  print('The expected value of the distance is x = {:.4f}'.format(average))


use_trials()
