package Patterns.ProxyPattern;

public class ProxyDrucker implements IDrucker {

    private IDrucker drucker;

    public ProxyDrucker() {
        this.drucker = new WSDrucker();
    }

    @Override
    public void drucken(String nachricht) {
        this.drucker.drucken(nachricht);
    }

    public void welchsleDrucker(IDrucker drucker) {
        this.drucker = drucker;
    }

}
