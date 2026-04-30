#include <pthread.h>
#include <ncurses.h>

// Hilo para actualizar la pantalla (La "Raid")
void* update_screen(void* arg) {
    while(1) {
        mvprintw(1, 1, "Enemigo: Dragon | HP: %d", dragon_hp);
        refresh(); // Dibuja los cambios
        usleep(500000); // Espera medio segundo
    }
}

// Hilo principal para tu comando
int main() {
    initscr(); // Inicia modo ncurses
    pthread_create(&thread_id, NULL, update_screen, NULL);
    
    while(1) {
        move(20, 1); // Mueve el cursor al área de comandos
        printw("$: ");
        getstr(comando); // Se queda esperando tu comando aquí
        procesar_comando(comando);
    }
}