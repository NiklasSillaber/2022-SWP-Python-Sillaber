package Patterns.ObserverPattern;
import java.util.ArrayList;

public abstract class Messstation {
    private ArrayList<Abonnent> abonnentenListe = new ArrayList<Abonnent>(); 

    public void aboHinzufügen(Abonnent abonnent) { 
        abonnentenListe.add(abonnent); 
    } 

    public void aboEntfernen(Abonnent abonnent) { 
        abonnentenListe.remove(abonnent); 
    } 

    protected void verteileWetter(Wetter wetter) { 
        for (Abonnent abonnent : abonnentenListe) { 
            abonnent.erhalteWetter(wetter); 
        } 
    }
}
