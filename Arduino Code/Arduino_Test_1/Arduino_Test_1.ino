const int motor_left1 = 3;
const int motor_left2 = 4;

void setup()
{
    Serial.begin(9600);

    pinMode(motor_left1, OUTPUT);
    pinMode(motor_left2, OUTPUT);
}

void loop()
{
    if (Serial.available())
    {
        char c = Serial.read();

        if (c == '1')
        {
            digitalWrite(motor_left1, HIGH);
            digitalWrite(motor_left2, LOW);
        }

        if (c == '0')
        {
            digitalWrite(motor_left1, LOW);
            digitalWrite(motor_left2, LOW);
        }
    }
}