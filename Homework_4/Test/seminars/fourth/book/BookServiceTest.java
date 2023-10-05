package seminars.fourth.book;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.anyInt;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class BookServiceTest {

    /**
     * Задание 2. У вас есть класс BookService, который использует интерфейс BookRepository для получения
     * информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
     * Mockito для создания мок-объекта BookRepository.
     */

    @Test
    public void testFindBookById() {
        // Создаём мок-объект для класса BookRepository
        BookRepository mockBookRepository = mock(BookRepository.class);

        // Определение поведения мок-объектов
        Book testBook = new Book("1", "Book1", "Author1");

        when(mockBookRepository.findById("1")).thenReturn(testBook);

        // Создаем объект класса, который мы хотим протестировать, передавая мок в качестве зависимости
        BookService bookService = new BookService(mockBookRepository);

        // Вызываем метод, который хотим протестировать
        Book resultBook = bookService.findBookById("1");

        // Проверяем результат
        assertEquals(testBook, resultBook);
    }

    @Test
    public void testFindAllBooks() {
        // Создаём мок-объект для класса BookRepository
        BookRepository mockBookRepository = mock(BookRepository.class);

        // Определение поведения мок-объектов
        List<Book> testBooks = new ArrayList<>();
        testBooks.add(new Book("1", "Book1", "Author1"));
        testBooks.add(new Book("2", "Book2", "Author2"));

        when(mockBookRepository.findAll()).thenReturn(testBooks);

        // Создаем объект класса, который мы хотим протестировать, передавая мок в качестве зависимости
        BookService bookService = new BookService(mockBookRepository);

        // Вызываем метод, который хотим протестировать
        List<Book> resultList = bookService.findAllBooks();

        // Проверяем результат
        assertEquals(testBooks, resultList);
    }
}