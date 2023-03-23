package Patterns.ObserverPattern;

public class Client {
    public static void main(String[]args){
        Zentrale messzentrale = new Zentrale(); 
        messzentrale.aboHinzufügen(new A1()); 
        messzentrale.setAktuellesWetter(new Wetter("Schön",25,30)); 

        ZentralePull messzentralePull = new ZentralePull(); 
        messzentralePull.aboHinzufügen(new A2(messzentralePull)); 
        messzentralePull.setAktuellesWetter(new Wetter("Regnerisch",10,80)); 

    }
}
