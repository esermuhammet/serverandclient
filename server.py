{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80256319",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sunucu dinleniyor...\n"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "import threading\n",
    "import sys\n",
    "\n",
    "# Sunucu adresi ve port numarası\n",
    "HOST = '127.0.0.1'  # localhost\n",
    "PORT = 7545\n",
    "\n",
    "# Bağlı istemcilerin listesi ve sıcaklık, hız, voltage verilerini tutacak liste\n",
    "clients = []\n",
    "temperature_val = []\n",
    "speed_val = []\n",
    "voltage_val = []\n",
    "\n",
    "\n",
    "def handle_client(client_socket):\n",
    "    while True:\n",
    "        try:\n",
    "            # İstemciden veri al\n",
    "            data = client_socket.recv(1024)\n",
    "            if not data:\n",
    "                # Veri alınmadıysa bağlantıyı kapat\n",
    "                print(\"İstemci bağlantısı kapatıldı.\")\n",
    "                clients.remove(client_socket)\n",
    "                client_socket.close()\n",
    "                break\n",
    "            else:\n",
    "                # Gelen veriyi işle\n",
    "                message = data.decode()\n",
    "                if message.startswith(\"write*4*\"):\n",
    "                    write_temperature(message)\n",
    "                elif message.startswith(\"read*4\"):\n",
    "                    read_temperature(client_socket)\n",
    "                elif message.startswith(\"write*5*\"):\n",
    "                    write_speed(message)\n",
    "                elif message.startswith(\"read*5\"):\n",
    "                    read_speed(client_socket)\n",
    "                elif message.startswith(\"write*6*\"):\n",
    "                    write_voltage(message)\n",
    "                elif message.startswith(\"read*6\"):\n",
    "                    read_voltage(client_socket)\n",
    "                else:\n",
    "                    print(\"Bilinmeyen komut:\", message)\n",
    "        except socket.error as e:\n",
    "            # Hata durumunda istemciyi listeden çıkar ve bağlantıyı kapat\n",
    "            print(e)\n",
    "            clients.remove(client_socket)\n",
    "            client_socket.close()\n",
    "            break\n",
    "\n",
    "def write_temperature(message):\n",
    "    new_temperature = int(message.split(\"*\")[2])\n",
    "    temperature_val.clear()  # Tüm önceki değerleri sil\n",
    "    temperature_val.append(new_temperature)\n",
    "    print(\"Sıcaklık verisi güncellendi:\", new_temperature)\n",
    "\n",
    "def read_temperature(client_socket):\n",
    "    if temperature_val:\n",
    "        client_socket.send(str(temperature_val[-1]).encode())\n",
    "    else:\n",
    "        client_socket.send(\"Sıcaklık verisi bulunamadı.\".encode())\n",
    "def write_speed(message):\n",
    "    try:\n",
    "        new_speed = int(message.split(\"*\")[2])\n",
    "        speed_val.clear()  # Tüm önceki değerleri sil\n",
    "        speed_val.append(new_speed)\n",
    "        print(\"Hız verisi güncellendi:\", new_speed)\n",
    "    except ValueError:\n",
    "        print(\"Hatalı hız değeri:\", message.split(\"*\")[2])\n",
    "        print(\"Hatalı hız değeri:\", message)\n",
    "\n",
    "\n",
    "def read_speed(client_socket):\n",
    "    if speed_val:\n",
    "        client_socket.send(str(speed_val[-1]).encode())\n",
    "    else:\n",
    "        client_socket.send(\"Hız verisi bulunamadı.\".encode())\n",
    "def write_voltage(message):\n",
    "    new_voltage = int(message.split(\"*\")[2])\n",
    "    voltage_val.clear()  # Tüm önceki değerleri sil\n",
    "    voltage_val.append(new_voltage)\n",
    "    print(\"Voltage verisi güncellendi:\", new_voltage)\n",
    "\n",
    "\n",
    "def read_voltage(client_socket):\n",
    "    if voltage_val:\n",
    "        client_socket.send(str(voltage_val[-1]).encode())\n",
    "    else:\n",
    "        client_socket.send(\"Voltage verisi bulunamadı.\".encode())\n",
    "\n",
    "def start_server():\n",
    "    # IPv4 ve TCP soketi oluştur\n",
    "    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
    "    server.bind((HOST, PORT))\n",
    "    server.listen()\n",
    "\n",
    "    print(\"Sunucu dinleniyor...\")\n",
    "\n",
    "    while True:\n",
    "        # İstemci bağlantıları kabul et\n",
    "        client_socket, client_address = server.accept()\n",
    "        print(f\"{client_address} adresinden istemci bağlandı.\")\n",
    "\n",
    "        # Bağlı istemciler listesine ekle\n",
    "        clients.append(client_socket)\n",
    "\n",
    "        # İstemci işlemleri için yeni bir thread başlat\n",
    "        client_handler = threading.Thread(target=handle_client, args=(client_socket,))\n",
    "        client_handler.start()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    start_server()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1caaaa7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "360680b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}