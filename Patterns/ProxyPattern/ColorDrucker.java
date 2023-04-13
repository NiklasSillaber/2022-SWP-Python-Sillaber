package Patterns.ProxyPattern;

public class ColorDrucker implements IDrucker{
    
    @Override
    public void drucken(String nachricht) {
        System.out.println(nachricht + " - Color");
    }

}
    