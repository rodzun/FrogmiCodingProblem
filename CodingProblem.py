import datetime

class Incident:
    def __init__(self, description, status, dateOpen=None, dateSolved=None):
        self.description = description
        self.status = status
        self.dateOpen = dateOpen or datetime.datetime.now()
        self.dateSolved = dateSolved
    
    def __repr__(self):
        if self.status == 'Open':
            return 'Incident Description: ' + self.description + ', Status: ' + self.status + ', Date Open: ' + self.dateOpen.strftime("%m/%d/%Y, %H:%M:%S") + ', Date Solved: None' 
        else:
            return 'Incident Description: ' + self.description + ', Status: ' + self.status + ', Date Open: ' + self.dateOpen.strftime("%m/%d/%Y, %H:%M:%S") + ', Date Solved: ' + self.dateSolved.strftime("%m/%d/%Y, %H:%M:%S")

class Store:
    def __init__(self):
        self.Incidents = []

    def add_incident(self, incidentObject):
        self.Incidents.append(incidentObject)
    
    def solve_incident(self, incidentIndex):
        self.Incidents[incidentIndex].status = "Solved"
        self.Incidents[incidentIndex].dateSolved = datetime.datetime.now()

    def incident_status(self, initialDate, finalDate):
        open_cases = 0
        closed_cases = 0
        average_solution = 0
        solution_times = []
        maximum_solution = datetime.timedelta()

        for incident in self.Incidents:
            if incident.dateOpen >= initialDate:
                if incident.status == 'Open':
                    open_cases += 1
                    if datetime.datetime.now() - incident.dateOpen > maximum_solution:
                        maximum_solution = datetime.datetime.now() - incident.dateOpen
                if incident.status == 'Solved' and incident.dateSolved <= finalDate:    
                    closed_cases += 1
                    solutionTime = incident.dateSolved - incident.dateOpen
                    solution_times.append(solutionTime)
                    if solutionTime > maximum_solution:
                        maximum_solution = solutionTime

        if len(solution_times) > 0:
            average_solution = sum(solution_times,datetime.timedelta()) / len(solution_times)       
        else: 
            average_solution = 0

        #print(open_cases, closed_cases, average_solution, maximum_solution)
        stats = {'open_cases':open_cases,'closed_cases':closed_cases,'average_solution':str(average_solution),'maximum_solution':str(maximum_solution)}
        return stats

    def __str__(self):
        return 'Number of Incidents: ' + str(len(self.Incidents)) + ', \nIncidents: ' + self.Incidents.__str__()
        
if __name__ == "__main__": # pragma: no cover
    inc1 = Incident("Prueba", "Open")
    inc2 = Incident("Prueba", "Open", datetime.datetime.strptime('2022-01-03 00:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
    inc3 = Incident("Prueba", "Open", datetime.datetime.strptime('2022-01-04 11:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
    inc4 = Incident("Prueba", "Open", datetime.datetime.strptime('2022-01-01 11:35:22.687970', "%Y-%m-%d %H:%M:%S.%f"))
    store1 = Store()
    store1.add_incident(inc1)
    store1.add_incident(inc2)
    store1.add_incident(inc3)
    store1.add_incident(inc4)
    store1.solve_incident(0)
    store1.solve_incident(1)
    store1.solve_incident(2)
    print(store1)
    print(store1.incident_status(datetime.datetime.strptime('2022-01-01', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-11', "%Y-%m-%d")))
    print(store1.incident_status(datetime.datetime.strptime('2022-01-12', "%Y-%m-%d"),datetime.datetime.strptime('2022-01-22', "%Y-%m-%d")))