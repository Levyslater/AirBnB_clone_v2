import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand

class TestShowMethod(unittest.TestCase):

    def setUp(self):
        self.command_prompt = HBNBCommand()
        self.user = User()
        self.user.save()
        self.place = Place()
        self.place.save()
        self.state = State()
        self.state.save()
        self.city = City()
        self.city.save()
        self.amenity = Amenity()
        self.amenity.save()
        self.review = Review()
        self.review.save()

    def test_show_user(self):
        self.command_prompt.cmdloop()
        self.command_prompt.do_show("User", self.user.id)
        self.assertEqual(self.command_prompt.do_show("User", self.user.id), str(self.user))

    def test_show_place(self):
        self.command_prompt.cmdloop()
        self.command_prompt.do_show("Place", self.place.id)
        self.assertEqual(self.command_prompt.do_show("Place", self.place.id), str(self.place))

    def test_show_state(self):
        self.command_prompt.cmdloop()
        self.command_prompt.do_show("State", self.state.id)
        self.assertEqual(self.command_prompt.do_show("State", self.state.id), str(self.state))

    def test_show_city(self):
        self.command_prompt.cmdloop()
        self.command_prompt.do_show("City", self.city.id)
        self.assertEqual(self.command_prompt.do_show("City", self.city.id), str(self.city))

    def test_show_amenity(self):
        self.command_prompt.cmdloop()
        self.command_prompt.do_show("Amenity", self.amenity.id)
        self.assertEqual(self.command_prompt.do_show("Amenity", self.amenity.id), str(self.amenity))

if __name__ == "__main__":
    unittest.main()