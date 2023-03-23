public class Zentrale extends Messstation {
    
    private Wetter aktuellesWetter; 

    public void setAktuellesWetter(Wetter aktuellesWetter) { 
        this.aktuellesWetter = aktuellesWetter; 
        verteileWetter(aktuellesWetter); 
    } 

    public Wetter getAktuellesWetter() { 
        return aktuellesWetter; 
    }

}
