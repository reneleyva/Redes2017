#include <pcap.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include "headers.h"
#include <glib.h>

/*************
    Clase Main para capturar paquetes en pcap.
 **********/

/* Método que toma un paquete y el indice donde inicia el payload para saltarse el header de Ethernet, IP y TCP 
 * Luego imprime el paquete según su tipo. 
 */
void imprimePaquete(const u_char *packet, int len, int inicio_payload) {
   
    //ES GET
    if (packet[inicio_payload] == 0x47 && packet[inicio_payload+1] == 0x45 
        && packet[inicio_payload+2] == 0x54) {
        
        printf("\n************************************************\n");
        printf("--PETICION--\n\n");
        printf("  METODO: GET\n");
        printf("  URL: ");
        for (int i = inicio_payload+3; i < len; i++)
        {
            if (packet[i] == 0x0d && packet[i+1] == 0x0a) {
                //ES el simbolo \r\n
                printf("\n  ");
                i++;
            } else { 
                printf("%c", (char) packet[i]);
            }
        }
        printf("\n************************************************\n");
        // printf("LENGTH: %d\n", len);
    } else if (packet[inicio_payload] == 0x50 && packet[inicio_payload+1] == 0x4f && 
                        packet[inicio_payload+2] == 0x53 && packet[inicio_payload+3] == 0x54) {
        //ES POST
        printf("\n************************************************\n");
        printf("--PETICION--\n\n");
        printf("  METODO: POST\n");
        printf("  URL: ");
        for (int i = inicio_payload+4; i < len; i++)
        {
            if (packet[i] == 0x0d && packet[i+1] == 0x0a) {
                //ES el simbolo \r\n
                printf("\n   ");
                i++;
            } else { 
                printf("%c", (char) packet[i]);
            }
        }
        printf("\n************************************************\n");

    } else if (packet[inicio_payload] == 0x48 && packet[inicio_payload+1] == 0x45 && 
                        packet[inicio_payload+2] == 0x41 && packet[inicio_payload+3] == 0x44) {

        //ES HEAD
        printf("\n************************************************\n");
        printf("--PETICION--\n\n");
        printf("  METODO: HEAD\n");
        printf("  URL: ");
        for (int i = inicio_payload+4; i < len; i++)
        {
            if (packet[i] == 0x0d && packet[i+1] == 0x0a) {
                //ES el simbolo \r\n
                printf("\n  ");
                i++;
            } else { 
                printf("%c", (char) packet[i]);
            }
        }
        printf("\n************************************************\n");   
    } else if (packet[inicio_payload] == 0x50 && packet[inicio_payload+1] == 0x55 && packet[inicio_payload+2] == 0x54) {

        //ES PUT
        printf("\n************************************************\n");
        printf("--PETICION--\n\n");
        printf("  METODO: PUT\n");
        printf("  URL: ");
        for (int i = inicio_payload+3; i < len; i++)
        {
            if (packet[i] == 0x0d && packet[i+1] == 0x0a) {
                //ES el simbolo \r\n
                printf("\n  ");
                i++;
            } else { 
                printf("%c", (char) packet[i]);
            }
        }
        printf("\n************************************************\n");
    } else if (packet[inicio_payload] == 0x48 && packet[inicio_payload+1] == 0x54 && 
                        packet[inicio_payload+2] == 0x54 && packet[inicio_payload+3] == 0x50) {
        int count = 0; //Cuenta los saltos
        //ES de respuesta. 
        printf("\n************************************************\n");
        printf("-RESPUESTA-\n\n");
        printf("  VERSION:");
        for (int i = inicio_payload; i < len; i++)
        {
            if (packet[i] == 0x0d && packet[i+1] == 0x0a && packet[i+2] == 0x0a) {
                //ES el simbolo \r\n
                count++;
                printf("\n  ");
                i+=2;
            } if (count == 8) {
                break; //Para evitar que imprima el contenido extraño
            } else { 
                printf("%c", (char) packet[i]);
            }
        }
        printf("\n************************************************\n");
    }
    
}



/* Callback de  pcap_loop para lidiar con el paquete se captura indefinidamente, */
void got_packet(u_char *args, struct pcap_pkthdr *header, 
	const u_char *packet) {

	// printf("CAPTURANDO ANDO...\n");
	//Aqui se hacen los typecast 
    /* ethernet headers som de exactamente 14 bytes */
    #define SIZE_ETHERNET 14

    const struct ethernet_header *ethernet; /* Ethernet header */
    const struct ip_header *ip; /* IP header */
    const struct tcp_header *tcp; /* TCP header */
    const char *payload; /* payload */

    
    u_int size_ip;
    u_int size_tcp;

    ethernet = (struct ethernet_header*)(packet);
    ip = (struct ip_header*)(packet + SIZE_ETHERNET);
    size_ip = IP_HL(ip)*4;
    if (size_ip < 20) {
        printf("   * Invalid IP header length: %u bytes\n", size_ip);
        return;
    }
    tcp = (struct tcp_header*)(packet + SIZE_ETHERNET + size_ip);
    size_tcp = TH_OFF(tcp)*4;
    if (size_tcp < 20) {
        printf("   * Tamaño de header de TCP inválido: %u bytes\n", size_tcp);
        return;
    }

    //Typecast to request or response. 
    int inicio_payload = (int) (SIZE_ETHERNET + size_ip + size_tcp);

    payload = (u_char *)(packet + SIZE_ETHERNET + size_ip + size_tcp);

    //Llama a método auxiliar 
    imprimePaquete(packet, header->len, inicio_payload);

}

