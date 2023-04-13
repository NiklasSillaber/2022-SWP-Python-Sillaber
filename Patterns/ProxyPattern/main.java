package Patterns.ProxyPattern;

public class main {

    public static void main(String[] args) {

        ProxyDrucker drucker = new ProxyDrucker();
        drucker.drucken("Hallo");

        drucker.welchsleDrucker(new ColorDrucker());

        drucker.drucken("Seas");

    }

}
