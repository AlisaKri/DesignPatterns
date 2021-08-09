package Observer.Java;
public class WeatherStation {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();

        CurrentConditionsDisplay currentDisplay = new CurrentConditionsDisplay(weatherData);
        HeatIndexDisplay heatIndex = new HeatIndexDisplay(weatherData);
        weatherData.setMeasurements(80.0f, 65.0f, 30.4f);
        weatherData.setMeasurements(82.0f, 70.0f, 29.2f);
        weatherData.setMeasurements(78.0f, 90.0f, 29.2f);
    }
}