/* Le da a alegir al usuario entre todos los dispositivos disponibles y 
 * Captura paquetes indefinidamente el en dispositivo que elija el usuario .
 */
int capturarIndef() {
	
	//Definiciones 
	char errbuf[PCAP_ERRBUF_SIZE];	/* Error string */
    pcap_if_t* deviceList; //Lista de dispositivos
    pcap_if_t *d; //Para recorrer
    pcap_t *captura; //La caputura
    struct bpf_program fp;      /* The compiled filter */
    char filter_exp[] = "port 80";  /* Filtro TELNET*/
    char chosen_dev[30]; //El dispositivo elegido
    bpf_u_int32 mask;       /* The netmask of our sniffing device */
    bpf_u_int32 net;       /* The IP of our sniffing device */
    int flag = 0; //para ver si se encontŕó el dispositivo en la lista. 
   
   	printf("Todos las interfaces de Red: \n\n");

    pcap_findalldevs(&deviceList, errbuf);//Obtiene los dispositivos
    for (d = deviceList; d != NULL; d = d->next) {
    	printf("   - %s \n",(d->name));
    }

    printf("\nEscoge un dispositivo de Red: ");
    scanf("%s", chosen_dev);
    

    //Checa si lo que introdujo el usuario es un nombre correcto de interfaz
    for (d = deviceList; d != NULL; d = d->next) {
    	//Checa si son iguales
        if (!strcmp(d->name, chosen_dev)) {
        	flag = 1;
        	break;
        }
    }

    if (!flag) {
    	printf("Dispositivo \"%s\" Inválido!\n", chosen_dev);
    	return EXIT_FAILURE;
    } else {
    	printf("Captutando desde: \"%s\" ...\n", chosen_dev);
    }

    //Empieza a capturar desde chosen_dev
    if (pcap_lookupnet(chosen_dev, &net, &mask, errbuf) == -1) {
         fprintf(stderr, "Can't get netmask for device %s\n", chosen_dev);
         net = 0;
         mask = 0;
     }

    captura = pcap_open_live(chosen_dev, BUFSIZ, 1, 1000, errbuf);
    if (captura == NULL) {
        fprintf(stderr, "No se pudo abrir el dispositivo %s: %s\n", chosen_dev, errbuf);
        return EXIT_FAILURE;
    }
    /* Compile and apply the filter */
    if (pcap_compile(captura, &fp, filter_exp, 0, net) == -1) {
        fprintf(stderr, "No se puede aplicar filtro %s: %s\n", filter_exp, pcap_geterr(captura));
        return EXIT_FAILURE;
    }

    if (pcap_setfilter(captura, &fp) == -1) {
        fprintf(stderr, "Couldn't install filter %s: %s\n", filter_exp, pcap_geterr(captura));
        return EXIT_FAILURE;
    }

    return pcap_loop(captura, -1,  (pcap_handler)got_packet, NULL);

}

/* Regresa la extension del archivo */
const char *get_filename_ext(const char *filename) {
    const char *dot = strrchr(filename, '.');
    if(!dot || dot == filename) return "";
    return dot + 1;
}

/* Recibe el nombre del archivo pcap y lo lee. */
void readPcapFile(char const * name) {
    
    if ( strcmp(get_filename_ext(name), "pcap") != 0) {
        printf("Extension del archivo no permitido!!\n");
        return;
    } 

    int c;
    FILE *file;
    struct global_header * globalHeader; //Header global de los datos. 
    struct packet_header * packetHeader; //header de los paquetes en los datos.

    file = fopen(name, "r");
    //Busca el final de archivo para obtener tamaño. 
    fseek(file, 0L, SEEK_END);
    int size = ftell(file);
    rewind(file);

    u_char data[size]; //Arreglo que contendrá todo el contenido del archivo.
    int i = 0; //indice
    printf("Size: %d\n", size);
    if (file) {
        while ((c = getc(file)) != EOF)
            data[++i] = (u_char) c;
        fclose(file);
    } else {
        printf("ARCHIVO NO ENCONTRADO CHAVAL!\n");
    }

    globalHeader = (struct global_header*)(data+1);

    for (int i = 0; i < size;i++)
    {
        packetHeader = (struct packet_header*)(data  + i);
        imprimePaquete(data, i+300, i);        
    }
    

    // printf("orig_len: %x\n", packetHeader->orig_len);    


    /* Contruir apuntador de u_char que sea el paquete con tamaño data  data + sizeof(globalHeader) + packet->orig_len
        Y pasarlo a got it packet. 
    */    
}

int main(int argc, char const *argv[])
{
	
	if (argc == 2) {
        readPcapFile(argv[1]);
	} else {
		return capturarIndef();
	}
	return 0;

}