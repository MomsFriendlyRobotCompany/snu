import numpy as np
from squaternion import Quaternion

class Vector:
    __data = None

    def __init__(self, x=0,y=0,z=0):
        self.__data = [x,y,z]

    # def __index__(self, i):
    #     return self.__data[i]

    @property
    def x(self):
        return self.__data[0]
    @x.setter
    def x(self, x):
        self.__data[0] = x

    @property
    def y(self):
        return self.__data[1]
    @y.setter
    def y(self, y):
        self.__data[1] = y

    @property
    def z(self):
        return self.__data[2]
    @z.setter
    def z(self, z):
        self.__data[2] = z

    def __str__(self):
        v = self.__data
        return 'x: {:.2f} y: {:.2f} z: {:.2f}'.format(v[0], v[1], v[2])

    def __len__(self):
        """Enables the length function to work: len(v) => 3"""
        return 3

    def __iter__(self):
        """Enables iterating: for i in v: print(i)"""
        for i in self.__data:
            yield i

    def __getitem__(self, i):
        """Enables indexing: v[0] => v.x"""
        return self.__data[i]

    def __eq__(self, vv):
        v = self.__data
        if v[0] == vv[0] and v[1] == vv[1] and v[2] == vv[2]:
            return True
        return False
        # return np.all(self.__data,vv.__data)

    def __mul__(self, s):
        # dot product?
        v = self.__data
        if isinstance(s, (float, int)):
            return Vector(s*v[0],s*v[1],s*v[2])
        elif isinstance(s, Vector):
            return Vector(s[0]*v[0],s[1]*v[1],s[2]*v[2])
        return NotImplementedError(f"Invalide type for s*Vector: {type(s)}")

    def __rmul__(self, s):
        """Would handle things like: s*v"""
        v = self.__data
        if isinstance(s, (float, int)):
            return Vector(s*v[0],s*v[1],s*v[2])
        return NotImplementedError(f"Invalide type for s*Vector: {type(s)}")

    def __add__(self, vv):
        """Would handle things like: v+vv"""
        v = self.__data
        return Vector(v[0]+vv[0],v[1]+vv[1],v[2]+vv[2])

    def __sub__(self, vv):
        """Would handle things like: v-vv"""
        v = self.__data
        return Vector(v[0]-vv[0],v[1]-vv[1],v[2]-vv[2])

    def to_tuple(self):
        v = self.__data
        return (v[0],v[1],v[2],)

    def cross(self, a):
        raise NotImplementedError()

    def normalize(self):
        raise NotImplementedError()

    def magnitude(self):
        raise NotImplementedError()


class Foot:
    position = None
    orientation = 0 # yaw only
    cycle = 0

    def __init__(self, x=0, y=0, z=0, theta=0, cycle=0):
        self.position = Vector(x,y,z)
        self.orientation = theta
        self.cycle = cycle

class Twist:
    linear = Vector()
    angular = Vector()

    def __str__(self):
        return f"linear {self.linear} angular {self.angular}"

class Wrench:
    force = Vector()
    torque = Vector()

class Pose:
    position = Vector()
    orientation = Quaternion()

class Pose2D:
    x = 0
    y = 0
    theta = 0
