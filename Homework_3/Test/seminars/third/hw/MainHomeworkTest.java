package seminars.third.hw;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import seminars.third.coverage.SomeService;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class MainHomeworkTest {

    private MainHW mainHW;
    @BeforeEach
    void setUp() {mainHW = new MainHW();}

    @Test
    void testEvenNumber() {
        assertTrue(mainHW.evenOddNumber(2));
    }

    @Test
    void testOddNumber() {
        assertFalse(mainHW.evenOddNumber(3));
    }

    @Test
    void testNumberInInterval() {
        assertTrue(mainHW.numberInInterval(35));
    }

    @ParameterizedTest
    @ValueSource(ints = {15,105})
    void testNumberNotInInterval(int i) {
        assertFalse(mainHW.numberInInterval(i));
    }
}