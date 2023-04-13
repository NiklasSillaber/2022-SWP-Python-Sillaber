package Patterns.ObserverPattern;

public class A2 implements AbonnentPull {

    private ZentralePull zentrale;

    public A2(ZentralePull z){
        this.zentrale = z;
    }

    @Override
    public void updateWetter() {
        Wetter w = zentrale.getAktuellesWetter();
        System.out.println("A2 erhält das aktuelle Wetter: " + w.getDescription() + ", Temperatur: "+w.getTemperature()+"°C, Luftfeuchtigkeit: "+w.getHumidity()+"%"); 
    }
    
}