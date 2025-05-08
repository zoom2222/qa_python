import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_set_book_genre(self, collector):
        collector.add_new_book("Сталкер")
        collector.set_book_genre("Сталкер", "Фантастика")
        assert collector.get_book_genre("Сталкер") == "Фантастика"


    def test_get_book_genre_non_existent(self, collector): # полностью изменил этот тест
        assert collector.get_book_genre("Несуществующая книга") is None


    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Ужасы")
        collector.set_book_genre("Книга 2", "Ужасы")
        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert len(horror_books) == 2
        assert "Книга 1" in horror_books
        assert "Книга 2" in horror_books


    def test_get_books_for_children(self, collector):
        collector.add_new_book("Мультфильм")
        collector.add_new_book("Ужастик")
        collector.set_book_genre("Мультфильм", "Мультфильмы")
        collector.set_book_genre("Ужастик", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Мультфильм" in children_books
        assert "Ужастик" not in children_books


    def test_book_add_in_favorites(self, collector):
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Нелюбимая книга")
        collector.add_book_in_favorites("Нелюбимая книга")
        collector.delete_book_from_favorites("Нелюбимая книга")
        assert "Нелюбимая книга" not in collector.get_list_of_favorites_books()


    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Избранная книга 1")
        collector.add_new_book("Избранная книга 2")
        collector.add_book_in_favorites("Избранная книга 1")
        collector.add_book_in_favorites("Избранная книга 2")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert "Избранная книга 1" in favorites
        assert "Избранная книга 2" in favorites


@pytest.mark.parametrize(
    "genre, is_for_children",
    [
        ("Мультфильмы", True),
        ("Ужасы", False),
        ("Комедии", True)
    ]
)
def test_get_books_for_children_param(collector, genre, is_for_children):
    book = "Kids Book"
    collector.add_new_book(book)
    collector.set_book_genre(book, genre)
    result = book in collector.get_books_for_children()
    assert result == is_for_children


@pytest.mark.parametrize(
    "input_genre, expected",
    [
        ("Фантастика", "Фантастика"),
        ("", ""),
        (None, None)
    ]
)
def test_get_book_genre_param(collector,input_genre, expected):
    book = "Test Book"
    input_genre is not None and collector.add_new_book(book)
    input_genre is not None and collector.set_book_genre(book, input_genre)
    assert collector.get_book_genre(book) == expected

@pytest.mark.parametrize(
    "action, expected_count",
    [
        ("add", 1),
        ("remove", 0)
    ]
)
def test_add_and_remove_books_from_favorites(collector,action, expected_count):
    book = "Favorite Book"
    collector.add_new_book(book)
    action == "add" and collector.add_book_in_favorites(book)
    action == "remove" and collector.delete_book_from_favorites(book)
    assert len(collector.get_list_of_favorites_books()) == expected_count