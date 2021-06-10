import unittest
import Examples


class TestFunction(unittest.TestCase):

    def test_json_sum_str(self):
        dumped = Examples.json_seria.dumps(Examples.summing)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), Examples.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), Examples.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("json", "error"))

    def test_json_sum_file(self):
        Examples.json_seria.dump(Examples.summing)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(16, -5), Examples.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), Examples.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("json", "error"))

    def test_pickle_sum_str(self):
        dumped = Examples.pickle_seria.dumps(Examples.summing)
        loaded = Examples.pickle_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), Examples.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), Examples.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("pickle", "error"))

    def test_pickle_sum_file(self):
        Examples.pickle_seria.dump(Examples.summing)
        loaded = Examples.pickle_seria.load()
        self.assertEqual(loaded(16, -5), Examples.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), Examples.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("pickle", "error"))

    def test_toml_sum_str(self):
        dumped = Examples.toml_seria.dumps(Examples.summing)
        loaded = Examples.toml_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), Examples.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), Examples.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("toml", "error"))

    def test_toml_sum_file(self):
        Examples.toml_seria.dump(Examples.summing)
        loaded = Examples.toml_seria.load()
        self.assertEqual(loaded(-124, 11), Examples.summing(-124, 11))
        self.assertEqual(loaded(11.2, 2.6), Examples.summing(11.2, 2.6))
        self.assertNotEqual(loaded(1, 8), Examples.summing(1, 0))
        self.assertRaises(TypeError, lambda: loaded("toml", "error"))

    def test_yaml_sum_str(self):
        dumped = Examples.yaml_seria.dumps(Examples.summing)
        loaded = Examples.yaml_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), Examples.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), Examples.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("yaml", "error"))

    def test_yaml_sum_file(self):
        Examples.yaml_seria.dump(Examples.summing)
        loaded = Examples.yaml_seria.load()
        self.assertEqual(loaded(16, -5), Examples.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), Examples.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), Examples.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("yaml", "error"))


class TestLambda(unittest.TestCase):

    def test_json_triple_str(self):
        dumped = Examples.json_seria.dumps(Examples.triple)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_json_triple_file(self):
        Examples.json_seria.dump(Examples.triple)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_pickle_triple_str(self):
        dumped = Examples.json_seria.dumps(Examples.triple)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_pickle_triple_file(self):
        Examples.json_seria.dump(Examples.triple)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("ha"), Examples.triple("ha"))

    def test_toml_triple_str(self):
        dumped = Examples.json_seria.dumps(Examples.triple)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded(17.2), Examples.triple(17.2))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("str"), Examples.triple("str"))

    def test_toml_triple_file(self):
        Examples.json_seria.dump(Examples.triple)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("val"), Examples.triple("val"))

    def test_yaml_triple_str(self):
        dumped = Examples.json_seria.dumps(Examples.triple)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("c"), Examples.triple("c"))

    def test_yaml_triple_file(self):
        Examples.json_seria.dump(Examples.triple)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(2), Examples.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), Examples.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), Examples.triple(1))
        self.assertEqual(loaded("1"), Examples.triple("1"))


class TestObject(unittest.TestCase):

    def test_json_circle_str(self):
        dumped = Examples.json_seria.dumps(Examples.circle)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_json_circle_file(self):
        Examples.json_seria.dump(Examples.circle)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_pickle_circle_str(self):
        dumped = Examples.pickle_seria.dumps(Examples.circle)
        loaded = Examples.pickle_seria.loads(dumped)
        self.assertEqual(loaded.square(), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_pickle_circle_file(self):
        Examples.pickle_seria.dump(Examples.circle)
        loaded = Examples.pickle_seria.load()
        self.assertEqual(loaded.square(), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_toml_circle_str(self):
        dumped = Examples.toml_seria.dumps(Examples.circle)
        loaded = Examples.toml_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_toml_circle_file(self):
        Examples.toml_seria.dump(Examples.circle)
        loaded = Examples.toml_seria.load()
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_yaml_circle_str(self):
        dumped = Examples.yaml_seria.dumps(Examples.circle)
        loaded = Examples.yaml_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)

    def test_yaml_circle_file(self):
        Examples.yaml_seria.dump(Examples.circle)
        loaded = Examples.yaml_seria.load()
        self.assertEqual(loaded.square(loaded), Examples.circle.square())
        self.assertEqual(loaded.radius, Examples.circle.radius)
        self.assertEqual(loaded.name, Examples.circle.name)
        self.assertEqual(loaded.samples, Examples.circle.samples)


class TestClass(unittest.TestCase):

    def test_json_figure_str(self):
        dumped = Examples.json_seria.dumps(Examples.Figure)
        loaded = Examples.json_seria.loads(dumped)
        parsed_obj = loaded("circle")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_json_figure_file(self):
        Examples.json_seria.dump(Examples.Figure)
        loaded = Examples.json_seria.load()
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_pickle_figure_str(self):
        dumped = Examples.pickle_seria.dumps(Examples.Figure)
        loaded = Examples.pickle_seria.loads(dumped)
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_pickle_figure_file(self):
        Examples.pickle_seria.dump(Examples.Figure)
        loaded = Examples.pickle_seria.load()
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_toml_figure_str(self):
        dumped = Examples.toml_seria.dumps(Examples.Figure)
        loaded = Examples.toml_seria.loads(dumped)
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_toml_figure_file(self):
        Examples.toml_seria.dump(Examples.Figure)
        loaded = Examples.toml_seria.load()
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_yaml_figure_str(self):
        dumped = Examples.yaml_seria.dumps(Examples.Figure)
        loaded = Examples.yaml_seria.loads(dumped)
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_yaml_figure_file(self):
        Examples.yaml_seria.dump(Examples.Figure)
        loaded = Examples.yaml_seria.load()
        parsed_obj = loaded("ellipse")
        fig_obj = Examples.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())


class TestHardFunction(unittest.TestCase):

    def test_json_calc_str(self):
        dumped = Examples.json_seria.dumps(Examples.calculate)
        loaded = Examples.json_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_json_calc_file(self):
        Examples.json_seria.dump(Examples.calculate)
        loaded = Examples.json_seria.load()
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_pickle_calc_str(self):
        dumped = Examples.pickle_seria.dumps(Examples.calculate)
        loaded = Examples.pickle_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_pickle_calc_file(self):
        Examples.pickle_seria.dump(Examples.calculate)
        loaded = Examples.pickle_seria.load()
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_toml_calc_str(self):
        dumped = Examples.toml_seria.dumps(Examples.calculate)
        loaded = Examples.toml_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_toml_calc_file(self):
        Examples.toml_seria.dump(Examples.calculate)
        loaded = Examples.toml_seria.load()
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_yaml_calc_str(self):
        dumped = Examples.yaml_seria.dumps(Examples.calculate)
        loaded = Examples.yaml_seria.loads(dumped)
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))

    def test_yaml_calc_file(self):
        Examples.yaml_seria.dump(Examples.calculate)
        loaded = Examples.yaml_seria.load()
        self.assertEqual(loaded(2), Examples.calculate(2))
        self.assertEqual(loaded(-4), Examples.calculate(-4))
        self.assertRaises(TypeError, lambda: loaded("2"))
