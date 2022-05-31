"""_summary_
    """

# * https://github.com/scook12/geofactory
# * https://github.com/jazzband/geojson

import json
import random
from geojson import Point, utils
from faker import Faker

fake = Faker()


class GeoFactory:
    """Faker Provider object for generating valid GeoJSON data"""
    @staticmethod
    def lnglat(num=2):
        """Returns specific number of random lon/lat pairs"""
        return [(float(fake.longitude()),
                float(fake.latitude()))
                for _ in range(num)]

    @staticmethod
    def point():
        """Returns single geojson point object with random coordinates"""
        return Point(GeoFactory.lnglat(1)[0])

    @staticmethod
    def linestring():
        """Returns a geojson linestring object with
        a random number of nodes"""

        return utils.generate_random("LineString",
                                     numberVertices=random.randint(3, 300))

    @ staticmethod
    def polygon():
        """Returns a randomly arranged polygon with a
        specified number of nodes"""

        return utils.generate_random("Polygon",
                                     numberVertices=random.randint(4, 500))


if __name__ == "__main__":

    # print(GeoFactory.point())
    # print(json.dumps(GeoFactory.point(), indent=2))
    # print(GeoFactory.linestring())
    # print(json.dumps(GeoFactory.linestring(), indent=2))
    # print(GeoFactory.polygon())
    print(json.dumps(GeoFactory.polygon(), indent=2))
