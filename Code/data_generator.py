"""_summary_
    """
import json
import lorem
from faker import Faker
from geo_factory import GeoFactory

fake = Faker()


class DataGenerator:

    """_summary_

    Returns:
        _type_: _description_
    """

    @staticmethod
    def city():
        """_summary_

        Returns:
            _type_: _description_
        """
        return {"name": fake.city(),
                "coordinate": GeoFactory.point(),
                "description": lorem.paragraph()}

    @staticmethod
    def road():
        """_summary_

        Returns:
            _type_: _description_
        """
        return {"name": fake.city(),
                "coordinate": GeoFactory.linestring(),
                "description": lorem.paragraph()}

    @staticmethod
    def land():
        """_summary_

        Returns:
            _type_: _description_
        """
        # return {"name": fake.city(),
        #         "coordinate": GeoFactory.polygon(random.randint(4, 1_000)),
        #         "description": lorem.paragraph()}

        return {"name": fake.city(),
                "coordinate": GeoFactory.polygon(),
                "description": lorem.paragraph()}


if __name__ == "__main__":

    print("="*4, " city ", "="*4)
    print(json.dumps(DataGenerator.city(), indent=2))

    print("="*4, " road ", "="*4)
    print(json.dumps(DataGenerator.road(), indent=2))

    print("="*4, " land ", "="*4)
    print(json.dumps(DataGenerator.land(), indent=2))
