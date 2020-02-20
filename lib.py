class Lib:
    def __init__(self, self_id, book_ids, signup, ship_per_day):
        self.id = self_id
        self.book_ids = book_ids
        self.signup = signup
        self.ship_per_day = ship_per_day

    def __str__(self):
        print('\{id :{}\nsignup : {}\n spd : {}'.format(self.id, self.signup, self.ship_per_day))
        print(' books_num : {}'.format(len(self.book_ids)))
        print(' book_ids : ' + ' '.join(map(str, lib.book_ids)))

