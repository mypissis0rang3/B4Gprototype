Para a gravacao do firmware micropython, a necessario algum trabalho manual, dispensavel após esta dita instalacao. 
Serao necessarios para essa primeira instalacao: esptool; Thonny ou análogo; e a imagem especifica do micropython, que pode ser encontrada em https://micropython.org/download/
Para o modelo ESP32-CAM desse projeto, o bin pode ser encontrado no repositorio https://github.com/lemariva/micropython-camera-driver/tree/master/firmware

Existem diversas ferramentas para as ligação PC - ESP, porém, dado que o ESP32-CAM comum não possui modulo USB, será necessário um conversor USB-Serial adequado (e jumpers ou semelhantes para a coneccao). Este ESP conta com duas entradas GND, necessárias para esse método. 

Conexão e comandos:
Conversor     ESP
TX            RX
RX            TX
5V ou 3.3V    VIN ou 3v3
GND           GND

Feito essas conexoes, ligue um cabo jumper unindo os pinos GPIO 0 e GND do ESP para iniciar o modo gravação - não interrompa a conexão GND - GND pre-estabelecida entre o conversor e o ESP.

Conecte o conversor ao PC.

Aperte o Reset do ESP32S-CAM.

No seu pc, no terminal (se for necessario utilize ambiente virtual), para apagar o flash e gravar o firmware:
bash
esptool erase_flash
epstool write_flash -z 0x1000 firmware.bin

Substitua "firmware" com o nome do arquivo. Pode ser necessário especificar o port.

Completo o upload, remova o jumper GND - GPIO 0 e pressione reset novamente.

Agora faca upload de main.py ao ESP, aqui usarei Thonny para isso.


