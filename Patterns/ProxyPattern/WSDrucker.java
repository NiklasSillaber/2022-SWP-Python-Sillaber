package Patterns.ProxyPattern;

public class WSDrucker implements IDrucker {
    
    @Override
    public void drucken(String nachricht) {
        System.out.println(nachricht + " - WS");
    }

}
