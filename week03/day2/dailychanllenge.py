class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []  # Default to empty list if None
        self.pageSize = int(pageSize)
        self.totalPages = (len(self.items) + self.pageSize - 1) // self.pageSize
        self.currentPage = 1  # Pages start at 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        try:
            page = int(pageNum)
        except ValueError:
            page = 1
        if page < 1:
            self.currentPage = 1
        elif page > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = page
        return self


# ✅ This runs your code and shows output
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.getVisibleItems())              # ['a', 'b', 'c', 'd']
    print(p.nextPage().getVisibleItems())   # ['e', 'f', 'g', 'h']
    print(p.lastPage().getVisibleItems())   # ['y', 'z']
    print(p.goToPage(2).getVisibleItems())  # ['e', 'f', 'g', 'h']
    print(p.goToPage(100).getVisibleItems())# ['y', 'z']
