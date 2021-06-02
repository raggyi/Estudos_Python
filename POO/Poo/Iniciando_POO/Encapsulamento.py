"""
_protected
__private
"""
class Database:
    def __init__(self):
        self.data = {}

    def insert_clients(self,id,name):
        if 'clients' not in self.data:
            self.data['clients'] ={id:name}
        else:
            self.data['clients'].update({id:name})

    def listclients(self):
        for id, name in self.data['clients'].items():
            print(f'{id}: {name}')

    def del_clients(self,id):
        del self.data['clients'][id]

d1 = Database()
d1.insert_clients(1,'Roger')
d1.insert_clients(2,'Lebade')
d1.listclients()