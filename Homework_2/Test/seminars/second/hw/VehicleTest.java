package seminars.second.hw;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import seminars.second.simple_shopping_cart.Cart;
import seminars.second.simple_shopping_cart.Shop;

import static com.sun.org.apache.bcel.internal.Repository.instanceOf;
import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

import static org.junit.jupiter.api.Assertions.*;

class VehicleTest {

    private Car car;
    private Motorcycle motorcycle;

    @BeforeEach
    void setup() {
        car = new Car("BMW", "318i", 2023);
        motorcycle = new Motorcycle("Suzuki", "GSX-8S", 2022);
    }

    // Проверить, что экземпляр объекта Car
    // также является экземпляром транспортного средства (используя оператор instanceof).
    @Test
    void testInstanceOf() {
        assertTrue(car instanceof Vehicle);
    }

    // Проверить, что объект Car создается с 4-мя колесами.
    @Test
    void testNumberWheelsCar() {
        assertThat(car.getNumWheels()).isEqualTo(4);
    }

    // Проверить, что объект Motorcycle создается с 2-мя колесами.
    @Test
    void testNumberWheelsMotorcycle() {
        assertThat(motorcycle.getNumWheels()).isEqualTo(2);
    }

    // Проверить, что объект Car развивает скорость 60
    // в режиме тестового вождения (используя метод testDrive()).
    @Test
    void testTestDriveSpeedCar() {
        car.testDrive();
        assertThat(car.getSpeed()).isEqualTo(60);
    }

    // Проверить, что объект Motorcycle развивает скорость 75
    // в режиме тестового вождения (используя метод testDrive()).
    @Test
    void testTestDriveSpeedMotorcycle() {
        motorcycle.testDrive();
        assertThat(motorcycle.getSpeed()).isEqualTo(75);
    }

    //Проверить, что в режиме парковки (сначала testDrive, потом park,
    // т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    @Test
    void testParkCar() {
        car.testDrive();
        car.park();
        assertThat(car.getSpeed()).isEqualTo(0);
    }

    // Проверить, что в режиме парковки (сначала testDrive, потом park,
    // т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
    @Test
    void testParkMotorcycle() {
        motorcycle.testDrive();
        motorcycle.park();
        assertThat(motorcycle.getSpeed()).isEqualTo(0);
    }
}