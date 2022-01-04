import unittest
import datetime
from CodingProblem import Incident,Store

class IncidentTest(unittest.TestCase):
    def setUp(self):
        self.i = Incident("Testing description","Open",datetime.datetime.strptime('2022-01-04 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))

    def test_details(self):
        description = self.i.description
        self.assertEqual(description,"Testing description")

        status = self.i.status
        self.assertEqual(status,"Open")

        dateOpen = self.i.dateOpen
        self.assertEqual(dateOpen,datetime.datetime.strptime('2022-01-04 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
        self.assertIsInstance(dateOpen, datetime.datetime)

    def test_repr_open(self):
        self.assertEqual(self.i.__repr__(),'Incident Description: Testing description, Status: Open, Date Open: 01/04/2022, 00:35:22, Date Solved: None')    

    def test_repr_solved(self):
        self.i = Incident("Testing description","Solved",datetime.datetime.strptime('2022-01-04 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"),datetime.datetime.strptime('2022-01-04 01:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
        self.assertEqual(self.i.__repr__(),'Incident Description: Testing description, Status: Solved, Date Open: 01/04/2022, 00:35:22, Date Solved: 01/04/2022, 01:35:22')    

class StoreTest(unittest.TestCase):
    def setUp(self):
        self.s = Store()
        self.i = Incident("Testing description","Open",datetime.datetime.strptime('2022-01-04 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))

    def test_add_incident(self):
        self.s.add_incident(self.i)
        self.assertEqual(1,len(self.s.Incidents))
        self.assertIsInstance(self.i,Incident)

    def test_solve_incident(self):
        self.s.add_incident(self.i)
        self.s.solve_incident(0)
        self.assertEqual(self.s.Incidents[0].status,"Solved")
    
    def test_open_cases(self):
        self.s.add_incident(self.i)
        stat = self.s.incident_status(datetime.datetime.strptime('2022-01-04', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d"))
        self.assertEqual(1,stat['open_cases'])

    def test_solved_cases(self):
        self.s.add_incident(self.i)
        self.s.solve_incident(0)
        stat = self.s.incident_status(datetime.datetime.strptime('2022-01-04', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d"))
        self.assertEqual(1,stat['closed_cases'])

    def test_average_solution(self):
        self.i = Incident("Testing description","Solved",datetime.datetime.strptime('2022-01-03 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"),datetime.datetime.strptime('2022-01-03 01:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
        self.i2 = Incident("Testing description 2","Solved",datetime.datetime.strptime('2022-01-04 01:05:22.687970', "%Y-%m-%d %H:%M:%S.%f"),datetime.datetime.strptime('2022-01-04 01:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
        self.s.add_incident(self.i)
        self.s.add_incident(self.i2)
        stat = self.s.incident_status(datetime.datetime.strptime('2022-01-03', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d"))
        self.assertEqual('0:45:00',stat['average_solution'])    

    def test_average_solution_zero_incidents(self):
        stat = self.s.incident_status(datetime.datetime.strptime('2022-01-04', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d"))
        self.assertEqual('0',stat['average_solution'])

    def test_maximum_solution(self):
        self.i = Incident("Testing description","Solved",datetime.datetime.strptime('2022-01-04 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"),datetime.datetime.strptime('2022-01-04 01:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
        self.s.add_incident(self.i)
        stat = self.s.incident_status(datetime.datetime.strptime('2022-01-04', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d"))
        self.assertEqual('1:00:00',stat['average_solution'])

    def test_str(self):
        self.assertEqual(self.s.__str__(),'Number of Incidents: 0, \nIncidents: []')    

if __name__ == "__main__":
    unittest.main(verbosity=2)