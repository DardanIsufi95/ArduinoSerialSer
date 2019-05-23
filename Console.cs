using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.IO.Ports;
using System.Timers;
using Quobject.SocketIoClientDotNet.Client;

namespace ArduinoSerial
{
    class Program
    {

        private static string[] ports;
        private static System.Timers.Timer aTimer;
        private static string buffer = string.Empty;
        private static SerialPort port = new SerialPort();

        private static Thread ReadS = new Thread(ReadSerial);

        private static string l = "OFF";

        private static Quobject.SocketIoClientDotNet.Client.Socket socket;


        static void Main(string[] args)
        {
            port.BaudRate = 9600;
            var ser = Console.ReadLine().Trim();
            connect();
            Console.WriteLine("Connected on port : "+port.PortName);
            aTimer = new System.Timers.Timer();
            aTimer.Interval = 1500;
            
            socket = IO.Socket(ser);

            socket.On("NTC", (data) =>
            {
                if(data.ToString() != l)
                {
                    l = data.ToString();
                    port.WriteLine(data.ToString()); ;
                }
                Console.WriteLine(data.ToString());
                
                
            });
            
        }
        public static void ReadSerial()
        {
            while (true)
            {
                buffer = string.Empty;
                string data = port.ReadLine();
                if (data.Length == 12)
                {
                    Console.WriteLine(data);
                    socket.Emit("CTN", data);
                }

            }
        }


        public static void connect()
        {
            Console.WriteLine("Waiting For Arduino!");
            ports = SerialPort.GetPortNames();
            foreach (string p in ports)
            {
                port.PortName = p;
                try
                {
                    port.Open();
                    ReadS.Start();
                    return;
                }
                catch
                {
                    continue;
                }
            }
            Thread.Sleep(1500);
            connect();

        }

    }
}
