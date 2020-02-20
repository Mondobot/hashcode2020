class Lib:
    def __init__(self, self_id, book_ids, signup, ship_per_day):
        self.id = self_id
        self.book_ids = book_ids
        self.signup = signup
        self.ship_per_day = ship_per_day

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = '\nid :{}\n\tsignup : {}\n\tspd : {}\n'.format(self.id, self.signup, self.ship_per_day)
        string += '\tbooks_num : {}'.format(len(self.book_ids))
        string += '\tbook_ids : ' + ' '.join(map(str, self.book_ids))

        return string
