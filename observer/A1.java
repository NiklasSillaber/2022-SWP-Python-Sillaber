public class A1 implements Abonnent {

    @Override
    public void erhalteWetter(Wetter wetter) {
        System.out.println("A1 erhält das aktuelle Wetter: " + wetter.getDescription() + ", Temperatur: "+wetter.getTemperature()+"°C, Luftfeuchtigkeit: "+wetter.getHumidity()+"%"); 
    }
    
}
