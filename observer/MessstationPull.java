

import java.util.ArrayList;

public abstract class MessstationPull {
    private ArrayList<AbonnentPull> abonnentenListe = new ArrayList<AbonnentPull>(); 

    public void aboHinzufügen(AbonnentPull abonnent) { 
        abonnentenListe.add(abonnent); 
    } 

    public void aboEntfernen(AbonnentPull abonnent) { 
        abonnentenListe.remove(abonnent); 
    } 

    protected void verteileWetterPull() { 
        for (AbonnentPull abonnent : abonnentenListe) { 
            abonnent.updateWetter(); 
        } 
    } 
}
