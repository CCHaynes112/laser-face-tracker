import serial
import time

ser = serial.Serial()
ser.port = "COM4"

ser.open()

while True:
    print("Enter coordinates: ")
    print("Or 'q' to quit")

    xLoc = input("x: ")
    yLoc = input("y: ")
    if xLoc == "q" or yLoc == "q":
        break

    xLoc = int(xLoc)
    yLoc = int(yLoc)

    coordinates = str.encode("X{x}Y{y}".format(x=xLoc, y=yLoc))

    ser.write(coordinates)
ser.close()


# namespace Laser_Servo
# {
#     public partial class Form1 : Form
#     {
#         public Stopwatch watch { get; set; }
#         public Form1()
#         {
#             InitializeComponent();
#         }

#         private void Form1_Load(object sender, EventArgs e)
#         {
#             watch = Stopwatch.StartNew();
#             port1.Open();
#         }

#         private void Form1_MouseMove(object sender, MouseEventArgs e)
#         {
#             writeToPort(new Point(e.Y, e.X));
#         }

#         public void writeToPort(Point coordinates)
#         {
#             if (watch.ElapsedMilliseconds > 15)
#             {
#                 watch = Stopwatch.StartNew();

#                 port1.Write(String.Format("X{0}Y{1}",
#                 (180 - coordinates.X / (Size.Width / 180)),
#                 ( 180 - coordinates.Y / (Size.Height / 180))));
#             }
#         }
#     }
# }
