package Patterns.ObserverPattern;

public class ZentralePull extends MessstationPull {
    private Wetter aktuellesWetter; 

    public void setAktuellesWetter(Wetter aktuellesWetter) { 
        this.aktuellesWetter = aktuellesWetter; 
        verteileWetterPull(); 
    } 

    public Wetter getAktuellesWetter() { 
        return aktuellesWetter; 
    }
}
