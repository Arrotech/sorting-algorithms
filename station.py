class Subway():
    def __init__(self):
        super().__init__()
        self.data = {}

    def save(self, stationName, startTime):

        new_data = {
            "id": len(self.data)+1,
            "stationName": stationName,
            "startTime": startTime
        }

        self.data[len(self.data)+1] = new_data
        return print(self.data)

        # for journey in self.data[len(self.data)]:
        #     print(journey[id])
            # if self.data['id'] == len(self.data)+1:
            #     return print(journey)

        # return print(self.data)

    # def get_by_id(self, id):
    #     if self.data:
    #         for journey in self.data:
    #             print(journey)
    #             if journey.get('id') == id:
    #                 return print(journey)

    # def checkout(self, id):
    #     journey = Subway().get_by_id(1)
    #     return print(journey)



if __name__ == '__main__':
    stationName = 'London'
    startTime = "8"
    Subway().save(stationName, startTime)
    # Subway().save(stationName, startTime)
    # Subway().save(stationName, startTime)
    # Subway().get_by_id(1)