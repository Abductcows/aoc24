import importlib
import os
import re
import unittest


##### SPOILERS FOR THE SAME INPUT FILES #####

class MyTestCase(unittest.TestCase):
    def test_d1(self):
        self.assertEqual(1189304, self.solve('d1p1'))
        self.assertEqual(24349736, self.solve('d1p2'))

    def test_d2(self):
        self.assertEqual(585, self.solve('d2p1'))
        self.assertEqual(626, self.solve('d2p2'))

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        files = [f[:-3] for f in os.listdir(current_dir) if f.startswith('d') and f.endswith('.py')]
        for file in files:
            module = importlib.import_module(file)
            self.module_dict[file] = module

    module_dict = {}

    def solve(self, module_name):
        match = re.fullmatch(r'd(\d+)p(\d+)', module_name)
        assert match
        day, _problem = map(int, match.groups())
        return self.module_dict[module_name].run(f'i{day}.txt')


if __name__ == '__main__':
    unittest.main(buffer=False)
