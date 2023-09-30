package seminars.third.tdd;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import seminars.third.coverage.SomeService;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class UserTest {

    private User user;

    @BeforeEach
    void setUp() {user = new User("nameTest", "passwordTest");}

    @Test
    void goodAuthenticateTest() {
        assertTrue(user.authenticate("nameTest", "passwordTest"));
    }

    @Test
    void badNameAuthenticateTest() {
        assertFalse(user.authenticate("badNameTest", "passwordTest"));
    }

    @Test
    void badPasswordAuthenticateTest() {
        assertFalse(user.authenticate("nameTest", "badPasswordTest"));
    }

    @Test
    void goodAddUserInUserRepository() {
        UserRepository userRepositoryTest = new UserRepository();
        User userTest = new User("nameTest", "passwordTest");
        userTest.authenticate("nameTest", "passwordTest");
        userRepositoryTest.addUser(userTest);
        assertTrue(userRepositoryTest.findByName("nameTest"));
    }

    @Test
    void badAddUserInUserRepository() {
        UserRepository userRepositoryTest = new UserRepository();
        User userTest = new User("nameTest", "passwordTest");
        // пользователь не проходит аутентификацию
        userTest.authenticate("nameTest", "badPasswordTest");
        userRepositoryTest.addUser(userTest);
        assertFalse(userRepositoryTest.findByName("nameTest"));
    }
}