class Book:
    def __init__(self, title):
        self.title = title

class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        """Returns a list of related contracts."""
        return self._contracts

    def books(self):
        """Returns a list of related books using the Contract class as an intermediary."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract object between the author and the specified book with the specified date and royalties."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        """Returns the total amount of royalties that the author has earned from all of their contracts."""
        return sum(contract.royalties for contract in self._contracts)

class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = None
        self.book = None
        self.date = None
        self.royalties = None

        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)

        Contract._all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that have the same date as the date passed into the method."""
        return [contract for contract in cls._all_contracts if contract.date == date]

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class")
        self.author = author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class")
        self.book = book

    def set_date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self.date = date

    def set_royalties(self, royalties):
        if not isinstance(royalties, (int, float)) or royalties < 0 or royalties > 100:
            raise Exception("royalties must be a number between 0 and 100")
        self.royalties = royalties

