package seminars.third.tdd;

public class User {

    String name;
    String password;

    boolean isAuthenticate = false;

    public User(String name, String password) {
        this.name = name;
        this.password = password;

    }

    //3.6.
    public boolean authenticate(String name, String password) {
        if (name.equals(this.name)) {
            if (password.equals(this.password)) {
                isAuthenticate = true;
                return true;
            } else {
                isAuthenticate = false;
                return false;
            }
        } else {
            isAuthenticate = false;
            return false;
        }
    }
}