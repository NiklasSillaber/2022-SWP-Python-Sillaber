package Patterns.ObserverPattern;

public class Wetter {
    private String description;
    private double temperature;
    private double humidity;

    public Wetter(String des,double temp,double humi){
        this.description = des;
        this.temperature = temp;
        this.humidity = humi;
    }

    public String getDescription(){
        return this.description;
    }

    public double getTemperature(){
        return this.temperature;
    }

    public double getHumidity(){
        return this.humidity;
    }

}
