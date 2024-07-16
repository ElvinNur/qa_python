import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "Гордость и предубеждение и зомби",
        "Что делать, если ваш кот хочет вас убить"
    ])
    def test_add_new_book(self, book_name): # Тестируем добавление новой книги. Проверяем, что книга добавляется в словарь books_genre.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ""

    @pytest.mark.parametrize("book_name,genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Гарри Поттер", "Неизвестный Жанр")
    ])
    def test_set_book_genre(self, book_name, genre): # Тестируем установку жанра книги. Проверяем, что жанр устанавливается корректно.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        expected_genre = genre if genre in collector.genre else ""
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("book_name,genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Стивен Кинг", "Ужасы")
    ])
    def test_get_books_with_specific_genre(self, book_name, genre): #  Тестируем получение списка книг с определенным жанром. Проверяем, что книга с указанным жанром присутствует в списке.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book_name in books

    @pytest.mark.parametrize("book_name,genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Стивен Кинг", "Ужасы")
    ])
    def test_get_books_for_children(self, book_name, genre): # Тестируем получение списка книг, подходящих для детей. Проверяем, что книги с возрастным рейтингом отсутствуют в списке.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_for_children()
        if genre in collector.genre_age_rating:
            assert book_name not in books
        else:
            assert book_name in books

    @pytest.mark.parametrize("book_name", [
        "Гарри Поттер",
        "Стивен Кинг"
    ])
    def test_add_book_in_favorites(self, book_name): # Тестируем добавление книги в избранное. Проверяем, что книга добавляется в список favorites.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", [
        "Гарри Поттер",
        "Стивен Кинг"
    ])
    def test_delete_book_from_favorites(self, book_name): # Тестируем удаление книги из избранного. Проверяем, что книга удаляется из списка favorites.
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self): # Тестируем получение списка избранных книг. Проверяем, что список содержит корректные книги.
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

if __name__ == '__main__':
    pytest.main()
